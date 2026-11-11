import time, requests

all_post, page = [], 1
while True:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={"_page": page, "_limit": 10},
        timeout=10,
    )
    response.raise_for_status()
    batch = response.json()
    if not batch:
        break
    all_post.extend(batch)
    page += 1
    time.sleep(0.2)

print(len(all_post))
print(all_post[0]["id"], all_post[-1]["id"])
print(len({post["id"] for post in all_post}))