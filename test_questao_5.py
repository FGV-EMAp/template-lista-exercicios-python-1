import respostas

def test_eh_perfeito_1():
    assert respostas.eh_perfeito(1) == False

def test_eh_perfeito_2():
    assert respostas.eh_perfeito(2) == False

def test_eh_perfeito_3():
    assert respostas.eh_perfeito(3) == False

def test_eh_perfeito_4():
    assert respostas.eh_perfeito(6) == True
    
def test_eh_perfeito_5():
    assert respostas.eh_perfeito(8128) == True