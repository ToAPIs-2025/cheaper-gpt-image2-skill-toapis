"""Run the patched upstream CLI; four image cases, dry-run unless --live."""
from pathlib import Path
import argparse,subprocess,os,json,re,hashlib,time,urllib.request
from decimal import Decimal
from PIL import Image
SHASOURCE='9f8aa1a44a4a5c0f5a5d6e45eed564b3e2d5b87f'
def main():
    p=argparse.ArgumentParser();p.add_argument('--upstream',type=Path,required=True);p.add_argument('--key-file');p.add_argument('--output',type=Path,default=Path('results'));p.add_argument('--live',action='store_true');p.add_argument('--case',default='all');a=p.parse_args()
    cases=json.loads((Path(__file__).parent/'cases/briefs.json').read_text(encoding='utf-8'));cases=[c for c in cases if a.case=='all' or c['id']==a.case]
    if not cases:raise SystemExit('Unknown case')
    env=os.environ.copy();env.update({'PYTHONPATH':str(a.upstream.resolve()/'src')+os.pathsep+env.get('PYTHONPATH',''),'PYTHONIOENCODING':'utf-8','TOAPIS_BASE_URL':'https://toapis.cn','TOAPIS_STATE_DIR':str(a.output.resolve()/'private-state')})
    if a.live:
        os.sys.path.insert(0,str(a.upstream.resolve()/'src'))
        if a.key_file:
            for line in Path(a.key_file).read_text(encoding='utf-8-sig').splitlines():
                if '=' in line and not line.lstrip().startswith('#'):
                    k,v=line.split('=',1);env[k.strip()]=v.strip().strip('\"\x27')
        key=env.get('TOAPIS_API_KEY');assert key,'Configure TOAPIS_API_KEY privately'
        from gpt_image_cli.toapis import normalize_origin,NoRedirect
        origin=normalize_origin(env.get('TOAPIS_BASE_URL','https://toapis.cn'));http=urllib.request.build_opener(NoRedirect)
        quotes={}
        for model in sorted(set(c['model'] for c in cases)):
            with http.open(urllib.request.Request(origin+'/v1/pricing?model='+model,headers={'Authorization':'Bearer '+key}),timeout=30) as r:quotes[model]=json.load(r)
        estimate=Decimal('0')
        for case in cases:
            prices=[x for m in quotes[case['model']].get('data',[]) for x in m.get('prices',[]) if x.get('unit')=='request' and x.get('conditions',{}).get('resolution')=='1K' and x.get('conditions',{}).get('n',1)==1 and (case['model']=='gpt-image-2' or x.get('conditions',{}).get('quality')=='low')]
            if not prices:raise SystemExit('No exact applicable catalog rate; stop before submission')
            case['quote_usd']=str(max(Decimal(x['unit_price']) for x in prices));estimate+=Decimal(case['quote_usd'])
        if estimate>Decimal('0.10'):raise SystemExit('Four-image demonstration exceeds its $0.10 sub-cap; no submission')
        a.output.mkdir(parents=True,exist_ok=True);(a.output/'pricing.json').write_text(json.dumps({'date':'2026-10-13','quotes':quotes,'estimated_usd':str(estimate)},ensure_ascii=False,indent=2),encoding='utf-8')
    records=[]
    for case in cases:
        folder=a.output/case['id'];output=folder/'result.png';cmd=[os.sys.executable,'-m','gpt_image_cli.cli','--provider','toapis','--model',case['model'],'--quality','low','--resolution','1K','--size','square','-p',case['prompt'],'-f',str(output.resolve())]
        if case.get('reference'):cmd+=['-i',str((a.output/case['reference']).resolve())]
        env['TOAPIS_RUN_ID']=case['id']
        if not a.live:
            cmd+=['--dry-run'];run=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8');assert run.returncode==0,run.stderr;print(run.stdout.strip());continue
        if (folder/'evidence.json').exists():records.append(json.loads((folder/'evidence.json').read_text(encoding='utf-8')));continue
        start=time.monotonic();run=subprocess.run(cmd,env=env,capture_output=True,text=True,encoding='utf-8');folder.mkdir(parents=True,exist_ok=True)
        log=run.stdout+'\n'+run.stderr;assert key not in log;(folder/'cli-log.txt').write_text(log,encoding='utf-8')
        if run.returncode:raise SystemExit('CLI failed; keep private-state and task ID. '+run.stderr[:600])
        task_match=re.search(r'"task_id":\s*"([^"]+)"',run.stderr)
        # A completed receipt can be reused without a new submitted event.
        receipts=[json.loads(f.read_text(encoding='utf-8')) for f in (a.output/'private-state').glob('*.json')]
        receipt=next(x for x in receipts if x['request']['prompt']==case['prompt'] and x['request']['model']==case['model'])
        e={'case':case,'upstream_repo':'wuyoscar/GPT-Image2-Skill','upstream_sha':SHASOURCE,'date':'2026-10-13','task_id':receipt['task_id'],'status':receipt['state'],'request':receipt['request'],'observations':receipt['observations'],'billing':receipt.get('billing'),'actual_cost_usd':(receipt.get('billing') or {}).get('cost_usd'),'quote_usd':case['quote_usd'],'pixels':list(Image.open(output).size),'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'elapsed_seconds':round(time.monotonic()-start,2),'entrypoint':'real upstream cli.main -> call_generate/call_edit -> ToAPIsClient -> original write_outputs','scope':'CLI only; no agent runtime, UI, video or masks tested'}
        e['resumed_existing_task']=task_match is None
        e['elapsed_scope']='resume query/download/write only; original generation latency unavailable' if task_match is None else 'single observed CLI call including polling and download; not a benchmark'
        (folder/'evidence.json').write_text(json.dumps(e,ensure_ascii=False,indent=2),encoding='utf-8');records.append(e);print(json.dumps({'case':case['id'],'task':e['task_id'],'pixels':e['pixels'],'billing':e['billing'],'elapsed':e['elapsed_seconds']}),flush=True)
    if a.live:(a.output/'runs.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':main()
