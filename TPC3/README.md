# TPC3: Somador on/off

Autor: Rui Pedro Castro Alves (a100699)

## Executação
Para executar o programa:

```bash
    $ cat test.txt | python3 main.py
```

## Somador ON/OFF

Este programa recebe de entrada um ficheiro de texto e soma todas as sequências de dígitos encontradas, com base na ativação e desativação do comportamento de soma.
- Sempre que encontrar a string "Off" em qualquer combinação de maiúsculas e minúsculas, o comportamento de soma é desligado.
- Sempre que encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas, o comportamento de soma é ligado.
- Sempre que encontrar o caractere "=", o resultado da soma é colocado na saída, resetando o contador da soma.
- Assumimos, no inicio, que o comportamento da soma está ligado.

## Resultados

Para o seguinte input:
```
    135gwero 3on4=a
    1off23on4=
```

Devemos obter o output de:
```
    Valor até agora: 142 (135+3+4)
    Valor até agora: 5 (1+4)
```

## Autómato

[![Untitled-1.png](https://i.postimg.cc/sgwcJ79m/Untitled-1.png)](https://postimg.cc/nX9BFsW9)