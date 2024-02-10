
# TPC1: Análise de um dataset

Autor: Rui Pedro Castro Alves (a100699)


## Executação
Para executar o programa:

```bash
    $ cat emd.csv | python3 main.py
```


## Parse CSV
- Para o parse dos dados do csv, criamos um dicionario que vai servir para guardarmos todos os dados que pretendemos usar do csv. Com isso, redirecionamos todo o conteudo do csv para o stdin, atraves do comando $ cat emd.csv para ser utilizado no nosso programa python.
- Em seguida, lemos todas as linhas do stdin, ignorando a primeira, e guardamos no dicionario apenas o campo da idade, modalidade e resultado, utilizando funções como strip() e split(','), para dividirmos a linha em uma lista de campos utilizando um ',' como delimitador.

## Lista ordenada alfabeticamente das modalidades desportivas

- Para ordenarmos alfabeticamente todas as modalidades, criamos um set(pois este não permite valores repetidos) e preenchemos o set com todas as modalides presentes.
- Sendo assim, utilizamos a função sorted(), ordenando assim o set por ordem alfabetica.

## Percentagens de atletas aptos e inaptos para a prática desportiva

- Para a percentagem de atletas aptos e inaptos, utilizamos o resultado do atleta para verificar se estava apto ou não para a pratica desportiva.
- Sendo assim, caso o resultado seja True ou False, somamos 1 a cada variavel(percentagem_aptos ou percentagem_inaptos) dividindo o resultado pelo nr total de atletas e multiplicando por 100 para obter a percentagem.

## Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos)

- Para a distribuição de idades é criado um dicionario de idades com valores a começar nos 18 até aos 37, com intervalos de 5 anos, ou seja [18-22],[23,27],....
- Em seguida, é utilizada a mesma estratégia da query anterior, em que contamos o nr de atletas que a idade está entre o intervalo de idades atual.

## Resultados

| Desafio              | Resultado                                              |
| ----------------- | ---------------------------------------------------------------- |
| Lista ordenada alfabeticamente      | ['Andebol', 'Atletismo', 'BTT', 'Badminton', 'Basquetebol', 'Ciclismo', 'Dança', 'Equitação', 'Esgrima', 'Futebol', 'Karaté', 'Orientação', 'Parapente', 'Patinagem', 'Triatlo'] |
| Percentagens de atletas aptos| 54.0 % |
| Percentagens de atletas inaptos      | 46.0 % |
| Distribuição de atletas por escalão etário      | [18-22]: 41, [23-27]: 96, [28-32]: 110, [33-37]: 53|

[![aptos.png](https://i.postimg.cc/G3kFWHk6/aptos.png)](https://postimg.cc/qgv6nBDG)
[![idades.png](https://i.postimg.cc/7Yw3ww9h/idades.png)](https://postimg.cc/ThNLc8Zv)
