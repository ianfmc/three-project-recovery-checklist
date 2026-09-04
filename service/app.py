import base64,hmac,json,os
import boto3
from botocore.exceptions import ClientError
from domain import apply_change
s3=boto3.client('s3');BUCKET=os.environ['DATA_BUCKET'];KEY='data.json';TOKEN=os.environ['ACCESS_TOKEN']
with open('data.json') as f:SEED=json.load(f)
def reply(code,body):return {'statusCode':code,'headers':{'Content-Type':'application/json','Cache-Control':'no-store'},'body':json.dumps(body)}
def lambda_handler(event,context):
 headers={k.lower():v for k,v in (event.get('headers') or {}).items()}
 if not hmac.compare_digest(headers.get('authorization',''),'Bearer '+TOKEN):return reply(401,{'message':'Open a current private checklist link.'})
 try:
  obj=s3.get_object(Bucket=BUCKET,Key=KEY);doc=json.loads(obj['Body'].read())
  method=event.get('requestContext',{}).get('http',{}).get('method')
  if method=='GET':return reply(200,{'data':doc})
  if method!='POST':return reply(405,{'message':'Method not allowed.'})
  raw=event.get('body','')
  if event.get('isBase64Encoded'):raw=base64.b64decode(raw).decode()
  if len(raw)>1000000:return reply(413,{'message':'Update too large.'})
  body=json.loads(raw)
  if not isinstance(body,dict):raise ValueError('Invalid update.')
  updated=apply_change(doc,body,SEED)
  s3.put_object(Bucket=BUCKET,Key=KEY,Body=json.dumps(updated,ensure_ascii=False).encode(),ContentType='application/json',CacheControl='no-store',ServerSideEncryption='AES256',IfMatch=obj['ETag'])
  return reply(200,{'data':updated})
 except RuntimeError as e:return reply(409,{'message':str(e)})
 except ClientError as e:
  if e.response['Error']['Code'] in ('PreconditionFailed','ConditionalRequestConflict','412','409'):return reply(409,{'message':'Another device saved first. Refresh and retry.'})
  return reply(503,{'message':'Saving is temporarily unavailable. Your change was not confirmed.'})
 except (ValueError,KeyError,TypeError,AttributeError) as e:return reply(400,{'message':str(e) if isinstance(e,ValueError) else 'Invalid checklist data.'})
 except Exception:return reply(503,{'message':'Saving is temporarily unavailable.'})
