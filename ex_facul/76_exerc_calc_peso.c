#include <stdio.h>

int calcularPeso() {
    float b, c, h;

    // Solicitar e ler os valores do usuário
    printf("\nDigite o valor da base: ");
    scanf("%f", &b);

    printf("\nDigite o valor da altura: ");
    scanf("%f", &h);

    printf("\nDigite o valor do comprimento: ");
    scanf("%f", &c);

    // Cálculo do peso (base * altura * comprimento * fator de densidade)
    return (int)(b * h * c * 25); // Convertendo para inteiro
}

int main() {
    int peso;

    // Calcular o peso
    peso = calcularPeso();

    // Determinar qual guindaste utilizar com base no peso
    if (peso <= 500) {
        printf("\nO guindaste de modelo G1 deve ser usado.\n");
    } else if (peso > 1500) {
        printf("\nO guindaste de modelo G3 deve ser usado.\n");
    } else {
        printf("\nO guindaste de modelo G2 deve ser usado.\n");
    }

    return 0;
}
