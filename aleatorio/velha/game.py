import numpy as np
import random

board = np.array( [ [7,8,9],
                    [4,5,6],
                    [1,2,3] ] )

def check_winner(board):
    ''' Funcao para identificar se alguém venceu o jogo, e quem.'''
    linhas = board.sum(axis=1)
    colunas = board.sum(axis=0)
    diag_1 = board.trace()
    diag_2 = board[::-1].trace()

    if 30 in linhas or 30 in colunas or 30 == diag_1 or 30 == diag_2:
        return "X"
    elif 300 in linhas or 300 in colunas or 300 == diag_1 or 300 == diag_2:
        return "O"
    else:
        return None
    
def show_board( board ):
    line_1 = '+---+---+---+'
    line_2 = '|{0:^3}|{1:^3}|{2:^3}|'
    for i in range(board.shape[0]):
        list_str = []
        for j in board[i]:
            if j == 100:
                list_str.append( "O" )
            elif j == 10:
                list_str.append( "X" )
            else:
                list_str.append(j)
        print(line_1)
        print(line_2.format( *list_str ))
    print(line_1)

def make_play( board, player ):
    print(chr(27) + "[2J")
    show_board(board)
    str_player = "X" if player == 10 else "O"
    print("É a vez do jogodador", str_player)
    op = -1
    while op not in board:
        op = int( input("Escolha o número para fazer jogada: ") )
    board[ np.where( board == op) ] = player

players = [10,100]
random.shuffle( players)
players *= 10
for p in players:
    make_play(board, p)
    winner = check_winner(board)
    if winner is None:
        pass
    else:
        print(chr(27) + "[2J")
        print("Parabens, ", winner, ". Você Ganhou!", sep='')
        show_board(board)
        break
