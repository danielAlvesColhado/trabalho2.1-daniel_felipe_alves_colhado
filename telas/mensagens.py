from telas.jogadores import buscar_nome_jogador_da_vez


def mensagem_criacao_jogador(jogador):
    print(f'criacao do {jogador}!')


def mensagem_inicializacao():
    print('=== iniciando jogo ==')
    print('== batalha naval ==')


def mensagem_inicio_posic(jogador):
    print(f'{jogador} Agora você vai posicionar seus barcos!')
    print('Peça pro seu adversario olhar para o lado')


def vez_de_jogar(jogador1, jogador2):
    print(f'agora a vez de jogar é de {buscar_nome_jogador_da_vez(jogador1, jogador2)}')