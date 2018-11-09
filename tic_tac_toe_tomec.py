def Vod(game_board, symbol): #���s�𔻕ʂ���֐�
    #������
    for i in range(4):
        if ((game_board[i][0] == symbol or game_board[i][0] == 'T') and (game_board[i][1] == symbol or game_board[i][1] == 'T')
            and (game_board[i][2] == symbol or game_board[i][2] == 'T') and (game_board[i][3] == symbol or game_board[i][3] == 'T')):
            return True
    #�c����
    for j in range(4):
        if ((game_board[0][j] == symbol or game_board[0][j] == 'T') and (game_board[1][j] == symbol or game_board[1][j] == 'T')
            and (game_board[2][j] == symbol or game_board[2][j] == 'T') and (game_board[3][j] == symbol or game_board[3][j] == 'T')):
            return True
    #�΂ߕ���(�E�オ��)
    if ((game_board[0][3] == symbol or game_board[0][3] == 'T') and (game_board[1][2] == symbol or game_board[1][2] == 'T')
        and (game_board[2][1] == symbol or game_board[2][1] == 'T') and (game_board[3][0] == symbol or game_board[3][0] == 'T')):
        return True
    #�΂ߕ���(�E������)
    if ((game_board[0][0] == symbol or game_board[0][0] == 'T') and (game_board[1][1] == symbol or game_board[1][1] == 'T')
        and (game_board[2][2] == symbol or game_board[2][2] == 'T') and (game_board[3][3] == symbol or game_board[3][3] == 'T')):
        return True
    #�ǂ�ɂ��Y�����Ȃ����False
    return False


def draw(game_board): #���������𔻕ʂ���֐�
    for i in range(4):
        for j in range(4):
            if (game_board[i][j] == '.'):
                return True
    return False


def solve(game_board):
    if Vod(game_board, 'O'): #game_board��symbol(= 'O')�ɑ΂��ATrue(��)False(��)��Ԃ�
        result = 'O won'
    elif Vod(game_board, 'X'): #game_board��symbol(= 'X')�ɑ΂��ATrue(��)False(��)��Ԃ�
        result = 'X won'
    elif draw(game_board): #game_board�ɑ΂��A1�ł�'.'�������draw��Ԃ�
        result = 'Game has not completed'
    else:
        result = 'Draw'
    return result


def answer(input_file_name,output_file_name):
    input_file = open(input_file_name)
    output_file = open(output_file_name, 'w')
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        game_board =[]
        for i in range(4):
            one_row = []
            for j in range(4):
                one_row += input_file.read(1)
            game_board += [one_row]
            input_file.read(1)
        input_file.read(1)
        output_file.write('Case #{0}: {1}\n'.format(case_number,solve(game_board)))
        #print(game_board)
    input_file.close()
    output_file.close()
    return