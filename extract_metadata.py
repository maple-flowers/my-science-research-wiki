import os
import re
import json

directory = r'E:\swan_goose\宝宝\笔记库\sgg\科研Wiki\raw\note'
results = []

# Refined regex patterns
# Stops at the next field (word::) or end of line
patterns = {
    'citekey': re.compile(r'qnkey::\s*(.*?)(?=\s*\w+::|$)'),
    'title': re.compile(r'title::\s*(.*?)(?=\s*\w+::|$)'),
    'year': re.compile(r'dateY::\s*(.*?)(?=\s*\w+::|$)'),
    'materials': re.compile(r'主要研究对象::\s*(.*?)(?=\s*\w+::|$)'),
    'methods': re.compile(r'主要研究方法::\s*(.*?)(?=\s*\w+::|$)')
}

def clean_value(val):
    if not val:
        return ""
    # Remove markdown formatting like [[...]]
    val = re.sub(r'\[\[(.*?)\]\]', r'\1', val)
    # Remove HTML tags
    val = re.sub(r'<.*?>', '', val)
    return val.strip()

def parse_list(val):
    cleaned = clean_value(val)
    if not cleaned:
        return []
    # Split by common separators: 、 , ; or spaces if they separate links
    # But for these specific fields, they are often descriptive sentences.
    # If there are '、', split by them.
    if '、' in cleaned:
        parts = re.split(r'、', cleaned)
    else:
        parts = [cleaned]
    return [p.strip() for p in parts if p.strip()]

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
                data = {
                    'citekey': '',
                    'title': '',
                    'year': '',
                    'materials': [],
                    'methods': []
                }
                
                for key, pattern in patterns.items():
                    match = pattern.search(content)
                    if match:
                        val = match.group(1).strip()
                        if key in ['materials', 'methods']:
                            data[key] = parse_list(val)
                        else:
                            data[key] = clean_value(val)
                
                if not data['citekey']:
                    data['citekey'] = os.path.splitext(filename)[0]
                
                if not data['title']:
                    title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
                    if title_match:
                        data['title'] = clean_value(title_match.group(1))
                    else:
                        data['title'] = data['citekey']

                results.append(data)
        except:
            pass

with open('final_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False)
