// gcc -o main main.c -L. -l:sum_of_squares.cpython-<version>-<plataforma>.so

#include <stdio.h>

// Declaración de la función externa
extern int sum_of_squares(int n);

int main() {
    int result = 0;
    int n = 1000;
    for (int i = 0; i < 100000; i++) {
        result = sum_of_squares(n) / 1000000000;
    }
    printf("The sum of squares from 1 to %d is: %d\n", n, result);
    return 0;
}
