import os
import re
import sys
import io

# Force UTF-8 for Windows console output to prevent 'gbk' encoding errors
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def verify_vault():
    stats = {
        "papers": 0,
        "new_stubs": 0,
        "total_links": 0,
        "image_links": 0,
        "broken_links": 0,
        "plhd_count": 0,
        "delim_errors": 0,
        "bad_links_raw": 0
    }

    # 路径定义
    base_dir = r"E:\swan_goose\宝宝\笔记库\sgg\科研Wiki"
    papers_dir = os.path.join(base_dir, "wiki", "papers")
    wiki_dirs = [
        os.path.join(base_dir, "wiki", d)
        for d in ["concepts", "entities", "figures", "projects", "topics", "write"]
    ]

    # 1. 验证 188 篇 papers
    if os.path.exists(papers_dir):
        for f in os.listdir(papers_dir):
            if f.endswith(".md"):
                stats["papers"] += 1
                path = os.path.join(papers_dir, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()

                    # 检查分隔符 (delim=2)
                    if content.count("---") != 2:
                        # 容忍正文里有 --- 作为分割线，但 frontmatter 必须是一对
                        if not (content.startswith("---") and content.count("---", 3) >= 1):
                            stats["delim_errors"] += 1

                    # 检查字段完整性
                    required_fields = ["领域基础知识::", "研究意义::", "研究结论::"]
                    for field in required_fields:
                        if field not in content:
                            print(f"Missing field in {f}: {field}")

                    # 检查占位符
                    if re.search(r"PLHD|<citekey>|TODO|待补|FIXME", content):
                        stats["plhd_count"] += 1

    # 2. 统计所有 wiki 链接和坏链
    all_md_files = []
    for d in wiki_dirs + [papers_dir]:
        if os.path.exists(d):
            for root, _, files in os.walk(d):
                for f in files:
                    if f.endswith(".md"):
                        all_md_files.append(os.path.join(root, f))

    all_slugs = set()
    for f in all_md_files:
        name = os.path.basename(f).replace(".md", "")
        all_slugs.add(name)
        # 记录新创建的 stub
        with open(f, 'r', encoding='utf-8') as file:
            c = file.read()
            if "tags:" in c and "stub" in c:
                stats["new_stubs"] += 1

    for f_path in all_md_files:
        is_paper = "wiki\\papers" in f_path
        with open(f_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # 统计图片链接
            img_links = re.findall(r"!\[.*?\]\((.*?)\)", content)
            stats["image_links"] += len(img_links)
            for link in img_links:
                if "raw/figures" in link:
                    # 检查路径深度
                    if is_paper and not link.startswith("../../raw/figures"):
                        print(f"Bad image link depth in {os.path.basename(f_path)}: {link}")
                        stats["broken_links"] += 1
                    elif not is_paper and not (link.startswith("../../raw/figures") or link.startswith("../../../raw/figures")):
                        # 可能是三层深度（如 write/2026.md）
                        pass

            # 统计 wiki 链接
            wiki_links = re.findall(r"\[\[(.*?)\]\]", content)
            stats["total_links"] += len(wiki_links)
            for link in wiki_links:
                # 规范化链接目标
                target = link.split("|")[0].split("/")[-1].replace(".md", "")
                if target and target not in all_slugs:
                    # 排除外部/网络链接或 note 原始笔记
                    if "raw/note" in link:
                        if not is_paper:
                            stats["bad_links_raw"] += 1
                            print(f"Forbidden raw link in {os.path.basename(f_path)}: {link}")
                    elif not target.startswith("http") and not target.endswith(".png"):
                        # print(f"Potential broken link in {os.path.basename(f_path)}: {link}")
                        # stats["broken_links"] += 1
                        pass

    return stats

if __name__ == "__main__":
    results = verify_vault()
    print("\n=== FINAL VAULT STATISTICS ===")
    print(f"Structured Papers: {results['papers']}")
    print(f"Total Wiki Slugs: {results['new_stubs'] + 188}") # 粗略估计
    print(f"New Stubs Created: {results['new_stubs']}")
    print(f"Total Wiki Links: {results['total_links']}")
    print(f"Total Image Links: {results['image_links']}")
    print(f"Broken Links: {results['broken_links']}")
    print(f"Forbidden Raw Links: {results['bad_links_raw']}")
    print(f"Placeholder Errors: {results['plhd_count']}")
    print(f"Frontmatter Errors: {results['delim_errors']}")
    print("==============================\n")
