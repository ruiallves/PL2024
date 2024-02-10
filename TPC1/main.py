import sys

if __name__ == "__main__":
    dados = []
    primeira_linha = True
    for linha in sys.stdin:
        if primeira_linha:
            primeira_linha = False
            continue
        campos = linha.strip().split(',')
        dados.append({'idade': int(campos[5]), 'modalidade': campos[8], 'resultado': campos[-1]})

    modalidades = sorted(set(d['modalidade'] for d in dados))
    print("Modalidades desportivas:", modalidades)
    
    percentagem_aptos, percentagem_inaptos = [(sum(1 for d in dados if d['resultado'] == 'true') / len(dados)) * 100, (sum(1 for d in dados if d['resultado'] == 'false') / len(dados)) * 100]
    print("Percentagem de atletas aptos:", percentagem_aptos)
    print("Percentagem de atletas inaptos:", percentagem_inaptos)    
    
    distribuicao_idade = {idade: sum(1 for d in dados if (d['idade'] >= idade and d['idade'] < idade + 5)) for idade in range(18, 37, 5)}
    print("Distribuição de atletas por escalão etário:")
    for escalao, quantidade in distribuicao_idade.items():
        print(f"[{escalao}-{escalao+4}]:", quantidade)
