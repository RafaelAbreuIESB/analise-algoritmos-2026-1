import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    i, j = action
    if board[i][j] is not EMPTY:
        raise Exception("Ação inválida")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    # Checar linhas e colunas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    # Checar diagonais
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None

def terminal(board):
    # Se alguém ganhou ou não existem mais espaços vazios, o jogo acabou
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

def utility(board):
    win = winner(board)
    if win == X: return 1
    if win == O: return -1
    return 0

def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)
    
    if current_player == X:
        return max(
            [(min_value(result(board, a)), a) for a in actions(board)],
            key=lambda x: x[0]
        )[1]
    else:
        return min(
            [(max_value(result(board, a)), a) for a in actions(board)],
            key=lambda x: x[0]
        )[1]

def max_value(board):
    if terminal(board): return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board): return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v