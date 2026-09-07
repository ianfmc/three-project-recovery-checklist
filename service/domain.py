"""Validate every saved state, including imports; no browser-only release rules."""
import copy
from datetime import datetime,timezone
TASK_FIELDS={'status','targetDate','evidence','blockerReason','nextAction','workingNote'}
COST_FIELDS={'model','tier','elapsedHours','credits','correctionLoops','testFailures','humanReworkMinutes','timeToGreenMinutes','cost','currency','adoptionDecision','note'}
STATUSES={'backlog','ready','doing','blocked','done','deferred'}
def now():return datetime.now(timezone.utc).isoformat(timespec='seconds')
def text(v,limit=10000):
 if not isinstance(v,str) or len(v)>limit:raise ValueError('Text is missing or too long.')
 return v.strip()
def validate(doc):
 tasks=doc['tasks']; ids={t['id']:t for t in tasks};dec={d['id']:d for d in doc['decisions']}
 if len(ids)!=len(tasks) or len(dec)!=len(doc['decisions']):raise ValueError('Duplicate IDs.')
 active=set();visited=set();visiting=set()
 def visit(id):
  if id in visiting:raise ValueError('Circular dependencies.')
  if id in visited:return
  if id not in ids:raise ValueError('Unknown prerequisite: '+id)
  visiting.add(id)
  for dep in ids[id]['dependencies']:visit(dep)
  visiting.remove(id);visited.add(id)
 for t in tasks:
  visit(t['id'])
  if t['status'] not in STATUSES:raise ValueError('Invalid task status.')
  for k in ('evidence','blockerReason','nextAction','workingNote'):text(t[k])
  if t['targetDate']:
   datetime.strptime(t['targetDate'],'%Y-%m-%d')
  if t['status']=='blocked' and (not t['blockerReason'].strip() or not t['nextAction'].strip()):raise ValueError('Blocked work needs both a reason and a next unblocking action.')
  if any(id not in dec for id in t['decisionDependencies']):raise ValueError('Unknown decision prerequisite.')
  if t['status'] in ('done','doing'):
   missing=[id for id in t['dependencies'] if ids[id]['status']!='done']+[id for id in t['decisionDependencies'] if dec[id]['status']!='resolved']
   if missing:raise ValueError(t['id']+' requires '+', '.join(missing)+'. Reopen dependent tasks before reopening a prerequisite.')
  if t['status']=='done':
   if t['releaseGate'] and not t['evidence'].strip():raise ValueError(t['id']+' needs evidence before completion.')
   if not t.get('completedAt'):raise ValueError('Completion timestamp is required.')
   datetime.fromisoformat(t['completedAt'].replace('Z','+00:00'))
  elif t.get('completedAt'):raise ValueError('Open tasks cannot have completion timestamps.')
  if t['project']=='AT' and ('http://' in t['evidence'].lower() or 'https://' in t['evidence'].lower()):raise ValueError('AT evidence must use sanitized text labels, not links.')
  if any(s in (t['evidence']+' '+t['workingNote']).lower() for s in ('x-amz-signature=','x-amz-credential=','aws_secret_access_key=')):raise ValueError('Remove signed URLs or credentials from notes/evidence.')
 for d in doc['decisions']:
  if d['status'] not in ('open','resolved'):raise ValueError('Invalid decision status.')
  text(d['recordedDecision']);text(d['note'])
  if d['status']=='resolved' and not d['recordedDecision'].strip():raise ValueError('A resolved decision needs a recorded answer.')
 for p in doc['projects']:
  if p.get('latestNote'):
   text(p['latestNote']['text']);text(p['latestNote']['owner'],100)
  for k,v in p['cost'].items():text(v)
  if p['cost']['tier'] not in ('Economy','Standard','Frontier'):raise ValueError('Model tier must be Economy, Standard, or Frontier.')
  if p['cost']['tier']=='Frontier' and not p['cost']['note'].strip():raise ValueError('Record the explicit escalation reason for Frontier use.')
 for g in doc['gates']:
  if not g['taskIds'] or any(id not in ids or not ids[id]['releaseGate'] for id in g['taskIds']):raise ValueError('Invalid release gate.')
 return doc

def apply_change(original,body,seed):
 if body.get('revision')!=original['revision']:raise RuntimeError('Progress changed on another device. Close this editor, refresh, and retry; your unsaved fields remain here.')
 doc=copy.deepcopy(original);op=body.get('operation');id=body.get('id');patch=body.get('patch',{});time=now()
 if not isinstance(patch,dict):raise ValueError('Invalid update.')
 if op=='task':
  t=next((t for t in doc['tasks'] if t['id']==id),None)
  if not t or set(patch)-TASK_FIELDS:raise ValueError('Unknown task or unsupported task fields.')
  prior=t['status']
  for k,v in patch.items():t[k]=None if k=='targetDate' and not v else text(v)
  t['completedAt']=(t.get('completedAt') if prior=='done' else time) if t['status']=='done' else None
 elif op=='decision':
  d=next((d for d in doc['decisions'] if d['id']==id),None)
  if not d or set(patch)-{'status','recordedDecision','note'}:raise ValueError('Invalid decision update.')
  d.update({k:text(v) for k,v in patch.items()})
 elif op in ('note','cost'):
  p=next((p for p in doc['projects'] if p['id']==id),None)
  if not p:raise ValueError('Unknown project.')
  if op=='note':
   owner=text(patch.get('owner'),100)
   if not owner:raise ValueError('Enter a saved-by name.')
   p['latestNote']={'text':text(patch.get('text')),'owner':owner,'updatedAt':time}
  else:
   if set(patch)-COST_FIELDS:raise ValueError('Invalid cost fields.')
   p['cost'].update({k:text(v) for k,v in patch.items()})
 elif op=='import':
  imported=body.get('document')
  if not isinstance(imported,dict) or imported.get('schemaVersion')!=1:raise ValueError('Choose a checklist JSON export.')
  for collection in ('tasks','decisions','projects'):
   rows=imported.get(collection)
   if not isinstance(rows,list) or len(rows)!=len(doc[collection]) or {r.get('id') for r in rows}!={r['id'] for r in doc[collection]}:raise ValueError('Import IDs must match this checklist.')
   by_id={r['id']:r for r in rows}
   for row in doc[collection]:
    incoming=by_id[row['id']]
    keys=TASK_FIELDS|{'completedAt'} if collection=='tasks' else {'status','recordedDecision','note'} if collection=='decisions' else {'latestNote','cost'}
    for k in keys:row[k]=copy.deepcopy(incoming[k])
 elif op=='reset':doc=copy.deepcopy(seed)
 else:raise ValueError('Unsupported operation.')
 doc['revision']=original['revision']+1;doc['updatedAt']=time
 return validate(doc)
