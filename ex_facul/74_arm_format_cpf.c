#include <stdio.h>

int main() {
    char cpf1[15]; // Array para armazenar o CPF formatado (NNN.NNN.NNN-NN)
    char cpf2[12]; // Array para armazenar o CPF sem formatação, tamanho 12 para incluir o terminador nulo

    int i = 0, n = 0;

    printf("Digite seu CPF na forma NNN.NNN.NNN-NN: \n");
    scanf("%14s", cpf1); // Limita a entrada para evitar overflow

    // Laço para percorrer o CPF de entrada
    for (i = 0; i < 14; i++) {
        // Verifica se o caractere atual é um dígito
        if (cpf1[i] >= '0' && cpf1[i] <= '9') {
            // Armazena o dígito em cpf2
            cpf2[n] = cpf1[i];
            n++; // Aumenta a contagem de dígitos armazenados
        }
    }

    // Adiciona o terminador nulo na string cpf2
    cpf2[n] = '\0'; 

    // Imprime o CPF sem formatação
    printf("\n\nCPF formatado = %s\n", cpf2);

    return 0;
}
