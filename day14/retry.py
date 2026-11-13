import time

calls = {"n": 0 }


def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ConnectionError("simulated failure")
    return "ok"


def retry(func, tries=4):
    for attempt in range(tries):
        try:
            return func()
        except RuntimeError:
            print(f"Attempt {attempt + 1} failed, waiting {2 ** attempt}s")
            time.sleep(2 ** attempt)
        raise RuntimeError("gave up")


print(retry(flaky))