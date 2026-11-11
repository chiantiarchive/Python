import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["API_KEY"]


def fetch_json(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The server took too long to answer.")
    except requests.exceptions.HTTPError as error:
        print(f"Server returned an error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Network problem: {error}")
    return None


users = fetch_json('https://jsonplaceholder.typicode.com/users')
if users:
    for user in users:
        print(user["name"], "-", user["email"])
    Path("users.json").write_text(json.dumps(users, indent=2), encoding="utf-8")
    print(f"Saved {len(users)} users")

fetch_json('https://this-site-does-not-exist-12345.com')      # bad URL
fetch_json('https://jsonplaceholder.typicode.com/posts/99999')  # 404

print('API key loaded:', len(api_key), 'characters')