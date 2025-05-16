#include <stdio.h>

int main(){

// Variáveis

float precoVenda, valorImposto, valorDesconto, precoFinal;

// Constantes

const float taxaImposto = 0.1;

const float descontoPadrao = 0.05;

// Entrada

printf("Informe o preço de venda do produto: ");

scanf("%f", &precoVenda);

// Processamento

valorImposto = precoVenda * taxaImposto;

valorDesconto = precoVenda * descontoPadrao;

precoFinal = precoVenda + valorImposto - valorDesconto;

// Saída

printf("O preço final do televisor é: R$ %.2f", precoFinal);

return 0;

}