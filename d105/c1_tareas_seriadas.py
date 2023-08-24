def download(url):
    # python3 -m pip install requests
    import requests

    response = requests.get(url)

    content = None

    # HTTP STATUS (Estándar)
    if response.status_code == 200:
        content = response.content

    response.close()

    return content

def write_content(filename, content):
    f = open(filename, "wb")
    f.write(content)
    f.close()