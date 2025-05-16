#include <stdio.h>

int main() {
    int avalia, cont = 0, soma = 0;
    char letra = ' ';
    float media;   

    do {
        printf("Digite uma nota para avaliação: \n");
        scanf("%d", &avalia);

        // Verifica se a nota digitada é válida (opcional)
        if (avalia < 0 || avalia > 10) {
            printf("Nota inválida! Digite uma nota entre 0 e 10.\n");
            continue; // Pula para a próxima iteração
        }

        cont++;
        soma += avalia;

        // Limpa o buffer de entrada
        while (getchar() != '\n'); // Limpa o caractere de nova linha

        printf("Digite qualquer letra para continuar ou 's' para encerrar: \n");
        letra = getchar(); // Lê um único caractere

    } while (letra != 's');

    if (cont > 0) { // Verifica para evitar divisão por zero
        printf("\nQuantidade de avaliações = %d e soma das notas = %d.\n", cont, soma);
        media = (float)soma / cont; // Garante divisão em ponto flutuante
        printf("Média das notas = %.2f\n", media);
    } else {
        printf("Nenhuma nota foi avaliada.\n");
    }

    return 0;
}
