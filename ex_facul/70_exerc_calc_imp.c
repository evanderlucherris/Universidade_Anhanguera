#include <stdio.h>

int main() {
    float salario, inss, ir, sal_liquido;

    printf("Calculo de Salario Liquido Com desconto do IR e INSS\n\n");
    printf("Digite seu salario Bruto: ");
    scanf("%f", &salario);

    // Calcular o INSS
    if (salario <= 1320) {
        inss = salario * 0.075;
    } else if (salario <= 2571.29) {
        inss = salario * 0.09;
    } else if (salario <= 3856.94) {
        inss = salario * 0.12;
    } else if (salario <= 7507.49) {
        inss = salario * 0.14;
    } else {
        inss = 1051.04; // teto de contribuição
    }

    // Calcular o IR
    if (salario <= 1903.98) {
        ir = 0;
    } else if (salario <= 2826.65) {
        ir = (salario - 1903.98) * 0.075;
    } else if (salario <= 3751.05) {
        ir = (salario - 2826.65) * 0.15 + (2826.65 - 1903.98) * 0.075;
    } else if (salario <= 4664.68) {
        ir = (salario - 3751.05) * 0.225 + (3751.05 - 2826.65) * 0.15 + (2826.65 - 1903.98) * 0.075;
    } else {
        ir = (salario - 4664.68) * 0.275 + (4664.68 - 3751.05) * 0.225 + (3751.05 - 2826.65) * 0.15 + (2826.65 - 1903.98) * 0.075;
    }

    // Calculo do Salario liquido
    sal_liquido = salario - inss - ir;

    // Resultados
    printf("\nDesconto do INSS: %.2f\n", inss);
    printf("Desconto do imposto de renda: %.2f\n", ir);
    printf("Salário líquido: %.2f\n", sal_liquido);

    return 0;
}