def afundados(frota, tabuleiro):
    cont=0


    for conj in frota.values():
        for posicoes in conj:
            i=0
            comprimento=len(posicoes)
            for coordenadas in posicoes:
                linha=coordenadas[0]
                coluna=coordenadas[1]

                if tabuleiro[linha][coluna]=='X':
                    i+=1
            
            if i==comprimento:
                cont+=1
    
    return cont





