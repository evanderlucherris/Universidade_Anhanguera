class Produto:
    # Representa um produto com características específicas do produto.
    def __init__(self, nome, categoria, quantidade, preco, localizacao_estoque):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao_estoque = localizacao_estoque

    def __str__(self):
        # Retorna uma string formatada com as informações do produto
        return (f'Nome: {self.nome.title()}\n'
                f'Categoria: {self.categoria}\n'
                f'Quantidade: {self.quantidade}\n'
                f'Preço: R${self.preco:.2f}\n'
                f'Localização No Estoque: {self.localizacao_estoque}')

# Dicionário para armazenar os produtos, com o nome como chave
produtos = {}

# Limites de estoque para gerar relatórios
estoque_baixo_minimo = 5  # Limite para estoque baixo
estoque_maximo = 50  # Limite para excesso de estoque

def verificar_campos_vazios(nome, categoria, quantidade, preco, localizacao_estoque):
    if not nome.strip() or not categoria.strip() or not localizacao_estoque.strip():
        raise ValueError("Nome, categoria e localização não podem ser vazios.")
    if not isinstance(quantidade, int) or quantidade < 0:
        raise ValueError("Quantidade deve ser um número inteiro não negativo.")
    if not isinstance(preco, float) or preco <= 0:
        raise ValueError("Preço deve ser um valor numérico maior que zero.")

def buscar_produto(nome):
    # Busca produto pelo nome
    return produtos.get(nome.lower())

def exibir_produto(produto):
    print(f'Nome: {produto.nome.title()}')
    print(f'Categoria: {produto.categoria}')
    print(f'Quantidade: {produto.quantidade}')
    print(f'Preço: R${produto.preco:.2f}')
    print(f'Localização No Estoque: {produto.localizacao_estoque}')
    print('-' * 40)

def cadastrar_produto(nome, categoria, quantidade, preco, localizacao_estoque):
    nome_normalizado = nome.strip().lower()  # Normaliza o nome para evitar duplicatas com capitalização diferente
    if nome_normalizado in produtos:
        print(f'O produto "{nome.title()}" já está cadastrado.')
        return

    try:
        verificar_campos_vazios(nome, categoria, quantidade, preco, localizacao_estoque)
    except ValueError as e:
        print(e)
        return

    produto = Produto(nome, categoria, quantidade, preco, localizacao_estoque)
    produtos[nome_normalizado] = produto
    print(f'Produto "{produto.nome.title()}" cadastrado com sucesso!')

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de Produtos Cadastrados:")
        for produto in produtos.values():
            exibir_produto(produto)

def movimentar_produto(nome, quantidade):
    produto = buscar_produto(nome)
    if produto:
        if quantidade == 0:
            print("Erro: A quantidade a ser movimentada não pode ser zero.")
            return
        if quantidade > 0:
            produto.quantidade += quantidade
            print(f'{quantidade} unidades de "{produto.nome.title()}" adicionadas ao estoque.')
        else:
            if produto.quantidade + quantidade >= 0:  # Garantir que não haja estoque negativo
                produto.quantidade += quantidade
                print(f'{abs(quantidade)} unidades de "{produto.nome.title()}" removidas do estoque.')
            else:
                print(f'Erro: Não há estoque suficiente de "{produto.nome.title()}".')
    else:
        print(f'O produto "{nome}" não foi encontrado.')

def gerar_relatorio_estoque():
    if not produtos:
        print("Nenhum produto cadastrado para gerar relatório.")
        return

    print("\n** Relatório de Estoque **")
    total_produtos_baixo = 0
    total_produtos_excesso = 0
    total_produtos_ideal = 0
    valor_total_baixo = 0
    valor_total_excesso = 0
    valor_total_ideal = 0

    # Categorias de produtos
    for produto in produtos.values():
        if produto.quantidade < estoque_baixo_minimo:
            exibir_produto(produto)
            total_produtos_baixo += 1
            valor_total_baixo += produto.quantidade * produto.preco
        elif produto.quantidade > estoque_maximo:
            exibir_produto(produto)
            total_produtos_excesso += 1
            valor_total_excesso += produto.quantidade * produto.preco
        else:
            exibir_produto(produto)
            total_produtos_ideal += 1
            valor_total_ideal += produto.quantidade * produto.preco

    # Resumo do Relatório
    print("\n** Resumo do Relatório **")
    print(f'Total de produtos cadastrados: {len(produtos)}')
    print(f'Produtos com estoque baixo: {total_produtos_baixo} (Valor total: R${valor_total_baixo:.2f})')
    print(f'Produtos com excesso de estoque: {total_produtos_excesso} (Valor total: R${valor_total_excesso:.2f})')
    print(f'Produtos com estoque ideal: {total_produtos_ideal} (Valor total: R${valor_total_ideal:.2f})')

