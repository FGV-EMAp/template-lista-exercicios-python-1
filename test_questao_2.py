import respostas

def test_pares_e_impares_1():
    # Escrever uma lista com os números de 1 a 10, em ordem aleatoria
    lista = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    assert respostas.pares_e_impares(lista) == [[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]]

def test_pares_e_impares_2():
    # Escrever uma lista com os números de 1 a 100
    lista = list(range(1, 101))
    assert respostas.pares_e_impares(lista) == [list(range(2, 101, 2)), list(range(1, 101, 2))]

def test_pares_e_impares_3():
    # Escrever uma lista com os números primos de 1 a 30, em ordem aleatoria
    lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert respostas.pares_e_impares(lista) == [[2], [3, 5, 7, 11, 13, 17, 19, 23, 29]]

def test_pares_e_impares_4():
    # Escrever uma lista com os números de -10 a 10
    lista = list(range(-10, 11))
    assert respostas.pares_e_impares(lista) == [[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10], [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]]