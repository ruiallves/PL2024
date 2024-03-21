# TPC2: Conversor de MD para HTML

Autor: Rui Pedro Castro Alves (a100699)

## Executação
Para executar o programa:

```bash
    $ python3 main.py (nome do ficheiro MD para converter) (nome do ficheiro que vai ser convertido)
```

## Conversor de MarkDown para HTML

Este programa converte texto em formato MarkDown para HTML. Ele suporta os seguintes elementos descritos na "Basic Syntax" da Cheat Sheet de MarkDown:

- Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
- Bold: pedaços de texto entre "**"
- Itálico: pedaços de texto entre "*"
- Listas numeradas
- Link: [texto](endereço URL)
- Imagem: ![texto alternativo](path para a imagem)

## Funcionamento do Conversor

- O programa analisa o texto MarkDown fornecido.
- Cada elemento MarkDown é identificado e convertido para a sintaxe HTML correspondente.
- O HTML resultante é impresso no stdout.

## Resultados

Para o seguinte input:
```
    # Exemplo

    Este é um **exemplo** de conversão de MarkDown para HTML.

    1. Primeiro item
    2. Segundo item
    3. Terceiro item

    Como pode ser consultado em [página da UC](http://www.uc.pt)

    ![imagem dum coelho](http://www.coellho.com)
```

Obtemos o output:
```
    <h1>Exemplo</h1>

    <p>Este é um <b>exemplo</b> de conversão de MarkDown para HTML.</p>

    <ol>
    <li>Primeiro item</li>
    <li>Segundo item</li>
    <li>Terceiro item</li>
    </ol>

    <p>Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a></p>

    <img src="http://www.coellho.com" alt="imagem dum coelho"/>
```
