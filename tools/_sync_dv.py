import os, re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
BASE = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
PAP = os.path.join(BASE,"wiki","papers")
RAW = os.path.join(BASE,"raw","note")
DV=['领域基础知识','研究背景','作者的问题意识','主要研究对象','主要研究方法','研究意义','研究结论','对领域的贡献','未来研究方向提及','未来研究方向思考']

def extract_raw(ck):
    p=os.path.join(RAW,ck+".md")
    if not os.path.isfile(p): return None
    t=open(p,encoding="utf-8").read()
    vals={}
    for k in DV:
        # match  > key:: value  possibly spanning until next > key:: or >  blank marker
        m=re.search(r'(?:^|\n)>?\s*'+re.escape(k)+r'::?\s*(.*?)(?=\n>?\s*(?:'+'|'.join(re.escape(x) for x in DV)+r')::|\n> \s*\n|\n>\s*🚀|\Z)', t, re.DOTALL)
        if m:
            v=m.group(1).strip()
            v=re.sub(r'^>\s?','',v,flags=re.M)  # strip leading >
            v=' '.join(line.strip() for line in v.splitlines() if line.strip())
            v=v.strip()
            if v: vals[k]=v
    return vals

def get_wiki_field(fm,k):
    m=re.search(r'^'+k+r'::\s*>?-?\s*\n((?:[ \t]+.*\n?)*)',fm,re.M)
    if m: return m.group(1).strip()
    m=re.search(r'^'+k+r'::\s*(.*)$',fm,re.M)
    if m: return m.group(1).strip()
    return None  # missing

stats={"filled":0,"replaced":0,"no_raw":0,"already":0}
targets = sys.argv[1:] if len(sys.argv)>1 else None
for fn in sorted(os.listdir(PAP)):
    if not fn.endswith(".md"): continue
    ck=fn[:-3]
    if targets and ck not in targets: continue
    p=os.path.join(PAP,fn); t=open(p,encoding="utf-8").read()
    mm=re.match(r'^(---\n)(.*?)(\n---\n)',t,re.DOTALL)
    if not mm: continue
    fm=mm.group(2)
    raw=extract_raw(ck)
    if not raw:
        if targets: print("NO RAW",ck)
        stats["no_raw"]+=1; continue
    changed=False
    for k in DV:
        cur=get_wiki_field(fm,k)
        new=raw.get(k)
        if not new: continue
        # replace if empty/missing OR (forced mode when targets given)
        if cur is None:
            # insert field block near figures/materials end (before tags if present, else append)
            block=k+":: >-\n  "+new+"\n"
            if re.search(r'^tags:',fm,re.M):
                fm=re.sub(r'(\n)(tags:)',r'\1'+block+r'\2',fm,count=1,flags=re.M)
            else:
                fm=fm.rstrip("\n")+"\n"+block
            changed=True; stats["filled"]+=1
        elif not cur:
            block=k+":: >-\n  "+new
            fm=re.sub(r'^'+k+r'::\s*$',block,fm,flags=re.M)
            changed=True; stats["replaced"]+=1
    if changed:
        t=t[:mm.start(2)]+fm+t[mm.end(2):]
        open(p,"w",encoding="utf-8",newline="\n").write(t)
print(stats)
