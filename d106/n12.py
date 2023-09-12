from concurrent.futures import ProcessPoolExecutor

def download_user_picture(id):
    import requests
    response_user = requests.get(f"https://randomuser.me/api?seed={id}")
    data = response_user.json()
    results = data["results"]
    user = results[0]
    pictureURL = user["picture"]["large"]
    response_picture = requests.get(pictureURL)
    picture_content = response_picture.content
    filename = f"output/{id}.png"
    with open(filename, "wb") as file:
        file.write(picture_content)
    return filename

if __name__ == "__main__":
    executor1 = ProcessPoolExecutor(max_workers=4)

    inputs = [123, 456, 789, 111, 222, 333]

    # Peticiones bajo demanda (on-demand | hot-spot)
    futures = [ executor1.submit(download_user_picture, id) for id in inputs ]

    from concurrent.futures import wait

    wait(futures)

    outputs = [ future.result() for future in futures ]

    print(outputs)