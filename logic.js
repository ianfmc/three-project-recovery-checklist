/* Pure scheduling and display rules, shared by UI and verification. */
(function(root){
const rank={critical:0,high:1,medium:2,low:3};
function today(){return new Intl.DateTimeFormat('en-CA',{timeZone:'America/Los_Angeles',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date())}
function tasksFor(d,p){return d.tasks.filter(t=>t.project===p)}
function included(ts){return ts.filter(t=>t.status!=='deferred'&&!t.optional)}
function progress(ts){ts=included(ts);const done=ts.filter(t=>t.status==='done').length;return {done,total:ts.length,percent:ts.length?Math.round(100*done/ts.length):0}}
function requirements(d,t){return [...t.dependencies.filter(id=>d.tasks.find(x=>x.id===id)?.status!=='done'),...t.decisionDependencies.filter(id=>d.decisions.find(x=>x.id===id)?.status!=='resolved')]}
function overdue(t,date=today()){return Boolean(t.targetDate)&&t.targetDate<date&&!['done','deferred'].includes(t.status)}
function compare(a,b){return (rank[a.priority]??4)-(rank[b.priority]??4)||(a.targetDate||'9999').localeCompare(b.targetDate||'9999')||a.id.localeCompare(b.id)}
function next(d,p,date=today(),track=null){
 const setupId=d.projects.find(x=>x.id===p)?.setupGate;
 if(setupId&&d.tasks.find(t=>t.id===setupId)?.status!=='done'){
  const ancestors=new Set();function gather(id){if(ancestors.has(id))return;ancestors.add(id);const t=d.tasks.find(t=>t.id===id);if(t)for(const dep of t.dependencies)gather(dep)}gather(setupId);
  const pending=d.tasks.filter(t=>ancestors.has(t.id)&&t.status!=='done');
  const ready=pending.filter(t=>['ready','doing'].includes(t.status)&&!requirements(d,t).length&&(t.status==='doing'||!t.startDate||t.startDate<=date)).sort((a,b)=>(a.status==='doing'?-1:0)-(b.status==='doing'?-1:0)||compare(a,b));
  if(ready.length)return {kind:'task',item:ready[0],reason:(ready[0].project===p?'':'Shared installation prerequisite. ')+'Complete Kiro and gstack setup before project work.'};
  const blocker=pending.filter(t=>t.status==='blocked'&&!requirements(d,t).length).sort(compare)[0];
  if(blocker)return {kind:'blocker',item:blocker,reason:blocker.nextAction};
  const scheduled=pending.filter(t=>t.status==='ready'&&!requirements(d,t).length).sort((a,b)=>(a.startDate||'').localeCompare(b.startDate||'')||compare(a,b))[0];
  if(scheduled)return {kind:'scheduled',item:scheduled,reason:'Installation prerequisite scheduled for '+scheduled.startDate+'.'};
  return {kind:'waiting',reason:'Finish or unblock the Kiro and gstack installation steps before starting project work.'};
 }
 if(!track&&d.projects.find(x=>x.id===p)?.tracks){const branches=nextByTrack(d,p,date).filter(x=>x.track.mode==='active');return branches.find(x=>['task','decision','blocker'].includes(x.result.kind))?.result||branches.find(x=>x.result.kind!=='complete')?.result||{kind:'complete',reason:'All active branches are complete.'};}
 const ts=tasksFor(d,p).filter(t=>t.status!=='deferred'&&t.status!=='done'&&(track?t.track===track:!t.optional));
 if(!ts.length)return {kind:'complete',reason:'All included work is complete.'};
 const ready=ts.filter(t=>!requirements(d,t).length&&t.status!=='blocked'&&!t.conditional&&(t.status==='ready'||t.status==='doing')&&(t.status==='doing'||!t.startDate||t.startDate<=date));
 const choose=ready.filter(t=>t.status==='doing').sort(compare)[0]||ready.filter(t=>t.critical).sort(compare)[0]||ready.filter(t=>t.targetDate&&t.targetDate<date).sort(compare)[0]||ready.sort(compare)[0];
 const decision=d.decisions.filter(x=>x.project===p&&x.status==='open'&&x.blocks.some(id=>ts.some(t=>t.id===id&&(t.critical||t.releaseGate)))).sort((a,b)=>a.dueDate.localeCompare(b.dueDate))[0];
 // Doing wins; an overdue critical-path decision precedes fresh work.
 if(decision&&(!choose||choose.status!=='doing'&&decision.dueDate<=date))return {kind:'decision',item:decision,reason:'Resolve this decision to unblock critical work.'};
 if(choose)return {kind:'task',item:choose,reason:choose.status==='doing'?'Continue the work already in progress.':choose.critical?'Critical work; required prerequisites are complete.':choose.targetDate&&choose.targetDate<date?'Overdue and ready to work.':'Highest-priority work ready to start.'};
 const blocked=ts.filter(t=>t.status==='blocked'&&!requirements(d,t).length).sort(compare)[0];
 if(blocked)return {kind:'blocker',item:blocked,reason:blocked.nextAction};
 if(decision)return {kind:'decision',item:decision,reason:'Record the decision before dependent work starts.'};
 const future=ts.filter(t=>!requirements(d,t).length&&!t.conditional&&t.status==='ready').sort((a,b)=>(a.startDate||'').localeCompare(b.startDate||'')||compare(a,b))[0];
 if(future)return {kind:'scheduled',item:future,reason:'Scheduled for '+future.startDate+'. Available to work ahead.'};
 const pending=[...new Set(ts.flatMap(t=>requirements(d,t)))],frontier=new Set();
 function trace(id,seen=new Set()){if(seen.has(id))return;seen.add(id);const task=d.tasks.find(t=>t.id===id);if(!task){frontier.add(id);return}const req=requirements(d,task);if(req.length)req.forEach(dep=>trace(dep,seen));else frontier.add(id)}pending.forEach(id=>trace(id));
 return {kind:'waiting',reason:frontier.size?'Waiting on '+[...frontier].join(', ')+'. Other prerequisites follow after these.':'No executable task. Review unresolved prerequisites, backlog, or conditional work.'};
}
function nextByTrack(d,p,date=today()){const project=d.projects.find(x=>x.id===p),setup=project?.setupGate;if(setup&&d.tasks.find(t=>t.id===setup)?.status!=='done')return [{track:{id:'setup',name:'Complete installation first',mode:'active'},result:next(d,p,date,'setup')}];return (project?.tracks||[{id:null,name:'Next action',mode:'active'}]).map(track=>({track,result:track.mode==='conditional'?{kind:'waiting',reason:'Deferred until the research result supports explicit production adoption.'}:next(d,p,date,track.id)}));}
function gateDone(d,g){return g.taskIds.every(id=>d.tasks.some(t=>t.id===id&&t.status==='done'&&t.evidence.trim()))}
function health(d,p,date=today()){
 const ts=included(tasksFor(d,p)),gs=d.gates.filter(g=>g.project===p&&!g.optional&&!g.conditional);
 if(gs.length&&gs.every(g=>gateDone(d,g)))return {label:'Complete',reason:'All release gates have verified evidence.'};
 const blocked=ts.find(t=>(t.critical||t.releaseGate)&&t.status==='blocked');
 if(blocked)return {label:'Blocked',reason:blocked.id+': '+blocked.blockerReason};
 const decision=d.decisions.find(x=>x.project===p&&x.status==='open'&&x.dueDate<=date&&x.blocks.some(id=>ts.some(t=>t.id===id&&t.status!=='done'&&(t.status==='doing'||!t.startDate||t.startDate<=date)&&(t.critical||t.releaseGate))));
 if(decision)return {label:'Blocked',reason:decision.id+': '+decision.title};
 const late=ts.find(t=>t.critical&&t.status!=='done'&&t.targetDate&&t.targetDate<date);
 if(late)return {label:'At Risk',reason:late.id+' is overdue.'};
 const milestone=d.milestones.find(m=>m.project===p&&m.targetDate<date&&ts.some(t=>t.track!=='setup'&&t.milestone===m.id&&t.status!=='done'));
 if(milestone)return {label:'At Risk',reason:milestone.name+' milestone is overdue.'};
 if(d.projects.find(x=>x.id===p).deadline<date)return {label:'At Risk',reason:'Release date has passed with gates still open.'};
 return {label:'On Track',reason:'No recorded critical blocker or overdue milestone; this is a rule-based status, not a forecast.'};
}
function lane(d,p,date=today()){return d.projects.find(x=>x.id===p)?.laneLabel||'Project work';}
const api={today,overdue,tasksFor,included,progress,requirements,next,nextByTrack,gateDone,health,lane};if(typeof module!=='undefined')module.exports=api;else root.Rules=api;
})(globalThis);
