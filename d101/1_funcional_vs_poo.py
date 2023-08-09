#
# Paradigma Funcional
# Resuelve problemas a través de tareas
#

def reportar_estadisticos(x):
    # GENERA ESTADÍSTICOS
    total_x = len(x)
    suma_x = sum(x)
    min_x = min(x)
    max_x = max(x)
    prom_x = suma_x / total_x
    var_x = sum([(xi - prom_x) ** 2 for xi in x]) / total_x
    dst_x = var_x ** 0.5

    # CÓDIGO NO REUTILIZABLE DE ALTO MANTENIMIENTO
    # RECOLECTAR LOS ESTADÍSTICOS
    stats = {
        "total": total_x,
        "suma": suma_x,
        "min": min_x,
        "max": max_x,
        "prom": prom_x,
        "var": var_x,
        "dst": dst_x
    }

    # CÓDIGO ACOPLADO A OTRO CÓDIGO PREVIO (ES CONTEXTUAL)
    # GENERA EL REPORTE DE LOS ESTADÍSTICOS
    print(f"TOTAL: {total_x}")
    print(f"SUMA: {suma_x}")
    print(f"MIN/MAX: {min_x} / {max_x}")
    print(f"PROMEDIO: {prom_x}")
    print(f"DES. EST: {dst_x}")

reportar_estadisticos([1.8, 1.9, 1.6, 1.7, 1.8, 2.1, 2.3, 1.7, 1.85])

def calcular_estadisticos(x):
    total_x = len(x)
    suma_x = sum(x)
    min_x = min(x)
    max_x = max(x)
    prom_x = suma_x / total_x
    var_x = sum([(xi - prom_x) ** 2 for xi in x]) / total_x
    dst_x = var_x ** 0.5

    return (total_x, suma_x, min_x, max_x, prom_x, var_x, dst_x)

def recolectar_estadisticos(total, suma, mini, maxi, prom, var, dst):
    stats = {
        "total": total,
        "suma": suma,
        "min": mini,
        "max": maxi,
        "prom": prom,
        "var": var,
        "dst": dst
    }

    return stats

def imprimir_estadisticos(stats):
    print(f"TOTAL: {stats['total']}")
    print(f"SUMA: {stats['suma']}")
    print(f"MIN/MAX: {stats['min']} / {stats['max']}")
    print(f"PROMEDIO: {stats['prom']}")
    print(f"DES. EST: {stats['dst']}")

def aplicar_estadisticos(x):
    t, s, mi, ma, p, v, d = calcular_estadisticos(x)
    stats = recolectar_estadisticos(t, s, mi, ma, p, v, d)
    imprimir_estadisticos(stats)

#
# Paradigma Orientado a Objetos
# Resuelve problemas a través de agentes (objetos)
#

# 1. Diseñar una clase para un agente que resuelve una tarea específica
# 2. Retener el estado necesario (memoria) del agente
# 3. Aplicar las transacciones necesesarias (operaciones) del agente

# Diferencia entre función y método
# * Una función es libre de contexto (no tiene acceso a un estado compartido)
# * Un método es una función interna de una clase
# * Un método es depediente de un contexto (del contexto llamado self)
# * self es el estado interno del objeto (agente) 
#   y retiene todos los valores para los atributos

# CLASE/DISEÑO Estadistico
# Clase es como un servicio o un agente que resuelve
# diferentes tareas asociadas (una por cada método/operación/transacción)
# mateniendo un mismo estado/propiedades/variables-internas/contexto-self
class Estadistico:

    # CONTEXTO/ESTADO/PROPIEDADES/VARIABLES-INTERNAS
    total = 0
    suma = 0
    mini = 0
    maxi = 0
    prom = 0.
    var = 0.
    dst = 0.

    stats = {}

    # MÉTODO/OPERACIÓN/TRASACCIÓN

    # Operación para actualizar los estadísticos
    def actualizar(self, x):
        self.total = len(x)
        self.suma = sum(x)
        self.mini = min(x)
        self.maxi = max(x)
        self.prom = self.suma / self.total
        self.var = sum([(xi - self.prom) ** 2 for xi in x]) / self.total
        self.dst = self.var ** 0.5

        self.condensar()

    # Operación para condensar los estadísticos
    def condensar(self):
        self.stats['total'] = self.total
        self.stats['suma'] = self.suma
        self.stats['min'] = self.mini
        self.stats['max'] = self.maxi
        self.stats['prom'] = self.prom
        self.stats['var'] = self.var
        self.stats['dst'] = self.dst

    # Operación para reportar los estadísticos
    def reportar(self):
        print(f"TOTAL: {self.stats['total']}")
        print(f"SUMA: {self.stats['suma']}")
        print(f"MIN/MAX: {self.stats['min']} / {self.stats['max']}")
        print(f"PROMEDIO: {self.stats['prom']}")
        print(f"DES. EST: {self.stats['dst']}")

# Herencia de Clases (Derivar una clase para extender o reemplazar)

class EstadisticoPro(Estadistico):

    # ... todo lo de la clase Estadísticos

    # EXTENDER - Título
    title = "--- REPORTE ESTADÍSTICO ---"

    # REEMPLAZAR - Operación para reportar estadísticos
    def reportar(self):
        print(self.title)

        for k, v in self.stats.items():
            print("{:>10s} | {:>.4f}".format(k, v))


if __name__ == '__main__':
    print("=" * 40)
    
    estadistico1 = Estadistico()
    estadistico1.actualizar([1, 2, 3, 4, 5, 6])
    estadistico1.reportar()

    print("=" * 40)

    estadistico2 = Estadistico()
    estadistico2.actualizar([8.5, 9.2, 10, 7.6, 5.4, 8.4])
    estadistico2.reportar()

    print(estadistico2.stats)
    print(estadistico2.stats['var'])
    print(estadistico2.var)

    print("-" * 40)

    # estadistico2.stats -> Diccionario ({ "suma": 20, "min": 5, ... })
    # estadistico2.stats.items() -> [ ('suma', 20), ('min', 5), ... ]
    # for a, b in [ ('suma', 20), ('min', 5), ... ]
    for k, v in estadistico2.stats.items():
        print("{:^10s}: \t {:.2f}".format(k, v))

    print("=" * 40)

    estadistico3 = EstadisticoPro()

    import random

    estadistico3.actualizar([random.gauss(5.6, 1.2) for _ in range(1000)])

    estadistico3.reportar()

    print([z ** 2 for z in range(-10, 11)])

    print("=" * 40)

    estadistico4 = EstadisticoPro()

    estadistico4.condensar()

    estadistico4.reportar()


        


