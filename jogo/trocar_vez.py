
def trocar_vez(jogador1, jogador2):
    if jogador1['vez']:
        jogador2['vez'] = True
        jogador1['vez'] = False
    else:
        jogador2['vez'] = False
        jogador1['vez'] = True