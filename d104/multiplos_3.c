/*
 * Problema: Contar cuántos múltiplos de 3 hay 
 *           del 1 al 1,000,000
 */

// Importamos la librería que contiene el `printf`
#include <stdio.h>

// Definimos la función principal
int main() {

    // Declaramos y asignamos la variable `contador`
    int contador = 0;

    // Recorremos un iterador del 1 al 1,000,000
    for (int i = 1; i < 1000000; i++) {
        // Verificamos si el iterador es múltiplo de 3
        if (i % 3 == 0) {
            // Incrementamos los que son múltiplos de 3
            contador++;
        }
    }

    printf("Hay %d múltiplos de 3 del 1 al 1,000,000\n", contador);

}

