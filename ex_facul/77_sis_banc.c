#include <stdio.h>

// Estrutura para representar a Conta
struct Conta {
    int numero;
    char titular[50];
    float saldo;
};

// Função para realizar o depósito
void realizarDeposito(struct Conta *conta, float valor) {
    if (valor > 0) {
        conta->saldo += valor;
        printf("Depósito de R$%.2f realizado com sucesso.\n", valor);
    } else {
        printf("Valor inválido para depósito.\n");
    }
}

// Função para realizar o saque
int realizarSaque(struct Conta *conta, float valor) {
    if (valor <= 0) {
        printf("Valor inválido para saque.\n");
        return 0; // Falha no saque
    }

    if (conta->saldo >= valor) {
        conta->saldo -= valor;
        printf("Saque de R$%.2f realizado com sucesso.\n", valor);
        return 1; // Sucesso no saque
    } else {
        printf("Saldo insuficiente para realizar o saque.\n");
        return 0; // Falha no saque
    }
}

// Função para realizar a transferência
int realizarTransferencia(struct Conta *origem, struct Conta *destino, float valor) {
    if (valor <= 0) {
        printf("Valor inválido para transferência.\n");
        return 0; // Falha na transferência
    }

    if (realizarSaque(origem, valor)) {
        realizarDeposito(destino, valor);
        printf("Transferência de R$%.2f realizada de Conta %d para Conta %d com sucesso.\n", valor, origem->numero, destino->numero);
        return 1; // Sucesso na transferência
    } else {
        printf("Transferência mal-sucedida devido a saldo insuficiente.\n");
        return 0; // Falha na transferência
    }
}

// Função principal para interação com o usuário
int main() {
    // Criação de duas instâncias da estrutura Conta
    struct Conta contas[2] = {{1, "Cliente1", 1000.0}, {2, "Cliente2", 500.0}};
    
    int op, cc, cc2;
    float valor = 0;

    do {
        // Exibição do menu
        printf("\nBOLSOFURADO BANK\n\n");
        printf("Saldo Conta 1: R$%.2f\n", contas[0].saldo);
        printf("Saldo Conta 2: R$%.2f\n\n", contas[1].saldo);

        printf("1 - Depósito\n");
        printf("2 - Saque\n");
        printf("3 - Transferência\n");
        printf("4 - Sair\n");

        // Leitura da opção
        printf("\nEscolha uma opção: ");
        scanf("%d", &op);

        switch (op) {
            case 1:
                printf("\nQual a conta para depósito? (1 ou 2): ");
                scanf("%d", &cc);
                printf("Qual o valor? ");
                scanf("%f", &valor);
                if (cc == 1 || cc == 2) {
                    realizarDeposito(&contas[cc - 1], valor);
                } else {
                    printf("Conta inválida.\n");
                }
                break;

            case 2:
                printf("\nQual a conta para saque? (1 ou 2): ");
                scanf("%d", &cc);
                printf("Qual o valor? ");
                scanf("%f", &valor);
                if (cc == 1 || cc == 2) {
                    realizarSaque(&contas[cc - 1], valor);
                } else {
                    printf("Conta inválida.\n");
                }
                break;

            case 3:
                printf("\nQual a conta de origem? (1 ou 2): ");
                scanf("%d", &cc);
                printf("Qual a conta de destino? (1 ou 2): ");
                scanf("%d", &cc2);
                printf("Qual o valor? ");
                scanf("%f", &valor);
                if ((cc == 1 || cc == 2) && (cc2 == 1 || cc2 == 2) && cc != cc2) {
                    realizarTransferencia(&contas[cc - 1], &contas[cc2 - 1], valor);
                } else {
                    printf("Conta inválida ou contas de origem e destino são iguais.\n");
                }
                break;

            case 4:
                printf("Saindo do sistema. Até logo!\n");
                break;

            default:
                printf("Opção inválida. Tente novamente.\n");
                break;
        }

    } while (op != 4);

    return 0;
}
