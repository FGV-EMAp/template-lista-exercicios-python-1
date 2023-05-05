# Lista de exercícios 1

Nessa lista, vocês irão praticar alguns conceitos básicos (mas essenciais) de Python, como:

- Definição de funções e importações de módulos
- Estruturas condicionais
- Estruturas de repetição
- Listas
- Manipulação de Strings

*ATENÇÃO*: essa lista será corrigida através de algoritmos de correção automática. Por isso, atente-se a seguir à risca nomes de arquivos, nomes de funções e tipos de entradas e saídas, conforme as descrições dadas.

### Como entregar

Todas as funções devem ser definidas num arquivo chamado `respostas.py`, que deve conter somente as definições. O arquivo deve estar situado diretamente na pasta raiz do seu repositório, e será o único arquivo observado durante a correção.

Vocês podem criar outros arquivos para testar suas funções enquanto as desenvolvem. Esses arquivos não serão observados durante a correção, então vocês podem fazer o que quiserem neles e não precisam deletá-los quando terminarem a lista.

A cada commit que fizerem, vocês devem receber um email que aponta para o relatório dos testes executados sobre as funções que vocês desenvolveram. Você só ganha os pontos de um determinado teste se ele for bem sucedido. A pontuação total da lista será a soma das pontuações de todos os testes sobre todas as funções.

Vocês também podem acessar o relatório dos seus testes seguindo os seguintes passos:
- Faça um commit no seu repositório com as últimas alterações que você fez
- Acesse o link do seu repositório no GitHub
- Clique na aba "Actions"
- Abra o item mais recente, chamado "Update GitHub Classroom Autograding Workflow"
- Clique no item "Autograding"
- Abra o conteúdo de "Run education/autograding@v1"
- Leia o log de execução dos testes

Agora que já sabem como entregar, vamos às questões!

---

### Questão 1:

Defina uma função chamada `converter_lista_para_string` que recebe como parâmetro somente uma lista. Cada elemento da lista recebida será um caractere, que juntos formam o título de filme. O papel da sua função é converter essa lista de caracteres para uma única string contendo o título do filme, e retorná-la. Nos lugares do título onde deveriam haver espaços entre as palavras, terão barras ("/"). Não se esqueça de substituí-las, e mudar **todas** as iniciais para letras maiúsculas (incluindo de artigos e preposições)!

Exemplo:

```python

>>> letras = ["e", "s", "q", "u", "e", "c", "e", "r", "a", "m", "/", "d", "e", "/", "m", "i", "m"]
>>> converter_lista_para_string(letras)
'Esqueceram de Mim'

```

---

### Questão 2:

Defina uma função `pares_e_impares` que recebe uma lista de números inteiros e retorna uma lista contendo duas sublistas, onde a primeira sublista contém apenas os números pares da lista original, e a segunda sublista contém apenas os números ímpares. 

> *Atenção*: as duas sublistas devem estar ordenadas em ordem crescente.

Exemplo:

```python

>>> numeros = [1, 3, 5, 2, 4]
>>> pares_e_impares(numeros)
[[2, 4], [1, 3, 5]]

```

---

### Questão 3:

Defina uma função `cria_matriz` que receba dois inteiros, representando as dimensões de uma matriz: M linhas e N colunas. A função deve retornar uma matriz M x N, preenchida com números inteiros de 1 até M*N em ordem crescente. 

> *Lembre*: uma matriz é representada por uma lista de listas, onde cada sublista corresponde a uma linha da matriz. Portanto, o tipo do retorno é uma lista.

Exemplo:

```python

>>> m = 2
>>> n = 3
>>> cria_matriz(m, n)
[[1, 2, 3], [4, 5, 6]]

```

---

### Questão 4:

Defina uma função `filtrar_palavras` que receba uma frase e uma letra (ou seja, duas strings). A função deve retornar uma lista com todas as palavras da frase de entrada que possuam a letra especificada. 

> Lembre que *"A" e "a" são a mesma letra*. Logo, dado "Afonso acertou a cerca ontem", e a letra especificada seja "a" ou "A", a função deve retornar ['Afonso', 'acertou', 'a', 'cerca'].

> *Dica*: Podemos converter uma frase em uma lista de palavras fazendo o **split** da frase por espaços em branco. 

Exemplo:

```python

>>> frase = "Afonso acertou a cerca ontem"
>>> letra = "a"
>>> filtrar_palavras(frase, letra)
['Afonso', 'acertou', 'a', 'cerca']

```

---

### Questão 5:

Defina uma função chamada `eh_perfeito` que receba um número inteiro e retorne um booleano, dizendo se aquele número é um número perfeito.

> *Número perfeito*: um número que é igual à soma dos seus divisores positivos diferentes dele mesmo.

Exemplo:

```python

>>> numero = 6
>>> eh_perfeito(numero)
True

```

### Desafio dos Monitores!

Tente fazer a questão 5 utilizando o conceito de Função [Lambda](https://www.w3schools.com/python/python_lambda.asp) para definir a função em uma linha só! Você também pode precisar utilizar os conceitos de list comprehension, juntamente da função `sum()`. Não vai valer ponto extra, mas quem conseguir pode mostrar como fez em uma monitoria e quem sabe ganhar um prêmio...