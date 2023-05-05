import respostas

def test_filtrar_palavras_1():
    frase = "Afonso acertou a cerca ontem"
    letra = "a"

    assert respostas.filtrar_palavras(frase, letra) == ["Afonso", "acertou", "a", "cerca"]

def test_filtrar_palavras_2():
    frase = "Afonso acertou a cerca ontem"
    letra = "A"

    assert respostas.filtrar_palavras(frase, letra) == ["Afonso", "acertou", "a", "cerca"]

def test_filtrar_palavras_3():
    frase = "Maria mora em Mariana"
    letra = "j"

    assert respostas.filtrar_palavras(frase, letra) == []

def test_filtrar_palavras_4():
    frase = "Aprender Python é muito legal"
    letra = "p"

    assert respostas.filtrar_palavras(frase, letra) == ["Aprender", "Python"]