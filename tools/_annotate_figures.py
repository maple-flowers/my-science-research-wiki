import os, re, io, sys, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
PAP = os.path.join(BASE, "wiki", "papers")
m = json.load(open(os.path.join(BASE, "tools", "_img2page.json"), encoding="utf-8"))
img2page = m["img2page"]
short = {slug: re.split(r"[（(]", title)[0].strip() for slug, title in m["pages"].items()}

RULES = [
    ("mathematical-models", ["公式", "式1", "式2", "式3", "式4", "式5", "式6", "式7",
     "式8", "式9", "eq_", "equation", "色散关系", "哈密顿", "矩阵元", "波函数",
     "微分", "积分", "回归方程", "拟合公式", "标度律", "scaling law", "关系式",
     "费曼图", "微扰", "自能", "理论预测", "体素尺寸", "方差分析",
     "eq.", "电子密度函数", "对势", "势参数",
     "势垒", "能垒", "cineb", "neb", "eform", "形成能", "应变张量", "应变矩阵",
     "方程", "llg", "thiele", "拓扑荷", "能量曲线", "能量-温度", "能量随",
     "双势阱", "势能", "公切线", "自相关", "lifshitz", "onsager", "螺旋诱导",
     "状态方程", "均方位移", "扩散系数", "原子化能", "h函数", "fx",
     "相对能量", "关键参数", "磁学参数表", "bader", "截面", "本底",
     "标度", "轻子", "解析模型", "随直径", "基准测试", "eq4", "eq5", "eq6",
     "eq7", "eq10", "eq13", "eq14", "eq16", "eq17", "eq18", "eq19",
     "eq20", "eq21", "eq23", "eq25", "eq26", "eq27",
     "孤子", "概率演化", "局域激发", "钉扎", "力常数", "tab_",
     "色散", "随温度", "斜率", "重整化", "初始激发", "模式"]),
    ("vibrational-spectra", ["拉曼", "声子", "红外", "raman", "phonon", "ir光谱",
     "振动模", "振动能", "红外吸收", "拉曼散射", "声子色散", "声子谱",
     "电磁振子", "振子"]),
    ("optical-spectra", ["吸收光谱", "透射率", "反射率", "折射率", "消光系数", "tauc",
     "光学带隙", "光学电导", "光致发光", "荧光", "pl光谱", "pl谱", "透射光谱",
     "反射光谱", "吸收谱", "光吸收", "椭偏", "介电函数", "光学常数", "偏振",
     "二色性", "圆二色性", "非线性吸收", "z扫描", "z-scan", "远场", "傅里叶频谱",
     "双光子", "非线性", "光束", "传播不变性", "吸光度", "峰值波长",
     "介电", "conductivity spectra", "permeability spectra", "mg光束",
     "shg", "二次谐波", "体光伏", "nlo"]),
    ("crystal-structures", ["晶体结构", "晶格", "顶视", "侧视", "原胞", "超胞",
     "空间群", "构型", "原子结构", "晶胞", "结构示意", "晶体图", "晶格常数",
     "键长", "原子位置", "结构演化", "相图", "晶体相", "结构相变", "多型",
     "堆垛", "层间距", "原子位移", "结构参数", "各向异性因子", "对称性破缺",
     "对称破缺", "中心对称", "几何参数", "晶格参数", "mülliken", "布居",
     "几何参数表", "structural parameters", "键角", "优化结构", "分子结构",
     "电荷分布", "平板模型", "slab", "晶粒", "组织演化", "铁素体", "形核",
     "zener", "重构表面", "二聚体", "吸附能", "能量景观", "直径差", "面积比",
     "原子堆积", "熔化温度", "eam", "ca网格", "pdf", "对分布",
     "岩盐", "钙钛矿", "八面体", "mxene", "纳米卷轴", "液态", "过冷"]),
    ("electronic-bands", ["能带", "dos", "态密度", "费米面", "费米能", "pdos",
     "瓦尼尔", "紧束缚", "arpes", "能带结构", "电子结构", "投影态密度",
     "费米嵌套", "嵌套矢量", "费米速度", "布里渊区", "费米口袋", "波矢",
     "dmft", "电阻率", "输运", "超导", "超流", "能隙", "穿透深度",
     "kagome", "鞍点", "范霍夫", "能级", "k网格", "k点", "采样",
     "电子性质", "能量与电子", "pband", "投影能带", "分波", "散射性质",
     "收敛性", "平面波收敛", "电荷密度差", "差分电荷密度", "塞贝克",
     "带隙", "收敛", "电荷密度分布", "临界场", "uemura"]),
    ("domain-walls", ["畴壁", "铁弹畴", "domain wall", "71°", "109°", "180°畴",
     "畴结构", "铁弹", "畴变", "畴反转", "成核", "翻转过程",
     "switching process", "电学翻转", "kittel", "畴密度"]),
    ("electronic-devices", ["器件", "晶体管", "存储", "记忆", "突触", "fet",
     "电容", "存储器", "忆阻", "i-v", "p-e", "电滞回线", "输出特性",
     "转移特性", "开关比", "耐久性", "保持时间", "写入", "擦除",
     "阻变", "电阻切换", "隧道结", "dielectric parameters",
     "逻辑运算", "图像处理", "神经网络", "时间线", "挑战与展望",
     "pcm", "mtj"]),
    ("heterostructures-stacking-moire", ["莫尔", "扭转角", "摩尔", "moire",
     "超晶格", "扭角", "层间转角", "莫尔波长"]),
    ("heterostructures-stacking-multiferroic", ["多铁", "磁电", "铁磁", "反铁磁",
     "磁序", "磁矩", "磁结构", "自旋纹理", "斯格明子", "磁化", "磁化强度",
     "交换耦合", "磁各向异性", "磁畴", "自旋螺旋", "自旋极化", "磁传播",
     "m-h", "磁滞", "m-h loops", "螺旋自旋", "jahn-teller",
     "螺旋态", "键偶极", "非本征铁电", "磁荷", "dmi", "二维磁性"]),
    ("heterostructures-stacking-polar-cdw", ["cdw", "电荷密度波", "极性金属",
     "拓扑相", "peierls", "嵌套", "电荷序", "轨道序", "mott",
     "金属-绝缘体相变", "能隙打开", "渗流", "percolation"]),
    ("heterostructures-stacking-sliding", ["滑移铁电", "层间滑移", "sliding",
     "滑移极化", "层间滑移铁电", "滑移路径", "滑移操作", "垂直极化"]),
    ("heterostructures-stacking-spintronics-strain", ["自旋电子", "应变工程",
     "自旋轨道", "自旋流", "自旋阀", "应变调控", "压应变", "张应变",
     "双轴应变", "面内应变", "应变效应", "自旋输运", "自旋注入",
     "自旋阀", "datta-das", "压阻", "压电", "电注入"]),
    ("heterostructures-stacking-mechanics-misc", ["力学", "剥离能", "弹性模量",
     "应力", "硬度", "柔性", "面内刚度", "泊松比", "杨氏模量",
     "液相剥离", "离子插层", "超声", "exfoliation"]),
    ("experimental-setups", ["装置", "系统框图", "示意图", "测量系统", "实验装置",
     "光路", "电路", "测试系统", "框图", "sem", "表征", "tem", "afm", "pfm",
     "xrd", "xps", "制备", "工艺", "样品", "测量装置", "测试装置",
     "电压-湿度", "湿度-电压", "响应曲线", "校准曲线", "标定曲线",
     "灵敏度", "重复性", "稳定性", "迟滞", "滞后", "中子衍射", "精修",
     "epr", "esr", "光谱仪", "显微镜", "显微", "doe", "cgh", "衍射光学",
     "光刻", "激光直写", "沉积", "溅射", "退火", "对比", "5点对比",
     "峰电位", "循环伏安", "tpp", "体素", "rda", "传感器",
     "光-湿", "暗态", "数据", "核心曲线", "核心数据", "实测",
     "设计", "原理", "机制", "过程", "示意", "校准矩阵", "检测信号",
     "归一化", "演化曲线", "冷速", "ca邻居", "离散化",
     "stm", "衍射", "磁光成像"]),
    ("heterostructures-stacking-reviews", ["综述", "汇总", "对比表", "总结表",
     "材料体系汇总", "性能对比", "清单", "铁电体分类", "二维铁电材料"]),
]

