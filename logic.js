/* Pure scheduling and display rules, shared by UI and verification. */
(function(root){
const rank={critical:0,high:1,medium:2,low:3};
function today(){return new Intl.DateTimeFormat('en-CA',{timeZone:'America/Los_Angeles',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date())}
function tasksFor(d,p){return d.tasks.filter(t=>t.project===p)}
function included(ts){return ts.filter(t=>t.status!=='deferred')}
function progress(ts){ts=included(ts);const done=ts.filter(t=>t.status==='done').length;return {done,total:ts.length,percent:ts.length?Math.round(100*done/ts.length):0}}
function requirements(d,t){return [...t.dependencies.filter(id=>d.tasks.find(x=>x.id===id)?.status!=='done'),...t.decisionDependencies.filter(id=>d.decisions.find(x=>x.id===id)?.status!=='resolved')]}
function compare(a,b){return (rank[a.priority]??4)-(rank[b.priority]??4)||(a.targetDate||'9999').localeCompare(b.targetDate||'9999')||a.id.localeCompare(b.id)}
function next(d,p,date=today()){
 const ts=included(tasksFor(d,p)).filter(t=>t.status!=='done');
 if(!ts.length)return {kind:'complete',reason:'All included work is complete.'};
 const ready=ts.filter(t=>!requirements(d,t).length&&t.status!=='blocked'&&!t.conditional&&(t.status==='ready'||t.status==='doing')&&(!t.startDate||t.startDate<=date));
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
 return {kind:'waiting',reason:'No executable task. Review unresolved prerequisites, backlog, or conditional work.'};
}
function gateDone(d,g){return g.taskIds.every(id=>d.tasks.some(t=>t.id===id&&t.status==='done'&&t.evidence.trim()))}
function health(d,p,date=today()){
 const ts=included(tasksFor(d,p)),gs=d.gates.filter(g=>g.project===p);
 if(gs.length&&gs.every(g=>gateDone(d,g)))return {label:'Complete',reason:'All release gates have verified evidence.'};
 const blocked=ts.find(t=>(t.critical||t.releaseGate)&&t.status==='blocked');
 if(blocked)return {label:'Blocked',reason:blocked.id+': '+blocked.blockerReason};
 const decision=d.decisions.find(x=>x.project===p&&x.status==='open'&&x.dueDate<=date&&x.blocks.some(id=>ts.some(t=>t.id===id&&t.status!=='done'&&(!t.startDate||t.startDate<=date)&&(t.critical||t.releaseGate))));
 if(decision)return {label:'Blocked',reason:decision.id+': '+decision.title};
 const late=ts.find(t=>t.critical&&t.status!=='done'&&t.targetDate&&t.targetDate<date);
 if(late)return {label:'At Risk',reason:late.id+' is overdue.'};
 const milestone=d.milestones.find(m=>m.project===p&&m.targetDate<date&&ts.some(t=>t.milestone===m.id&&t.status!=='done'));
 if(milestone)return {label:'At Risk',reason:milestone.name+' milestone is overdue.'};
 if(d.projects.find(x=>x.id===p).deadline<date)return {label:'At Risk',reason:'Release date has passed with gates still open.'};
 return {label:'On Track',reason:'No recorded critical blocker or overdue milestone; this is a rule-based status, not a forecast.'};
}
function lane(d,p,date=today()){if(date<=d.sequencing.weekendEnd)return p==='AT'?'Primary · Kiro + demo foundation':'Bounded Kiro evaluation';return p==='LW'?'Secondary · '+(date<d.sequencing.switchDate?'discovery':'implementation'):p==='AT'?(date<d.sequencing.switchDate?'Primary · executive demo':'Demo follow-through'):(date<d.sequencing.switchDate?'Foundation only':'Primary · design-partner release')}
const api={today,tasksFor,included,progress,requirements,next,gateDone,health,lane};if(typeof module!=='undefined')module.exports=api;else root.Rules=api;
})(globalThis);
