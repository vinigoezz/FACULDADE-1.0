#3. Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
#ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
#um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
#informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
#rodada.
valores = [1, 2, 3, 4, 5]
palpite_player1 = str(input('Deseja escolher par ou ímpar? [JOGADOR 1]: '))
num_player1 = int(input('escolha um número de 1 a 5: '))
palpite_player2 = str(input('Deseja escolher par ou ìmpar? [JOGADOR 2]: '))
num_player2 = int(input('Escolha um número de 1 a 5: '))
if num_player1 not in valores or num_player2 not in valores:
    print('Número inválido. Rodada encerrada.')
soma = num_player1 + num_player2
pontuação_rodada = 'par' if soma % 2 == 0 else 'ímpar'
if pontuação_rodada == palpite_player1:
    print('jogador 1 venceu!!!')
elif pontuação_rodada == palpite_player2:
    print('jogador 2 vencu a rodada!!!')
else:
    print('empate!!!')

