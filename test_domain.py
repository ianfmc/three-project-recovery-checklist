import copy,json,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/'service'))
from domain import validate,apply_change
SEED=json.loads(Path('data.json').read_text())
class RulesTest(unittest.TestCase):
 def setUp(self):self.doc=copy.deepcopy(SEED)
 def task(self,id):return next(t for t in self.doc['tasks'] if t['id']==id)
 def change(self,op,id=None,patch=None,**kw):self.doc=apply_change(self.doc,dict(operation=op,id=id,patch=patch or {},revision=self.doc['revision'],**kw),SEED)
 def test_seed_graph_and_source_coverage(self):
  validate(self.doc)
  import re
  source=Path('/Users/i802235/Desktop/three-program-recovery-plan.md')
  if source.exists():
   expected=set(re.findall(r'^- ((?:AT|LW|RW)-\d{3}):',source.read_text(),re.M))
   self.assertTrue(expected.issubset({t['id'] for t in self.doc['tasks']}))
  self.assertEqual(len({t['id'] for t in self.doc['tasks']}),len(self.doc['tasks']))
  self.assertTrue(all(t['owner']=='Ian' and t['id'].startswith(t['project']+'-') for t in self.doc['tasks']))
 def finish_setup(self,project):
  def finish(id):
   t=self.task(id)
   for dep in t['dependencies']:finish(dep)
   t.update(status='done',completedAt='2026-09-05T12:00:00+00:00',evidence='Setup verified')
  finish(project+'-635')
  validate(self.doc)
 def test_setup_blocks_project_work(self):
  for id in ('AT-101','LW-101','RW-101'):
   with self.assertRaisesRegex(ValueError,'635'):self.change('task',id,{'status':'doing'})
  self.finish_setup('AT');self.change('task','AT-101',{'status':'doing'})
 def test_evidence_gate(self):
  self.finish_setup('LW')
  with self.assertRaisesRegex(ValueError,'evidence'):self.change('task','AT-106',{'status':'done'}) if self.task('AT-106')['releaseGate'] else self.change('task','LW-301',{'status':'done'})
 def test_dependencies(self):
  with self.assertRaisesRegex(ValueError,'requires'):self.change('task','AT-201',{'status':'done','evidence':'Verified'})
 def test_decision_prerequisite(self):
  with self.assertRaisesRegex(ValueError,'AT-D02'):self.change('task','AT-102',{'status':'doing'})
 def test_multiple_doing_preserves_existing_progress(self):
  self.finish_setup('AT')
  self.change('task','AT-106',{'status':'doing'})
  self.change('task','AT-107',{'status':'doing'},switchDoing=True)
  self.assertEqual(self.task('AT-106')['status'],'doing')
  self.assertEqual(self.task('AT-107')['status'],'doing')
 def test_blocker_fields(self):
  with self.assertRaisesRegex(ValueError,'Blocked'):self.change('task','RW-101',{'status':'blocked'})
  self.change('task','RW-101',{'status':'blocked','blockerReason':'Missing fixture','nextAction':'Create minimal fixture'})
 def test_complete_reopen_preserves(self):
  self.change('task','AT-601',{'status':'done','evidence':'Installed','workingNote':'Resume here'})
  self.assertIsNotNone(self.task('AT-601')['completedAt'])
  self.change('task','AT-601',{'status':'ready'})
  self.assertIsNone(self.task('AT-601')['completedAt']);self.assertEqual(self.task('AT-601')['evidence'],'Installed')
 def test_notes_cost_decisions(self):
  self.change('note','RW',{'text':'A note','owner':'Ian'})
  self.change('cost','RW',{'credits':'12','model':'Evaluation model'})
  self.change('decision','RW-D02',{'status':'resolved','recordedDecision':'Keep current architecture'})
  self.assertEqual(self.doc['projects'][2]['latestNote']['text'],'A note')
 def test_conflict(self):
  with self.assertRaises(RuntimeError):apply_change(self.doc,dict(operation='reset',revision=900),SEED)
 def test_import_validation_and_definitions(self):
  incoming=copy.deepcopy(SEED);incoming['tasks'][0]['title']='Overwritten';self.change('import',document=incoming)
  self.assertNotEqual(self.doc['tasks'][0]['title'],'Overwritten')
  incoming['tasks'][0]['status']='done'
  with self.assertRaises(ValueError):self.change('import',document=incoming)
 def test_reset(self):
  self.change('note','AT',{'text':'Test','owner':'Ian'});self.change('reset')
  self.assertIsNone(self.doc['projects'][0]['latestNote']);self.assertEqual(self.doc['revision'],2)
 def test_cycle(self):
  self.task('AT-601')['dependencies']=['AT-602']
  with self.assertRaisesRegex(ValueError,'Circular'):validate(self.doc)
 def test_no_signed_evidence(self):
  with self.assertRaises(ValueError):self.change('task','RW-101',{'evidence':'https://test/?X-Amz-Signature=secret'})
 def test_frontier_reason(self):
  with self.assertRaisesRegex(ValueError,'escalation'):self.change('cost','RW',{'tier':'Frontier'})
  self.change('cost','RW',{'tier':'Frontier','note':'Explicit escalation for tenant-isolation review'})
if __name__=='__main__':unittest.main()
