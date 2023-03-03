

def misplaced_tiles(input_state):
    """
    the number of misplaced tiles for a given state is the heuristic function
    """
    # save the goal state (the ideal state that you want to end up with/the solved puzzle)
    goal_state = [1, 2, 3,
                  4, 5, 6,
                  7, 8, 0]
    # initialize the count as 0, this is the count of misplaced tiles
    number_misplaced_tiles = 0
    # iterate through all positions of the solved AND unsolved puzzles, comparing the values at each index.
    # if the values in each index do NOT match, add 1 to the counter
    for i in range(9):
        # if the current value in the state is not 0 and the numbers from both states don't match, count that is a
        # misplaced tile
        if input_state[i] != 0 and input_state[i] != goal_state[i]:
            number_misplaced_tiles += 1

    return number_misplaced_tiles


# this function changes for formatting of the state, changing it from an array to something that looks like more
# and actual puzzle (in the form of a matrix)
def pretty_print(current_state):
    for i in range(9):
        if i % 3 == 0 and i > 0:
            print("")
        print(str(current_state[i]) + " ", end="")


def next_move(_possible_moves, _position_of_zero, input_state):
    # initiate variable to store the best heuristic value
    # 100000 is arbitrary, it just needed to be really high because we're interested in LOWEST heuristic value
    best_heuristic = 100000
    # initiate_variable to store the best choice for moving forward
    output_state = input_state.copy()

    # iterate through ar, which is all the possible moves that a blank tile (0) can make in the current state. for each
    # of those possible moves, we iterate through all of them to figure out which is the better option
    for i in range(len(_possible_moves)):
        # make a copy of the state to manipulate
        temporary_input_state = input_state.copy()

        # NOTE: to make a move, the action is to swap 0 with the number where you want to move the zero!

        # temp returns 0. p tell us the index where 0 is so all we're doing is choosing the index of the current state
        # that contains 0
        zero_val = temporary_input_state[_position_of_zero]
        # assign the value from the possible move being assessed to the blank space (where the 0 is)
        temporary_input_state[_position_of_zero] = temporary_input_state[_possible_moves[i]]
        # move the blank space (0) to the index of the possible move being assessed
        temporary_input_state[_possible_moves[i]] = zero_val

        #
        temporary_heuristic = misplaced_tiles(temporary_input_state)
        if temporary_heuristic < best_heuristic:
            best_heuristic = temporary_heuristic
            output_state = temporary_input_state.copy()

    return output_state, best_heuristic


# initial state
state = [1, 2, 3,
         0, 5, 6,
         4, 7, 8]
# heuristic function is the number/count of "misplaced" tiles, value is saved in "h" variable
h = misplaced_tiles(state)

Level = 1
print("---Level {} ------".format(str(Level)))
pretty_print(state)
print("\n")
print("Heuristic value(misplaced tiles): {}".format(h))

while h > 0:
    # position of the blank tile, which is 0 in our case
    # we need to know where this is, so we can move it later
    position_of_zero = int(state.index(0))

    # increase the level by 1
    Level += 1

    # this if/elif block determines all possible moves that a blank tile can make FROM ANY index
    if position_of_zero == 0:
        possible_moves = [1, 3]
        state, h = next_move(possible_moves, position_of_zero, state)
    elif position_of_zero == 1:
        possible_moves = [0, 2, 4]
        state, h = next_move(possible_moves, position_of_zero, state)
    elif position_of_zero == 2:
        possible_moves = [1, 5]
        state, h = next_move(possible_moves, position_of_zero, state)
    elif position_of_zero == 3:
        possible_moves = [0, 4, 6]
        state, h = next_move(possible_moves, position_of_zero, state)
    elif position_of_zero == 4:
        possible_moves = [1, 3, 5, 7]
        state, h = next_move(possible_moves, position_of_zero, state)
    elif position_of_zero == 5:
        possible_moves = [2, 4, 8]
        state, h = next_move(possible_moves, position_of_zero, state)
    elif position_of_zero == 6:
        possible_moves = [3, 7]
        state, h = next_move(possible_moves, position_of_zero, state)
    elif position_of_zero == 7:
        possible_moves = [6, 4, 8]
        state, h = next_move(possible_moves, position_of_zero, state)
    elif position_of_zero == 8:
        possible_moves = [5, 7]
        state, h = next_move(possible_moves, position_of_zero, state)

    print("---Level {} ------".format(str(Level)))
    pretty_print(state)
    print("\n")
    print("Heuristic value(misplaced tiles): {}".format(h))
