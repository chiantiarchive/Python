import time
import requests

RETRY_STATUS = {429, 500, 502, 503, 504}


def get_with_retry(url, params=None, headers=None, tries=4):
    for attempt in range(tries):
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
        except requests.exceptions.RequestException as error:
            print(f"Attempt {attempt + 1} failed: {error}")
        else:
            if response.status_code not in RETRY_STATUS:
                response.raise_for_status()
                return response.json()
            print(f"Attempt {attempt + 1}: status {response.status_code}, retrying")
        if attempt < tries - 1:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"Gave up after {tries} tries: {url}")


def fetch_all_post():
    posts, page = [], 1
    while True:
        batch = get_with_retry(
            "https://jsonplaceholder.typicode.com/posts",
            params={"_page": page, "_limit": 10},
        )
        if not batch:
            return posts
        posts.extend(batch)
        page += 1
        time.sleep(0.2)


if __name__ == "__main__":
    print(len(fetch_all_post()))

    try:
        get_with_retry('https://this-site-does-not-exist-12345.com', tries=3)
    except RuntimeError as error:
        print("Final result:", error)