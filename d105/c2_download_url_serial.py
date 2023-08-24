# Librería Regex -> Identificar patrones regulares
import re

from c1_tareas_seriadas import download, write_content

with open("urls.txt", "r") as f: # f - nombre del archivo
    for url in f.readlines()[:5]: # line-by-line
        url = url.strip()
        filename = re.search("denue[\w\_\-]+_csv.zip", url).group(0)
        print(url, filename)

        # TAREA 1 - DESCARGAR
        content = download(url)
        # TAREA 2 - ESCRIBIR
        write_content("output/" + filename, content)



