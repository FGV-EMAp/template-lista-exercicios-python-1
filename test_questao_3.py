import respostas

def test_cria_matriz_1():
    assert respostas.cria_matriz(1, 1) == [[1]]

def test_cria_matriz_2():
    assert respostas.cria_matriz(1, 2) == [[1, 2]]

def test_cria_matriz_3():
    assert respostas.cria_matriz(2, 1) == [[1], [2]]

def test_cria_matriz_4():
    assert respostas.cria_matriz(2, 2) == [[1, 2], [3, 4]]

def test_cria_matriz_5():
    assert respostas.cria_matriz(3, 4) == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]