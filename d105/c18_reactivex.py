#
# ReactiveX es una metodología/patrón de diseño basado en flujos, observadores y operadores
#
# Flujos: Son "streams" de información como flujos de datos que provengan desede un archivo,
#         un socket, una base de datos, una petición web, variables, entre otras fuentes.
#
# Observadores: Son objetos capaces de observar el flujo y atender a los suscriptores.
#
# Operadores: Son funciones que sintetizan, transforman, agrupan, concatenan o alteran los flujos.
#
#

# Instalación: v2.x | python3 -m pip install rx==1.6.1
#              v3.x | python3 -m pip install rx
#              v4.x | python3 -m pip install reactivex

# Instalación: v2.x | import rx
#              v3.x | import rx
#              v4.x | import reactivex

from reactivex import of

source1 = of("Manzana", "Mango", "Pera", "Kiwi") # source1 ~> FLUJO/FLOW/STREAM/OBSERVABLE

# Un suscriptor es una función que recibe cada elemento en el flujo, cuando este lo determina
# es decir, cada que el flujo adquiere un nuevo elemento, este es propagado a los suscriptores

subscriber101 = source1.subscribe(lambda fruta: print(f"fruta={fruta}"))

print("-" * 80)

def reporte_fruta(fruta):
    print(f"Nombre={fruta}") # f-string
    print("Caracteres={}".format(len(fruta))) # .format
    print("Inicial={}".format(fruta[0].upper())) # .format
    print("=" * 80)

subscriber102 = source1.subscribe(reporte_fruta)




