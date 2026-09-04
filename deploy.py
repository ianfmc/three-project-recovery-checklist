"""Publish isolated resources. UI-only by default after initial deployment."""
import base64,hashlib,io,json,os,secrets,sys,zipfile
from pathlib import Path
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
ROOT=Path(__file__).resolve().parent
ACCOUNT='715853571315';REGION='us-west-2';BUCKET=f'three-program-recovery-{ACCOUNT}-{REGION}';STACK='three-program-recovery-control'
session=boto3.Session(region_name=REGION)
identity=session.client('sts').get_caller_identity()
if identity['Account']!=ACCOUNT:raise SystemExit('Wrong AWS account; deployment stopped.')
print('Verified account '+ACCOUNT+' · '+REGION,flush=True)
s3=session.client('s3',endpoint_url=f'https://s3.{REGION}.amazonaws.com',config=Config(signature_version='s3v4',s3={'addressing_style':'virtual'}));cf=session.client('cloudformation');lam=session.client('lambda')
try:s3.head_bucket(Bucket=BUCKET,ExpectedBucketOwner=ACCOUNT)
except ClientError as e:
 if e.response['Error']['Code'] not in ('404','NoSuchBucket'):raise
 s3.create_bucket(Bucket=BUCKET,CreateBucketConfiguration={'LocationConstraint':REGION})
 s3.put_bucket_tagging(Bucket=BUCKET,Tagging={'TagSet':[{'Key':'Application','Value':STACK}]})
# Existing bucket must be positively identified as ours before any publication.
tags=s3.get_bucket_tagging(Bucket=BUCKET)['TagSet']
if {'Key':'Application','Value':STACK} not in tags:raise SystemExit('Unrecognized bucket: stopped without overwriting objects.')
s3.put_public_access_block(Bucket=BUCKET,PublicAccessBlockConfiguration={k:True for k in ('BlockPublicAcls','IgnorePublicAcls','BlockPublicPolicy','RestrictPublicBuckets')})
s3.put_bucket_encryption(Bucket=BUCKET,ServerSideEncryptionConfiguration={'Rules':[{'ApplyServerSideEncryptionByDefault':{'SSEAlgorithm':'AES256'}}]})
s3.put_bucket_versioning(Bucket=BUCKET,VersioningConfiguration={'Status':'Enabled'})
policy={'Version':'2012-10-17','Statement':[{'Sid':'DenyInsecureTransport','Effect':'Deny','Principal':'*','Action':'s3:*','Resource':[f'arn:aws:s3:::{BUCKET}',f'arn:aws:s3:::{BUCKET}/*'],'Condition':{'Bool':{'aws:SecureTransport':'false'}}}]}
s3.put_bucket_policy(Bucket=BUCKET,Policy=json.dumps(policy))
try:stack=cf.describe_stacks(StackName=STACK)['Stacks'][0]
except ClientError as e:
 if 'does not exist' not in str(e):raise
 stack=None
sys.path.insert(0,str(ROOT/'service'));from domain import validate
seed=validate(json.loads((ROOT/'data.json').read_text()))
if stack is None or os.environ.get('PUBLISH_SERVICE')=='1':
 buf=io.BytesIO()
 with zipfile.ZipFile(buf,'w',zipfile.ZIP_DEFLATED) as z:
  for f in ('app.py','domain.py'):z.write(ROOT/'service'/f,f)
  z.write(ROOT/'data.json','data.json')
 package=buf.getvalue();key='service/'+hashlib.sha256(package).hexdigest()+'.zip'
 s3.put_object(Bucket=BUCKET,Key=key,Body=package,ServerSideEncryption='AES256')
 params=[{'ParameterKey':'CodeKey','ParameterValue':key},{'ParameterKey':'DataBucket','ParameterValue':BUCKET},{'ParameterKey':'DataKey','ParameterValue':'data.json'},{'ParameterKey':'AccessToken',**({'UsePreviousValue':True} if stack else {'ParameterValue':secrets.token_urlsafe(48)})}]
 args=dict(StackName=STACK,TemplateBody=(ROOT/'service/template.json').read_text(),Parameters=params,Capabilities=['CAPABILITY_IAM'])
 try:
  if stack:cf.update_stack(**args)
  else:cf.create_stack(**args)
  print('Waiting for isolated save service…',flush=True)
  cf.get_waiter('stack_update_complete' if stack else 'stack_create_complete').wait(StackName=STACK,WaiterConfig={'Delay':10,'MaxAttempts':90})
 except ClientError as e:
  if 'No updates are to be performed' not in str(e):raise
 stack=cf.describe_stacks(StackName=STACK)['Stacks'][0]
