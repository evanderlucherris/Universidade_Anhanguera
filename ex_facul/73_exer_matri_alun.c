#include <stdio.h>
#include <stdlib.h>

int main() {
    int total_disciplinas, limite_alunos = 100, total_alunos = 0;

    printf("Sistema de contagem de alunos matriculados!\n");
    printf("Insira o número de disciplinas disponíveis: ");
    scanf("%d", &total_disciplinas);

    // Valida o número de disciplinas
    if (total_disciplinas <= 0) {
        printf("Número de disciplinas deve ser maior que zero.\n");
        return 1; // Encerra o programa se o valor for inválido
    }

    for (int i = 1; i <= total_disciplinas; i++) {
        int alunos_matriculados;

        printf("Insira o número de alunos matriculados na disciplina %d: ", i);
        scanf("%d", &alunos_matriculados);

        // Verifica se o número de alunos matriculados é válido
        if (alunos_matriculados < 0) {
            printf("Número de alunos inválido. Tente novamente.\n");
            i--; // Volta para a mesma disciplina
            continue; // Pula para a próxima iteração do loop
        }

        total_alunos += alunos_matriculados;

        // Verifica se o limite de alunos foi atingido
        if (total_alunos >= limite_alunos) {
            printf("Limite de alunos atingido. Encerrando contagem de disciplinas.\n");
            break; // Encerra o loop de contagem de disciplinas
        }
    }

    printf("Total de disciplinas contadas: %d\n", total_disciplinas);
    printf("Total de alunos matriculados: %d\n", total_alunos);

    return 0;
}
