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

        
