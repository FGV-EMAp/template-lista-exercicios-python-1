import respostas

def test_converter_lista_para_string_1():
    # Escrever uma lista com os caracteres de "esqueceram de mim"
    lista = ["e", "s", "q", "u", "e", "c", "e", "r", "a", "m", "/", "d", "e", "/", "m", "i", "m"]
    assert respostas.converter_lista_para_string(lista) == "Esqueceram De Mim"

def test_converter_lista_para_string_2():
    # Escrever uma lista com os caracteres de "alvin e os equilos"
    lista = ["a", "l", "v", "i", "n", "/", "e", "/", "o", "s", "/", "e", "s", "q", "u", "i", "l", "o", "s"]
    assert respostas.converter_lista_para_string(lista) == "Alvin E Os Esquilos"

def test_converter_lista_para_string_3():
    # Escrever uma lista com os caracteres de "a era do gelo"
    lista = ["A", "/", "E", "r", "a", "/", "D", "o", "/", "G", "e", "l", "o"]
    assert respostas.converter_lista_para_string(lista) == "A Era Do Gelo"

def test_converter_lista_para_string_4():
    # Escrever uma lista com os caracteres de "a pequena sereia"
    lista = ["A", "/", "p", "E", "q", "u", "e", "N", "a", "/", "s", "e", "R", "e", "i", "a"]
    assert respostas.converter_lista_para_string(lista) == "A Pequena Sereia"

def test_converter_lista_para_string_5():
    # Escrever uma lista com os caracteres de "a branca de neve"
    lista = ["a", "/", "b", "r", "a", "n", "c", "a", "/", "d", "e", "/", "n", "e", "v", "e"]
    assert respostas.converter_lista_para_string(lista) == "A Branca De Neve"