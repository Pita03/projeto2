
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    i = 0

    while i < tamanho:
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        elif orientacao == "horizontal":
            posicoes.append([linha, coluna + i])
        i += 1

    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = []

    frota[nome_navio].append(posicoes)
    
    return frota

def posiciona_frota(navio_dicio):
    tabuleiro_f=[]
    linha=[]

    for i in range(10):
        linha = []
        for c in range(10):
            linha.append(0)
        tabuleiro_f.append(linha)
    

    for conjunto in navio_dicio.values():
        for posicoes in conjunto:
            for coordenadas in posicoes:
                linha=coordenadas[0]
                coluna=coordenadas[1]
                tabuleiro_f[linha][coluna]=1
    
    return tabuleiro_f