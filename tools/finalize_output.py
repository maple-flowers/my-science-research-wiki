import json

with open('final_metadata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Use StructuredOutput-like print (not really needed if we just call the tool)
# But I need to provide the content to the tool call.
# I will just keep the list of papers in memory and call the tool.
print(f"Total papers: {len(data)}")
