"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 50      # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = -1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board,player):
    while board.check_win() == None:
        empty_squares = board.get_empty_squares()
        square = random.choice(empty_squares)
        board.move(square[0],square[1], player)
        player = provided.switch_player(player) 
def mc_update_scores(scores,board,player):
    if board.check_win() == "DRAW":
        return
    elif board.check_win() == player:
    
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if player == board.square(row,col):
                    scores[row][col] += SCORE_CURRENT
                else:
                    scores[row][col] += SCORE_OTHER
    else:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if player == board.square(row,col):
                    scores[row][col] -= SCORE_CURRENT
                else:
                    scores[row][col] -= SCORE_OTHER
        
def get_best_move(board,scores):
    empty_squares = board.get_empty_squares()
    #print empty_squares
    maximum = -20
    coord = ()
    for square in empty_squares:
        if scores[square[0]][square[1]] > maximum:
            maximum = scores[square[0]][square[1]]
            coord = square
    if coord == None:
        return (0,0)
    return coord
def mc_move(board,player,trials):
    scores = [[0 for i in range(3)] for j in range(3)]
    for i in range(trials):
        b = board.clone()
        mc_trial(b, player)
        mc_update_scores(scores, b, player)
        print 'Score', scores
    return get_best_move(board, scores)
    
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

