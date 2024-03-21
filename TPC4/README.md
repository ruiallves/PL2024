# TPC3: Somador on/off

Autor: Rui Pedro Castro Alves (a100699)

## Executação
Para executar o programa:

```bash
    $ python3 analex.py
```

## Tokens Reconhecidos

O analisador léxico reconhece os seguintes tokens:

- SELECT: Representa a palavra-chave "SELECT".
- FROM: Representa a palavra-chave "FROM".
- WHERE: Representa a palavra-chave "WHERE".
- OPERATOR: Representa operadores de comparação (<, >, =).
- NUMBER: Representa números inteiros.
- COMMA: Representa uma vírgula.
- ATTRIBUTE: Representa os atributos.

## Resultados

Para o seguinte input:
```
    data = 'SELECT id, nome, salario FROM empregados WHERE salario>=820'
```

Devemos obter o output de:
```
    LexToken(SELECT,'SELECT',1,0)
    LexToken(ATTRIBUTE,'id',1,7)
    LexToken(COMMA,',',1,9)
    LexToken(ATTRIBUTE,'nome',1,11)
    LexToken(COMMA,',',1,15)
    LexToken(ATTRIBUTE,'salario',1,17)
    LexToken(FROM,'FROM',1,25)
    LexToken(ATTRIBUTE,'empregados',1,30)
    LexToken(WHERE,'WHERE',1,41)
    LexToken(ATTRIBUTE,'salario',1,47)
    LexToken(OPERATOR,'>=',1,54)
    LexToken(NUMBER,820,1,56)
```