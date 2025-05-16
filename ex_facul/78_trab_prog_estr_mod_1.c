#include <stdio.h>

int main() {
    // Declaração das variáveis
    int num1, num2, num3;
    
    // Solicita ao usuário os três números inteiros
    printf("Digite o primeiro número: ");
    scanf("%d", &num1);
    printf("Digite o segundo número: ");
    scanf("%d", &num2);
    printf("Digite o terceiro número: ");
    scanf("%d", &num3);
    
    // 1. Realizar as operações aritméticas: soma, subtração, multiplicação e divisão
    int soma = num1 + num2 + num3;
    int subtracao = num1 - num2 - num3;
    int multiplicacao = num1 * num2 * num3;
    float divisao = 0;
    if (num2 != 0 && num3 != 0) {  // Verifica se não vai ocorrer divisão por zero
        divisao = (float)num1 / num2 / num3;
    }
    
    // Exibe os resultados das operações
    printf("\nResultados das operações:\n");
    printf("Soma: %d\n", soma);
    printf("Subtração: %d\n", subtracao);
    printf("Multiplicação: %d\n", multiplicacao);
    if (num2 != 0 && num3 != 0) {
        printf("Divisão: %.2f\n", divisao);
    } else {
        printf("Divisão: Não é possível dividir por zero.\n");
    }

    // 2. Verificar se o primeiro número é maior que o segundo e se o segundo é menor que o terceiro
    if (num1 > num2) {
        printf("\nO primeiro número é maior que o segundo.\n");
    } else {
        printf("\nO primeiro número não é maior que o segundo.\n");
    }

    if (num2 < num3) {
        printf("O segundo número é menor que o terceiro.\n");
    } else {
        printf("O segundo número não é menor que o terceiro.\n");
    }

    // 3. Verificar se o primeiro número é positivo e se o segundo é par
    if (num1 > 0 && num2 % 2 == 0) {
        printf("\nO primeiro número é positivo e o segundo número é par.\n");
    } else {
        printf("\nCondições não atendidas: ou o primeiro número não é positivo ou o segundo número não é par.\n");
    }

    return 0;
}
