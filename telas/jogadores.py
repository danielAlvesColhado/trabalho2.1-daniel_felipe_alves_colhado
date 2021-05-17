def pedir_nome():
    return input('Informe seu nome: ')

def placar(jogador1, jogador2):
    print('')
    print('== placar ==')
    nomej1, pontosj1, nomej2, pontosj2 = jogador1.get('nome'), jogador1.get('pontos'),\
                                         jogador2.get('nome'), jogador2.get('pontos')

    print(f"{nomej1} esta com {pontosj1} pontos e {nomej2} esta com {pontosj2} pontos")
    print('')


def buscar_nome_jogador_da_vez(jogador1, jogador2):
    nome_jogador_da_vez = jogador1.get('nome') if jogador1.get('vez') else jogador2.get('nome')
    return nome_jogador_da_vez