def atualizar_estoque(nome, quantidade):
    produto = buscar_produto(nome)
    if produto:
        produto.quantidade += quantidade
        print(f'O estoque de "{produto.nome.title()}" foi atualizado para {produto.quantidade} unidades.')

def rastrear_localizacao(nome):
    produto = buscar_produto(nome)
    if produto:
        print(f'O produto "{produto.nome.title()}" se encontra no estoque em: {produto.localizacao_estoque}')

def atualizar_localizacao(nome, nova_localizacao):
    produto = buscar_produto(nome)
    if produto:
        produto.localizacao_estoque = nova_localizacao
        print(f'O produto: "{produto.nome.title()}" foi atualizado para o estoque: {nova_localizacao}')

def obter_numero_inteiro(mensagem, tipo='inteiro'):
    while True:
        try:
            valor = input(mensagem)
            if tipo == 'inteiro':
                return int(valor)
            elif tipo == 'flutuante':
                return float(valor)
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def excluir_produto(nome):
    nome_normalizado = nome.strip().lower()  # Normaliza o nome antes de procurar e excluir
    produto = buscar_produto(nome_normalizado)
    if produto:
        confirmacao = input(f"Você tem certeza que deseja excluir o produto {produto.nome.title()}? (s/n): ")
        if confirmacao.lower() == 's':
            del produtos[nome_normalizado]
            print(f'O produto "{produto.nome.title()}" foi excluído com sucesso.')
        else:
            print("A exclusão foi cancelada.")
    else:
        print(f'O produto "{nome}" não foi encontrado.')

def buscar_produto_menu():
    nome = input("Digite o nome do produto para buscar: ")
    produto = buscar_produto(nome)
    if produto:
        exibir_produto(produto)
    else:
        print(f"Produto '{nome}' não encontrado.")

def main():
    while True:
        print("\n1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Excluir Produto")
        print("4. Buscar Produto")
        print("5. Gerar Relatório")
        print("6. Atualizar Estoque")
        print("7. Rastrear Localização do Produto")
        print("8. Atualizar a Localização do Produto")
        print("0. Sair do Sistema")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            nome = input("Nome do Produto: ")
            categoria = input("Categoria: ")
            quantidade = obter_numero_inteiro("Quantidade Disponível: ", 'inteiro')
            preco = obter_numero_inteiro("Preço: R$", 'flutuante')
            localizacao_estoque = input("Localização No Estoque: ")

            cadastrar_produto(nome, categoria, quantidade, preco, localizacao_estoque)
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            nome = input("Digite o nome do produto para excluir: ")
            excluir_produto(nome)
        elif opcao == '4':
            buscar_produto_menu()
        elif opcao == '5':
            gerar_relatorio_estoque()
        elif opcao == '6':
            nome = input("Digite o nome do produto para atualizar o estoque: ")
            quantidade = obter_numero_inteiro("Digite a quantidade a ser adicionada ou retirada do estoque: ", 'inteiro')
            movimentar_produto(nome, quantidade)
        elif opcao == '7':
            nome = input("Digite o nome do produto para rastrear sua localização em Estoque: ")
            rastrear_localizacao(nome)
        elif opcao == '8':
            nome = input("Digite o nome do produto para atualizar a localização em Estoque: ")
            nova_localizacao = input("Digite a nova localização do produto: ")
            atualizar_localizacao(nome, nova_localizacao)
        elif opcao == '0':
            print("Finalização do sistema.")
            break
        else:
            print("Opção não encontrada, tente novamente.")

if __name__ == "__main__":
    main()
