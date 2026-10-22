from pathlib import Path
p=Path('App.jsx')
s=p.read_text(encoding='utf-8')
anchor='const timeChoices='
if anchor not in s:
    raise SystemExit('Could not find timeChoices anchor in App.jsx')
# Add choice-specific disruption copy and revised outcome rationale before timeChoices.
insert="""const disruption={
'CONTINUOUS MONITORING':{headline:'The monitoring model changed.',detail:'Dedicated devices gave way to distributed sensing and predictive workflows. Signal locations, data pathways and response patterns are different.'},
'VIRTUAL CARE':{headline:'The virtual-care platform was replaced.',detail:'The new model uses different devices, connection points and distributed-care workflows.'},
'INTELLIGENT COMMUNICATION':{headline:'The communication model shifted.',detail:'Role-based routing replaced several opening-day channels. Interfaces, directories and escalation paths now work differently.'},
'ADAPTABLE CARE':{headline:'The care model evolved.',detail:'Rooms now support different team configurations, equipment and workflows than the opening-day model anticipated.'},
'AUTOMATED SUPPORT':{headline:'The automation model changed.',detail:'New equipment has different charging, circulation, staging and interface requirements.'},
'LEARNING ENVIRONMENT':{headline:'The learning model expanded.',detail:'New analytics depend on different source data, definitions and feedback loops than the opening-day approach.'}
};
function assess2040(items,layers){
 const hardLocks=items.filter(([n,c])=>c==='COMMIT NOW'&&layers[n]==='CURRENT SOLUTION');
 const foundations=items.filter(([n,c])=>c==='COMMIT NOW'&&layers[n]==='DURABLE FOUNDATION');
 const flexible=items.filter(([,c])=>c==='ENABLE FOR LATER'||c==='EXPECT TO CHANGE'||c===\"DON'T LOCK IN\");
 if(hardLocks.length)return{posture:'BREAKS',hardLocks,foundations,flexible,why:`${hardLocks.map(x=>x[0]).join(' and ')} tied the building to an opening-day solution. Adapting now requires material redesign, disruption or workaround.`};
 if(foundations.length&&flexible.length>=1)return{posture:'BENDS',hardLocks,foundations,flexible,why:'Durable enabling conditions were protected while short-life components were allowed to change. The future can be accommodated without remaking the building.'};
 return{posture:'STRAINS',hardLocks,foundations,flexible,why:foundations.length?'The design protected a durable condition, but too many future assumptions remain unresolved. Adaptation is possible with added cost, disruption or compromise.':'The portfolio preserved flexibility but did not secure a durable physical foundation. The future remains possible, but additional intervention is required.'};
}
"""
if 'const disruption={' not in s:
    s=s.replace(anchor,insert+anchor,1)
start=s.index('if(step===6){')
# Final screen starts with the items declaration after step 6 block.
end=s.index('const items=names.map',start)
replacement="""if(step===6){
 const items=names.map(n=>[n,clock[n]]);
 const r=assess2040(items,layers);
 const stressName=(r.hardLocks[0]||items[0])?.[0];
 const event=disruption[stressName];
 return <Shell>
  <div className=\"resultHead\"><div><div className=\"eyebrow coral\">2040 UPDATE • CONSEQUENCE TEST</div><h2>{event.headline}</h2><p>{event.detail}</p><p><b>Can the design accommodate the change?</b></p></div><div className={'posture '+r.posture.toLowerCase()}><small>YOUR DESIGN</small><strong>{r.posture}</strong></div></div>
  <div className=\"resultCards\">{items.map(([n,c])=><article key={n}><span>{c==='COMMIT NOW'?(layers[n]==='CURRENT SOLUTION'?'OPENING-DAY SOLUTION':'ENABLING CONDITIONS'):c==='ENABLE FOR LATER'?'PROVIDE CAPACITY':c==='EXPECT TO CHANGE'?'DESIGN FOR REPLACEMENT':'PRESERVE OPTIONALITY'}</span><h3>{n}</h3><div><b>2040 EFFECT</b><p>{c==='COMMIT NOW'&&layers[n]==='CURRENT SOLUTION'?'Changing the solution now reaches into the building, infrastructure or operating model.':c==='COMMIT NOW'?'The long-life conditions remain useful even though the technical answer changed.':c==='ENABLE FOR LATER'?'Reserved pathway, capacity and access support the change.':c==='EXPECT TO CHANGE'?'Replaceable devices, interfaces and platforms absorb the change.':'The future model can change without violating a fixed assumption.'}</p></div></article>)}</div>
  <div className=\"resultBottom\"><section className={'outcome '+r.posture.toLowerCase()}><small>WHAT THAT MEANS IN 2040</small><strong>{r.posture}</strong><div><h3>{r.why}</h3>{r.hardLocks.length>0&&<p><b>Hard lock:</b> {r.hardLocks.map(x=>x[0]).join(' • ')}</p>}</div></section><section className=\"aha\"><small>THE AHA</small><h3>Certainty is not the problem.</h3><p>The risk is giving an opening-day solution the same lifespan as the building.</p></section></div>
  <Nav label=\"Create the team takeaway\"/>
 </Shell>
}
"""
s=s[:start]+replacement+s[end:]
s=s.replace('BUILD 12.2','BUILD 12.3')
p.write_text(s,encoding='utf-8')
print('Updated App.jsx to Build 12.3')
