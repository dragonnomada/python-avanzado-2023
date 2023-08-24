from c1_tareas_seriadas import download, write_content

content = download('https://raw.githubusercontent.com/dragonnomada/python-avanzado-2023/main/datasets/report1_spotify.csv')
write_content("spotify.csv", content)

