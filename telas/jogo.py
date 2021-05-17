from jogo.trocar_vez import trocar_vez
from telas.jogadores import placar
from telas.mensagens import vez_de_jogar


def pedir_onde_por_navios(jogador, tabuleiro):
    for r in range(1, 6):
        linha_navio = int(input(f'{jogador} Qual linha deseja posicionar o {r}° navio? '))
        coluna_navio = int(input('agora digite a coluna: '))
        print('')
        tabuleiro[linha_navio][coluna_navio] = 'navio'


def batalha(jogador, nome_jogador, tabuleiro, jogador1, jogador2):
    vez_de_jogar(jogador1, jogador2)
    print(f'Jogador{jogador["id"]} {nome_jogador} Faça sua jogada!')
    ataque_linha = int(input(f'{nome_jogador} Informe qual linha do campo inimigo deseja fazer o ataque: '))
    ataque_coluna = int(input(f'{nome_jogador} Agora informe a coluna: '))
    if tabuleiro[ataque_linha][ataque_coluna] == 'navio':
        tabuleiro[ataque_linha][ataque_coluna] = 'exnavio'
        jogador['pontos'] += 1
        print('')
        print(f'Parabens jogador {nome_jogador}!! Você acertou um Navio do inimigo!! ganhou um ponto')
        print('')
    elif tabuleiro[ataque_linha][ataque_coluna] == 'exnavio':
        print('')
        print('Voce já acertou um navio nesta posiçao! agora ele não vale mais, ganhou nada! segue o jogo...')
        print('')
    else:
        print('')
        print('Ataque falhou, segue o jogo...')
        print('')

    trocar_vez(jogador1, jogador2)
    placar(jogador1, jogador2)
