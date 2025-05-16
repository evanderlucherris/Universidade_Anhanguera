#include <stdio.h>

int main() {
    int numero, soma = 0;

    // Inicia o loop aguardando a entrada do usuário
    while (1) {
        // Solicita ao usuário que insira um número inteiro
        printf("Digite um número inteiro (digite 0 para encerrar): ");
        scanf("%d", &numero);

        // Verifica se o número inserido é zero, caso em que o loop é encerrado
        if (numero == 0) {
            break;
        }

        // Se o número não for zero, ele é somado à variável soma
        soma += numero;
    }

    // Exibe o resultado final da soma
    printf("A soma total dos números inseridos é: %d\n", soma);

    return 0;
}
