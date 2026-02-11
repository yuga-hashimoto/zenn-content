import json
import re
import urllib.request
import urllib.error
import sys

# Define constants
TOKEN = "5d59888dbad85c008680b0bfffa44aa9d27a6ec3"
FILE_PATH = "/Users/yu-ga/zenn-content/articles/2026-02-10-ai-world-models.md"
API_URL = "https://qiita.com/api/v2/items"

# Read markdown content
try:
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

# Remove Zenn frontmatter
# The regex matches --- at start, content, then ---
cleaned_content = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)

# Prepare JSON payload
payload = {
    "body": cleaned_content,
    "coediting": False,
    "group_url_name": None,  # Can be omitted or None if not posting to an organization
    "private": False,
    "tags": [
        {"name": "AI"},
        {"name": "WorldModel"},
        {"name": "2026"},
        {"name": "TechTrend"},
        {"name": "YannLeCun"}
    ],
    "title": "2026年のAIトレンド転換点：Yann LeCunの新天地「ワールドモデル」とエージェントの実用化",
    "tweet": True
}

# Send request
try:
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    
    with urllib.request.urlopen(req) as response:
        if response.status == 201:
            res_json = json.loads(response.read().decode("utf-8"))
            print(f"Successfully posted to Qiita: {res_json.get('url')}")
        else:
            print(f"Failed to post. Status: {response.status}")
            print(response.read().decode("utf-8"))

except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code}")
    print(e.read().decode("utf-8"))
except Exception as e:
    print(f"Error: {e}")
