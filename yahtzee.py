"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    hand = sorted(hand)
    max_score = 0
    current_value = hand[0]
    for i in range(len(hand)-1):
        if hand[i] == hand[i+1]:
            current_value += hand[i+1]
        else:
            if current_value > max_score:
                max_score = current_value
            current_value = hand[i+1]
    return max_score if max_score > current_value else current_value


def expected_value(held_dice, num_die_sides, num_free_dice):
    sides = []
    for i in range(num_die_sides):
        sides.append(i+1)
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.
    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled
    Returns a floating point expected value
    """
    sum_of_scores =0.0
    dice_space = gen_all_sequences(sides, num_free_dice)
    for hand in dice_space:
        sum_of_scores += score(hand + held_dice)
    expected_value = sum_of_scores / len(dice_space)
    return expected_value

def get_comb(hand, ln):
    res = set ([()])
    for i in range(ln):
        temp_set = set()
        for j in res:
            for k in range(i+1):
                new_seq = list(j) + list([hand[i]])
                res.add(tuple(new_seq))
    return res
#print sorted(get_comb((1,2,3,4),4))
def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    res = set([])
    for i in range(len(hand)):
        tmp = gen_all_sequences(hand, i)
        res = res.union(tmp)
    return res
        



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    best_hold = ()
    exp_value = 0
    all_holds = get_comb(hand, len(hand))
    print all_holds
    for hold in all_holds:
        new_ex = expected_value(hold, 6, 4 - len(hold))
        print new_ex, hold
        if new_ex > exp_value:
            exp_value = new_ex
            best_hold = hold
        
    return (exp_value, best_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (3,3,3,3)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
#print expected_value((),6,6)
run_example()

#print gen_all_holds([1,1,1,5])
#print gen_all_sequences((1,2,3,4,5,6),3)
#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    



