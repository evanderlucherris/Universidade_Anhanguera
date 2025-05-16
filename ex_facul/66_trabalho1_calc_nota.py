def cadastrar_notas():
    notas = []
    primeira_nota = False  # Variável para controlar se a primeira nota foi inserida

    while True:
        if primeira_nota:
            entrada = input("Digite a nota do aluno, digite 'calc' para calcular ou 'sair' para encerrar: ")
        else:
            entrada = input("Digite a nota do aluno (ou digite 'sair' para encerrar): ")

        if entrada.lower() == "sair":  # Verifica se o usuário deseja sair
            print("Saindo do sistema.")
            exit()  # Encerra a execução do programa

        if primeira_nota and entrada.lower() == "calc":  # Permite calcular apenas após a primeira nota
            break  # Se houver notas, finaliza a entrada

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:  # Verifica se a nota está no intervalo permitido
                notas.append(nota)
                primeira_nota = True  # Marca que a primeira nota foi inserida
            else:
                print("Nota inválida! A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

    return notas

def calcular_media(notas):
    if len(notas) == 0:  # Evita divisão por zero
        return 0
    return sum(notas) / len(notas)

def determinar_situacao(media):
    if media >= 7:  # Situação baseada na média
        return "Aprovado"
    else:
        return "Reprovado"

def exibir_relatorio(notas, media, situacao):
    print("\n----- Relatório Final -----")
    print(f"Notas inseridas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

def main():
    print("Sistema de Gestão de Notas de Alunos")
    
    # Cadastrar notas
    notas = cadastrar_notas()
    
    if not notas:  # Verifica se nenhuma nota foi inserida
        print("Nenhuma nota foi inserida.")
        return
    
    # Calcular média
    media = calcular_media(notas)
    
    # Determinar situação
    situacao = determinar_situacao(media)
    
    # Exibir relatório
    exibir_relatorio(notas, media, situacao)

if __name__ == "__main__":
    main()

#O programa começa pedindo as notas dos alunos. Você pode continuar digitando até querer calcular a média, digitando "calc", ou sair com "sair". Depois da primeira nota, a mensagem muda para te ajudar.
#O sistema verifica se as notas estão entre 0 e 10. Ao digitar "calc", ele calcula a média, diz se o aluno está "Aprovado" (média ≥ 7) ou "Reprovado" (média < 7), e mostra um resumo com todas as notas e a situação.
#Se precisar sair, é só digitar "sair". É um jeito simples e prático de gerenciar as notas!