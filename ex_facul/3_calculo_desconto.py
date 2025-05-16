preco_unitario = 10
DESCONTO10 = 0.1
DESCONTO20 = 0.2
quantidade = eval(input("Digite a quantidade que vai comprar: "))
if(quantidade <= 10): #Menor ou igual a 10
    valor_final = preco_unitario*quantidade
elif(quantidade <= 20): #Maior que 10, menor ou igual a 20
    valor_final = preco_unitario*quantidade*(1-DESCONTO10)
else: #Maior que 20
    valor_final = preco_unitario*quantidade*(1-DESCONTO20)

print(f'O valor final da compra é: {valor_final}')