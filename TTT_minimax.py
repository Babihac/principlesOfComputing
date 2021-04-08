"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(150)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}
board = provided.TTTBoard(3)
board.move(2,1,provided.PLAYERX)
board.move(1,2,provided.PLAYERX)
board.move(0,1,provided.PLAYERO)
board.move(1,1,provided.PLAYERO)
#board.move(2,0,provided.PLAYERO)
def max_key(lst, key):
    """Adds a keyword argument to the max function."""
    new_lst = map(key, lst)
    print "printing new list", new_lst
    for idx, val in enumerate(lst):
        if new_lst[idx] == max(new_lst):
            return val
def xxx(lst, player):
    new_list = map(lambda x: lst[x] * player,lst)
    for i,j in enumerate(lst):
        if new_list[i] == max(new_list):
            return j
def switch_player(player):
    if player == provided.PLAYERX:
        return provided.PLAYERO
    return provided.PLAYERX
print board.__str__()
def mm_move(board, player):
    if board.check_win():
        return SCORES[board.check_win()], (-1, -1)
    board_clone = board.clone()
    empty_squares = board.get_empty_squares()
    results = {}
    pos = []
    for square in empty_squares:
        board_clone = board.clone()
        board_clone.move(square[0],square[1], player)
        res = mm_move(board_clone, switch_player(player))
        #print results
        if res[0] == SCORES[player]:
            return SCORES[player],square
        results[square] = res[0]
    #best_move = max_key(results,
     #   lambda x: SCORES[player] * results[x])
    best_move = xxx(results, SCORES[player])
    return results[best_move], best_move
    return best
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
print mm_move(board, provided.PLAYERX)
