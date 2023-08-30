import asyncio

loop = asyncio.get_event_loop()

from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=3)

async def fetch_users_api(n):
    url = f"https://randomuser.me/api?results={n}"

    import requests

    response = await loop.run_in_executor(executor, requests.get, url)

    import json

    data = json.loads(response.text)

    return data["results"]

users = loop.run_until_complete(fetch_users_api(10))

print(users)