def classify(alt):
    low = alt.lower()
    for slug, keywords in RULES:
        for kw in keywords:
            if kw.lower() in low:
                return slug
    return None

# Match individual image embeds (not whole lines)
embed_re = re.compile(r'!\[([^\]]*)\]\((\.\./\.\./raw/figures/[^)]+/([^)/]+\.png))\)')

stats = {"files": 0, "linked": 0, "already": 0, "unclassified": 0}
unclassified_samples = []

for fn in sorted(os.listdir(PAP)):
    if not fn.endswith(".md"):
        continue
    p = os.path.join(PAP, fn)
    txt = open(p, encoding="utf-8").read()
    # find all embeds, process from end to start to preserve offsets
    matches = list(embed_re.finditer(txt))
    if not matches:
        continue
    new_txt = txt
    changed = False
    for mm in reversed(matches):
        alt = mm.group(1)
        path = mm.group(2)
        img = mm.group(3)
        end = mm.end()
        # check if already annotated within next 60 chars
        tail = new_txt[end:end+60]
        if "[[../figures/" in tail:
            stats["already"] += 1
            continue
        # classify
        slug = img2page.get(img) or classify(alt)
        if not slug:
            stats["unclassified"] += 1
            if len(unclassified_samples) < 25:
                unclassified_samples.append((fn[:-3], alt[:70]))
            continue
        link = " -> [[../figures/" + slug + "|" + short.get(slug, slug) + "]]"
        new_txt = new_txt[:end] + link + new_txt[end:]
        changed = True
        stats["linked"] += 1
    if changed:
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_txt)
        stats["files"] += 1

print(json.dumps(stats, ensure_ascii=False, indent=1))
if unclassified_samples:
    print("\n=== unclassified samples ===")
    for ck, alt in unclassified_samples:
        print(f"  {ck:30s} {alt}")
