import multiprocessing

# threading -> process
class DownloadUserPictureProcess (multiprocessing.Process):

    id = None

    def __init__(self, id):
        super().__init__()

        self.id = id # Inicializamos la propiedad `self.id` 
                     # con el parámetro de construcción `id`

    def run(self):
        import requests
        response_user = requests.get(f"https://randomuser.me/api?seed={self.id}")
        data = response_user.json()
        results = data["results"]
        user = results[0]
        pictureURL = user["picture"]["large"]
        response_picture = requests.get(pictureURL)
        picture_content = response_picture.content
        with open(f"output/{self.id}.png", "wb") as file:
            file.write(picture_content)

if __name__ == "__main__":
    process1 = DownloadUserPictureProcess(123)
    process2 = DownloadUserPictureProcess(456)
    process3 = DownloadUserPictureProcess(789)
    process4 = DownloadUserPictureProcess(111)
    process5 = DownloadUserPictureProcess(222) # Error (se superó el número de núcleos)
    process6 = DownloadUserPictureProcess(333) # Error (se superó el número de núcleos)

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()