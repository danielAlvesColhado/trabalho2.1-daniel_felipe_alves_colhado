def cria_tabuleiro(jogador):
    tabuleiro = {
        'jogador': jogador,
        'area': []
    }
    for i in range(0, 10):
        linha = []
        for j in range(0, 10):
            linha.append(None)
        tabuleiro['area'].append(linha)

    return tabuleiro

def tabuleiro_posicionar(jogador1, tabuleiros):
    if jogador1['vez']:
        tabuleiro = tabuleiros[0]['area']
    else:
        tabuleiro = tabuleiros[1]['area']
    return tabuleiro


def tabuleiro_ataque(jogador1, tabuleiros):
    if jogador1['vez']:
        tabuleiro = tabuleiros[1]['area']
    else :
        tabuleiro = tabuleiros[0]['area']
    return tabuleiro