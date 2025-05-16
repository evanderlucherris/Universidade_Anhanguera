#include <stdio.h>

int main() {
    int linhas, espacos, asteriscos;

    printf("Digite o número de linhas do triângulo: ");
    scanf("%d", &linhas);

    for (int i = 1; i <= linhas; i++) {
        // Imprimir espaços
        for (espacos = 1; espacos <= linhas - i; espacos++) {
            printf(" ");
        }

        // Imprimir asteriscos
        for (asteriscos = 1; asteriscos <= 2 * i - 1; asteriscos++) {
            printf("*");
        }

        // Pular linha após cada linha do triângulo
        printf("\n");
    }

    return 0;
}
