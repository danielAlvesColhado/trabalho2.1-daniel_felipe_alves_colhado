from time import sleep

from jogo.jogadores import criar_jogadores, sortear_jogador_inicial, jogador_ataque_vez
from jogo.trocar_vez import trocar_vez
from telas.jogo import pedir_onde_por_navios, batalha
from jogo.tabuleiro import cria_tabuleiro, tabuleiro_ataque, tabuleiro_posicionar
from telas.jogadores import placar, buscar_nome_jogador_da_vez
from telas.mensagens import mensagem_inicializacao, mensagem_inicio_posic
from telas.tabuleiro import mostrar_tabuleiro, mostrar_tabuleiro_final

jogador1 = None
jogador2 = None


def vencedor(jogador1, jogador2, tabuleiros):
    if jogador1['pontos'] == 5:
        print(f'Parabens {jogador1["nome"]} Você ganhou a batalha! acertou os 5 navios do {jogador2["nome"]}!!')
        print('')
        mostrar_tabuleiro_final(tabuleiros)
        return False
    elif jogador2['pontos'] == 5:
        print(f'Parabens {jogador2["nome"]} Você ganhou a batalha! acertou os 5 navios do {jogador1["nome"]}!!')
        print('')
        mostrar_tabuleiro_final(tabuleiros)
        return False
    else: return True


def rodar_programa():
    mensagem_inicializacao()
    jogador1, jogador2 = criar_jogadores()
    jogador1, jogador2 = sortear_jogador_inicial(jogador1, jogador2)
    placar(jogador1, jogador2)
    tabuleiros = cria_tabuleiro(jogador1), cria_tabuleiro(jogador2)
    mostrar_tabuleiro(tabuleiros)
    mensagem_inicio_posic(buscar_nome_jogador_da_vez(jogador1, jogador2))
    pedir_onde_por_navios(buscar_nome_jogador_da_vez(jogador1, jogador2), tabuleiro_posicionar(jogador1, tabuleiros))
    trocar_vez(jogador1, jogador2)
    mensagem_inicio_posic(buscar_nome_jogador_da_vez(jogador1, jogador2))
    pedir_onde_por_navios(buscar_nome_jogador_da_vez(jogador1, jogador2), tabuleiro_posicionar(jogador1, tabuleiros))
    trocar_vez(jogador1, jogador2)
    while vencedor(jogador1, jogador2, tabuleiros):
        mostrar_tabuleiro(tabuleiros)
        batalha(jogador_ataque_vez(jogador1, jogador2), buscar_nome_jogador_da_vez(jogador1, jogador2), tabuleiro_ataque(jogador1, tabuleiros), jogador1, jogador2)
        sleep(3)


rodar_programa()
