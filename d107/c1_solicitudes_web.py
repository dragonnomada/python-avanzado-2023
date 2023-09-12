#
# Las solicitudes web son peticiones bajo el protocolo HTTP
# que se emiten a un servidor (considerandonos nosotros como los clientes)
# para formar una mecanica de comunicación llamada cliente-servidor
# en la modalidad petición-respuesta.
#
# La solicitud web se hace a través de una URL que codifica la petición
# y obtiene una respuesta bajo los siguientes mandos:
# 
# 1. Un CÓDIGO DE ESTATUS sobre la respuesta, este es está estandarizado
#    y acorde a los estándares de HTTP del w3.org dónde los estatus son:
#
#    10X. Representan infromación general al cliente
#    20X. Representan respuestas exitósas al cliente
#    30X. Representan solicitudes al cliente
#    40X. Representan errores provocados por el cliente
#    50X. Representan errores ocurridos en el servidor
# 
#    Consulta: https://developer.mozilla.org/es/docs/Web/HTTP/Status
#
#    Entre los más comunes son:
#    200 - OK (respuesta exitósa)
#    301 - Redirect/Move Permanently (redirecciona o otro sitio)
#    400 - Bad request (petición incorrecta o con errores)
#    401 - Unathorized (acceso denagado)
#    403 - Forbidden (acceso no permitido)
#    404 - Not found (el recurso no existe)
#    500 - Internal server error (ocurrió un error en el servidor)
#    501 - Not implemented (el servidor aún no dispone de una implementación para esos recursos)
#
# 2. Datos asociados a la respuesta:
#  
#    HEADERS - Representan claves y valores de cabecera como las cookies, 
#              la información del servidor, fechas, tipos de datos devueltos, etc.
#              con meta-información de la respuesta (variable).
#    TEXTO - El contenido de texto directo cuándo el `HEADER content-type=text/plain`
#            o alguno similar como `text/html`, `text/css`, `text/...`
#
#    JSON - El contenido en formato JSON cuándo el `HEADER content-type=application/json`
#
#    XML - El contenido en formato XML cuándo el `HEADER content-type=application/xml`
#
#    BINARY CONTENT - El contenido binario cuándo el `HEADER content-type=application/octect-stream`,
#                     o `application/binary`, `application/ascii`, `application/pdf`, `image/png`, `image/jpeg`,
#                     `image/...`, `audio/...`, `video/...`
#
#   Todos estos son conocidos como los MIME-TYPES.
#
#   Consulta: https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
#

# python3 -m pip install requests
import requests

# url = "https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types"
url = "https://randomuser.me/api/portraits/women/37.jpg"

response = requests.get(url)

print(response.ok) # bool
print(response.status_code) # int
print("-" * 80)
print(response.headers) # dict
print("-" * 80)
print(response.headers["Content-Type"]) # dict
print(response.headers["Content-Length"]) # dict
print(response.headers["Date"]) # dict
print("-" * 80)
print(response.text[:20]) # str
print(response.content[:20]) # binary-str