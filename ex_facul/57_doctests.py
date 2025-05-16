def square(x):
    """
    Retorna o quadrado de um número.

    Exemplos:

    >>> square(3)
    9

    >>> square(-2)
    4

    >>> square(0)
    0
    """
    return x * x

import doctest
doctest.testmod()
