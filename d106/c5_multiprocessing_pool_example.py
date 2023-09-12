import multiprocessing

def get_user_info(id):
    import requests
    response = requests.get(f"https://randomuser.me/api?seed={id}")
    data = response.json()
    results = data["results"]
    user = results[0]
    return {
        "fullname": user["name"]["first"] + " " + user["name"]["last"],
        "email": user["email"],
        "pictureURL": user["picture"]["large"],
    }

# bootstrap
if __name__ == "__main__":
    # SYNC
    # print(get_user_info(123))
    # print(get_user_info(456))
    # print(get_user_info(789))

    # ASYNC
    pool1 = multiprocessing.Pool(processes=4)

    print("Ejecutándo...")
    
    # === MODE SYNC ===
    # users_info = pool1.map(get_user_info, [123, 456, 789])
    # ============

    users_info_async = pool1.map_async(get_user_info, [123, 456, 789])

    # === MODE ASYNC ===
    print("Esperando...")

    users_info = users_info_async.get() # ~ .join() | SYNCRONIZED

    print("Finalizado...")
    # ==================

    print(users_info)