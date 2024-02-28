import sys

def removeEspacos(texto):
    texto_sem_espacos = texto.replace(" ", "")
    return texto_sem_espacos

def main(args):
    podeSomar = True
    resValor = 0
    anteriorOFF = False
    letra_anterior = None
    valores = ""
    
    for linha in sys.stdin:
        linha = removeEspacos(linha)
        for i, letra in enumerate(linha):
            if letra.isdigit() and podeSomar:
                if i < len(linha) - 1:
                    if (linha[i + 1]).isdigit():
                        valores += linha[i]
                    else:
                        valores += linha[i]
                        resValor += int(valores)
                        valores = ""
            else:
                if (letra == 'n' or letra == 'N') and (letra_anterior == 'o' or letra_anterior == 'O'):
                    podeSomar = True
                elif (letra == 'o' or letra == 'O') or anteriorOFF:
                    anteriorOFF = True
                    if (letra == 'f' or letra == 'F') and (letra_anterior == 'f' or letra_anterior == 'F'):
                        podeSomar = False
                        
            if (letra == '='):
                print("Valor até agora: " + str(resValor) + '\n')
                resValor = 0
                
            letra_anterior = letra
            
        
    return 0

if __name__ == "__main__":
    main(sys.argv)
