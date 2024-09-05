Ai"""
Tic Tac Toe Player
"""

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
    """
    Returns player who has the next turn on a board.
    """
    # to kow how mane X and O are there
    X_count = 0
    O_count = 0

    # three options init, end or middle game
    if board == initial_state():
        return X
    elif terminal(board):
        return EMPTY

    # to count
    for row in board:
        if X in row:
            X_count += 1
        if O in row:
            O_count += 1

    # select the next one
    if X_count > O_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # game being played
    actions_set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if EMPTY == board[i][j]:
                actions_set.add((i, j))

    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # unpacked
    i, j = action
    # In case the action is invalid
    if action not in actions(board):
        raise Exception("Invalid Action")

    # copy of the board
    board_copy = copy.deepcopy(board)

    # move with the actual player
    board_copy[i][j] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Rows
    for row in board:
        if row[0] is not EMPTY and row[0] == row[1] == row[2]:
            return row[0]

    # Cols
    for col in range(3):
        if board[0][col] is not EMPTY and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Diagonal 1
    if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    # Diagonal 2
    if board[0][2] is not EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Winner
    if winner(board) is not None:
        return True

    # Tie
    if not any(EMPTY in row for row in board):
        return True

    # Continue
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    best_action = None

    if current_player == X:  # Maximizing player
        best_value = -math.inf

        for action in actions(board):
            value = minimax(result(board, action))
            if value is None:  # Just in case it returns None, treat as 0 (it's a terminal state)
                value = utility(board)
                if value > best_value:
                    best_value = value
                    best_action = action

    else:  # Minimizing player (O)
        best_value = math.inf

        for action in actions(board):
            value = minimax(result(board, action))
            if value is None:  # Just in case it returns None, treat as 0 (it's a terminal state)
                value = utility(board)
                if value < best_value:
                    best_value = value
                    best_action = action

    return best_action
