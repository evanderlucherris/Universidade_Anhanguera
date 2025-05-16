def divide(x, y):
    assert y != 0, "Divisão por zero!"
    return x / y

try:
    result = divide(6, 0)
    print(result)
except AssertionError as e:
    print(e)  # Isso irá imprimir: Divisão por zero!
