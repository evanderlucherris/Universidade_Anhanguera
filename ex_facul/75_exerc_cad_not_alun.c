#include <stdio.h>
#include <string.h>

struct Aluno {
    char nome[50];
    int matricula;
    float notas[2]; // Considerando 2 disciplinas para simplificar o código
};

struct Turma {
    int numeroTurma;
    struct Aluno alunos[30]; // Considerando até 30 alunos por turma
    int totalAlunos;
};

int main() {
    struct Aluno alunos[5]; // 5 alunos cadastrados
    struct Turma turmas[10]; // 10 turmas disponíveis
    int op;

    // Cadastrar os alunos
    strcpy(alunos[0].nome, "João");
    alunos[0].matricula = 1001;
    alunos[0].notas[0] = 8.5;
    alunos[0].notas[1] = 7.0;

    strcpy(alunos[1].nome, "Maria");
    alunos[1].matricula = 1002;
    alunos[1].notas[0] = 7.5;
    alunos[1].notas[1] = 8.0;

    strcpy(alunos[2].nome, "Pedro");
    alunos[2].matricula = 1003;
    alunos[2].notas[0] = 9.0;
    alunos[2].notas[1] = 9.5;

    strcpy(alunos[3].nome, "Ana");
    alunos[3].matricula = 1004;
    alunos[3].notas[0] = 7.0;
    alunos[3].notas[1] = 7.5;

    strcpy(alunos[4].nome, "Carlos");
    alunos[4].matricula = 1005;
    alunos[4].notas[0] = 8.0;
    alunos[4].notas[1] = 8.5;

    // Inicializa as turmas
    turmas[0].totalAlunos = 0;
    turmas[0].numeroTurma = 5000;

    turmas[1].totalAlunos = 0;
    turmas[1].numeroTurma = 6000;

    int a, t;
    float mediaTurma = 0.0;

    do {
        printf("\n1 - Cadastrar aluno na turma\n");
        printf("2 - Lançar notas de aluno\n");
        printf("3 - Média da turma\n");
        printf("4 - Relatório de turma\n");
        printf("5 - Encerrar\n");
        printf("Opção: ");
        scanf("%d", &op);

        switch (op) {
            case 1:
                printf("Escolha o aluno (0 a 4): ");
                scanf("%d", &a);
                if (a < 0 || a > 4) {
                    printf("Aluno inválido!\n");
                    break;
                }
                printf("Escolha a turma (0 a 9): ");
                scanf("%d", &t);
                if (t < 0 || t > 9) {
                    printf("Turma inválida!\n");
                    break;
                }
                if (turmas[t].totalAlunos < 30) {
                    turmas[t].alunos[turmas[t].totalAlunos] = alunos[a];
                    turmas[t].totalAlunos++;
                } else {
                    printf("A turma está cheia. Não é possível adicionar mais alunos.\n");
                }
                break;

            case 2:
                printf("Escolha o aluno (0 a 4): ");
                scanf("%d", &a);
                if (a < 0 || a > 4) {
                    printf("Aluno inválido!\n");
                    break;
                }
                for (int i = 0; i < 2; i++) {
                    printf("Nota %d: ", i + 1);
                    scanf("%f", &alunos[a].notas[i]);
                }
                break;

            case 3:
                printf("Escolha a turma (0 a 9): ");
                scanf("%d", &t);
                if (t < 0 || t > 9) {
                    printf("Turma inválida!\n");
                    break;
                }
                mediaTurma = 0.0;
                for (int i = 0; i < turmas[t].totalAlunos; i++) {
                    float somaNotas = 0.0;
                    for (int j = 0; j < 2; j++) { // 2 notas por aluno
                        somaNotas += turmas[t].alunos[i].notas[j];
                    }
                    mediaTurma += somaNotas / 2;
                }
                if (turmas[t].totalAlunos > 0) {
                    printf("\nMédia da turma: %.2f\n", mediaTurma / turmas[t].totalAlunos);
                } else {
                    printf("A turma não tem alunos cadastrados.\n");
                }
                break;

            case 4:
                printf("Escolha a turma (0 a 9): ");
                scanf("%d", &t);
                if (t < 0 || t > 9) {
                    printf("Turma inválida!\n");
                    break;
                }
                printf("\nTurma %d\n", turmas[t].numeroTurma);
                for (int i = 0; i < turmas[t].totalAlunos; i++) {
                    printf("Aluno: %s\n", turmas[t].alunos[i].nome);
                    printf("Matrícula: %d\n", turmas[t].alunos[i].matricula);
                    printf("Notas: ");
                    for (int j = 0; j < 2; j++) {
                        printf("%.2f ", turmas[t].alunos[i].notas[j]);
                    }
                    printf("\n");
                }
                break;

            default:
                printf("Programa encerrado!\n\n");
                break;
        }
    } while (op != 5);

    return 0;
}
