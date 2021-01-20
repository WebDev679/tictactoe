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
    if board == initial_state():
        return X

    noOfX = 0
    noOfO = 0
    for row in board:
        for block in row:
            if block == X:
                noOfX += 1
            elif block == O:
                noOfO += 1
            else:
                pass
    if noOfX + noOfO == 9:
        return None
    else:
        player = X if noOfX == noOfO else O
        return player

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """ 

    actions = []
    for i, row in enumerate(board):
        for j, block in enumerate(row):
            if block == EMPTY:
                actions.append((i, j))
            else:
                pass
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardcopy = copy.deepcopy(board)
    for i, row in enumerate(boardcopy):
        for j, block in enumerate(row):
            if action == (i, j):
                boardcopy[i][j] = player(boardcopy)
    return boardcopy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # def winning_combinations(n):
    #     for r in range(n):
    #     yield [(r, c) for c in range(n)]
    # for c in range(n):
    #     yield [(r, c) for r in range(n)]
    # yield [(i, i) for i in range(n)]
    # yield[(i, n-1-i) for i in range(n)]
    winCoords = [[(0, 0), (0, 1), (0, 2)], 
                [(1, 0), (1, 1), (1, 2)], 
                [(2, 0), (2, 1), (2, 2)], 
                [(0, 0), (1, 0), (2, 0)], 
                [(0, 1), (1, 1), (2, 1)], 
                [(0, 2), (1, 2), (2, 2)], 
                [(0, 0), (1, 1), (2, 2)],
                [(0, 2), (1, 1), (2, 0)],
                ]
    Xs = []
    Os = []
    for i, row in enumerate(board):
        for j, block in enumerate(row):
            if board[i][j] == X:
                Xs.append((i, j))
            elif board[i][j] == O:
                Os.append((i, j))
            else:
                pass
    for coord in winCoords:
        coordSet = set(coord)
        xs = set(Xs)
        os = set(Os)
        if len(coordSet.intersection(xs)) == 3:
            winner = X
            break
        elif len(coordSet.intersection(os)) == 3:
            winner = O
            break
        else:
            winner = None
    return winner



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    emptyCounter = 0
    for row in board:
        emptyCounter += row.count(EMPTY)
    if emptyCounter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        bestScoremax = -math.inf
        for action in actions(board):
            score = maxPlayer(result(board, action))
            if score > bestScoremax:
                bestScoremax = score
                bestMove = action
    else:
        bestScoremin = math.inf
        for action in actions(board):
            score = minPlayer(result(board, action))
            if score < bestScoremin:
                bestScoremin = score
                bestMove = action
    return bestMove

def maxPlayer(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minPlayer(result(board, action)))
    return v

def minPlayer(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxPlayer(result(board, action)))
    return v