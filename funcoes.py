
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

def faz_jogada(tabuleiro, linha, coluna):
    if linha < 0 or linha >= len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro[0]):
        return tabuleiro


    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

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

def afundados(frota, tabuleiro):
    cont=0


    for macro in frota.values():
        for posicoes in macro:
            i=0
            comprimento=len(posicoes)
            for coordenadas in posicoes:
                linha=coordenadas[0]
                coluna=coordenadas[1]

                if tabuleiro[linha][coluna]:
                    i+=1
        
            if i==comprimento:
                cont+=1
    
    return cont

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    for pos in posicoes_novo_navio:
        l, c = pos
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False  # Sai do tabuleiro

    # 2. Verifica se há colisão com navios já existentes
    for conjunto_navios in frota.values():
        for navio in conjunto_navios:
            for pos_existente in navio:
                if pos_existente in posicoes_novo_navio:
                    return False  # Colisão detectada

    return True