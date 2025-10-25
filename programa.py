from funcoes import posicao_valida, define_posicoes, preenche_frota

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     

navios = {
    "porta-aviões" : 4,
    "navio-tanque" : 3,
    "contratorpedeiro" : 2,
    "submarino":1
}

for nautico in navios.keys():
    tamanho = navios[nautico]

    while True:
        print(f'Insira as informações referentes ao navio {nautico} que possui tamanho {tamanho}')
        linha=int(input("Linha: "))
        coluna=int(input("Coluna: "))
        if nautico!='submarino':
            orientacao=int(input("[1] Vertical [2] Horizontal: "))
            if orientacao==1:
                orientacao='vertical'
            elif orientacao==2:
                orientacao='horizontal'
        else:
            orientacao='vertical'

        if posicao_valida(frota,linha,coluna,orientacao,tamanho)==False:
            print("Esta posição não está válida!")
        
        else:
            frota=preenche_frota(frota, nautico, linha, coluna, orientacao, tamanho)
            break


print(frota)