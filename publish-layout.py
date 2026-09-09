"""Publish the existing checklist page using the scoped checklist-tools profile.
Does not provision infrastructure or modify the live checklist data.
"""
import base64,json,os
from pathlib import Path
import boto3
from botocore.config import Config
ROOT=Path(__file__).resolve().parent
from service.domain import validate
settings=json.loads((ROOT/'deployment.json').read_text())
session=boto3.Session(profile_name='checklist-tools',region_name='us-west-2')
identity=session.client('sts').get_caller_identity()
assert identity['Account']==settings['account']=='715853571315'
assert settings['bucket']=='three-program-recovery-715853571315-us-west-2'
s3=session.client('s3',endpoint_url='https://s3.us-west-2.amazonaws.com',config=Config(signature_version='s3v4',s3={'addressing_style':'virtual'}))
live=json.loads(s3.get_object(Bucket=settings['bucket'],Key='data.json')['Body'].read())
seed=validate(json.loads((ROOT/'data.json').read_text()))
for collection in ['tasks','projects','decisions']:
 assert {r['id'] for r in live[collection]}=={r['id'] for r in seed[collection]}, 'Publish matching definitions before layout.'
secret=session.client('lambda').get_function_configuration(FunctionName=settings['function'])['Environment']['Variables']['ACCESS_TOKEN']
config=json.dumps({'url':settings['api'],'token':secret,'resetSeed':seed}).replace('<','\\u003c')
css=(ROOT/'styles.css').read_text()
for font in (ROOT/'fonts').iterdir():
 if font.suffix in ['.woff2','.ttf']:
  mime=font.suffix[1:];css=css.replace('fonts/'+font.name,'data:font/'+mime+';base64,'+base64.b64encode(font.read_bytes()).decode())
html=(ROOT/'index.html').read_text().replace('<link rel="stylesheet" href="styles.css">','<style>'+css+'</style>').replace('window.CONFIG=null;','window.CONFIG='+config+';')
for file in ['logic.js','app.js']:html=html.replace(f'<script src="{file}"></script>','<script>'+(ROOT/file).read_text()+'</script>')
s3.put_object(Bucket=settings['bucket'],Key='index.html',Body=html.encode(),ContentType='text/html; charset=utf-8',CacheControl='no-cache, no-store',ServerSideEncryption='AES256')
u=s3.generate_presigned_url('get_object',Params={'Bucket':settings['bucket'],'Key':'index.html'},ExpiresIn=604800)
p=ROOT/'.private/url.txt';p.write_text(u);os.chmod(p,0o600)
print('Published layout with current reset definitions using checklist-tools; live data preserved.')
