import json
import urllib.request
import urllib.error
import re

# Read the markdown file
with open('/Users/yu-ga/zenn-content/articles/ai-wars-feb-2026-claude-gemini.md', 'r') as f:
    content = f.read()

# Remove frontmatter (between --- and ---)
content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

# Prepare payload
data = {
    "body": content,
    "coediting": False,
    "private": False,
    "tags": [
        {"name": "AI"},
        {"name": "Claude"},
        {"name": "Gemini"},
        {"name": "OpenAI"},
        {"name": "TechTrends"}
    ],
    "title": "2026年2月「AI頂上決戦」勃発！Claude 4.6 Opus vs Gemini 3 Flash vs GPT-5.3",
    "tweet": True
}

# Convert data to JSON bytes
json_data = json.dumps(data).encode('utf-8')

# Headers
headers = {
    "Authorization": "Bearer 5d59888dbad85c008680b0bfffa44aa9d27a6ec3",
    "Content-Type": "application/json"
}

# Request
req = urllib.request.Request(
    "https://qiita.com/api/v2/items",
    data=json_data,
    headers=headers,
    method="POST"
)

try:
    with urllib.request.urlopen(req) as response:
        if response.status == 201:
            res_json = json.load(response)
            print(f"Success: {res_json['url']}")
        else:
            print(f"Error: {response.status}")
            print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"Error: {e.code}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
