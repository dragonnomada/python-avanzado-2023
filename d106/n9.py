async def task_part1(id):
    # await axios.get(...)
    # await sockeio.once(...)
    import requests
    response = requests.get(f"https://randomuser.me/api?seed={id}")
    data = response.json()
    results = data["results"]
    user = results[0]
    return user

async def task_part2(user):
    pictureURL = user["picture"]["large"]
    import requests
    response = requests.get(pictureURL)
    content = response.content
    return content

async def task_part3(filename, content):
    with open(filename, "wb") as file:
        file.write(content)

async def task_async(id):
    user = await task_part1(id)
    picture_content = await task_part2(user)
    await task_part3(f"output/{id}.png", picture_content)

def main():
    import asyncio

    loop1 = asyncio.get_event_loop()

    loop1.run_until_complete(task_async(123))
    loop1.run_until_complete(task_async(456))
    loop1.run_until_complete(task_async(789))

if __name__ == "__main__":
    main()