if stack['StackStatus'] not in ('CREATE_COMPLETE','UPDATE_COMPLETE'):raise SystemExit('Save service is not ready.')
try:remote=s3.get_object(Bucket=BUCKET,Key='data.json');live=json.loads(remote['Body'].read())
except ClientError as e:
 if e.response['Error']['Code']!='NoSuchKey':raise
 s3.put_object(Bucket=BUCKET,Key='data.json',Body=json.dumps(seed).encode(),ContentType='application/json',CacheControl='no-store',ServerSideEncryption='AES256',IfNoneMatch='*');live=seed
if os.environ.get('PUBLISH_DETAILS')=='1':
 from domain import TASK_FIELDS
 remote=s3.get_object(Bucket=BUCKET,Key='data.json');live=json.loads(remote['Body'].read());merged={**live,**seed}
 for collection in ('tasks','projects','decisions'):
  old={r['id']:r for r in live[collection]};merged[collection]=[]
  for row in seed[collection]:
   row=dict(row);prior=old.pop(row['id'],None)
   if prior:
    fields=TASK_FIELDS|{'completedAt'} if collection=='tasks' else {'latestNote','cost'} if collection=='projects' else {'status','recordedDecision','note'}
    row.update({k:prior[k] for k in fields})
   merged[collection].append(row)
  merged[collection].extend(old.values())
 merged['revision']=live['revision']+1;merged['updatedAt']=live['updatedAt'];validate(merged)
 s3.put_object(Bucket=BUCKET,Key='data.json',Body=json.dumps(merged).encode(),ContentType='application/json',CacheControl='no-store',ServerSideEncryption='AES256',IfMatch=remote['ETag'])
 live=merged
outputs={o['OutputKey']:o['OutputValue'] for o in stack['Outputs']}
secret=lam.get_function_configuration(FunctionName=outputs['FunctionName'])['Environment']['Variables']['ACCESS_TOKEN']
config=json.dumps({'url':outputs['ApiUrl'],'token':secret}).replace('<','\\u003c')
css=(ROOT/'styles.css').read_text()
for font in (ROOT/'fonts').iterdir():
 if font.suffix in ('.woff2','.ttf'):
  mime='woff2' if font.suffix=='.woff2' else 'ttf'
  css=css.replace('fonts/'+font.name,'data:font/'+mime+';base64,'+base64.b64encode(font.read_bytes()).decode())
html=(ROOT/'index.html').read_text().replace('<link rel="stylesheet" href="styles.css">','<style>'+css+'</style>').replace('window.CONFIG=null;','window.CONFIG='+config+';')
for f in ('logic.js','app.js'):html=html.replace(f'<script src="{f}"></script>','<script>'+(ROOT/f).read_text()+'</script>')
s3.put_object(Bucket=BUCKET,Key='index.html',Body=html.encode(),ContentType='text/html; charset=utf-8',CacheControl='no-cache, no-store',ServerSideEncryption='AES256')
url=s3.generate_presigned_url('get_object',Params={'Bucket':BUCKET,'Key':'index.html'},ExpiresIn=604800)
# Secret-bearing URL is only stored outside Git in a protected local file for opening/sharing.
local=ROOT/'.private';local.mkdir(exist_ok=True,mode=0o700);os.chmod(local,0o700)
(local/'url.txt').write_text(url);os.chmod(local/'url.txt',0o600)
(ROOT/'deployment.json').write_text(json.dumps({'account':ACCOUNT,'region':REGION,'bucket':BUCKET,'stack':STACK,'api':outputs['ApiUrl'],'function':outputs['FunctionName']},indent=2)+'\n')
print('Published private checklist; shared state preserved. URL saved in .private/url.txt',flush=True)
if '--print-url' in sys.argv:print(url)
