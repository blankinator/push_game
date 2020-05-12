import random
import sys
FINISHED_GAME = ["x", 1, 2, 3, 4, 5, 6, 7, 8]

"""
x 1 2
3 4 5
6 7 8
"""

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def create_game():
    new_game = list(FINISHED_GAME)
    random.shuffle(new_game)
    return new_game


def game_state_valid(game_state, past_game_states):
    for level in past_game_states:
        for past_game_state in level:
            if game_state == past_game_state:
                return False
    return True


def expand_level(past_game_states):
    new_level = list()
    for game in past_game_states[-1]:
        sub_nodes = filter(lambda node: game_state_valid(node, past_game_states),
                           [move(game, UP),
                            move(game, RIGHT),
                            move(game, DOWN),
                            move(game, LEFT)])
        new_level.extend(sub_nodes)

    for game in new_level:
        if game_finished(game):
            print_game(game)
            return True

    past_game_states.append(new_level)
    print(len(past_game_states))
    return expand_level(past_game_states)


def print_game(game):
    print("-----")
    print('{}|{}|{}'.format(*game[0:3]))
    print("-----")
    print('{}|{}|{}'.format(*game[3:6]))
    print("-----")
    print('{}|{}|{}'.format(*game[6:9]))
    print("-----")


def move(game, direction):
    index = game.index("x")
    x_row = get_row(index)
    x_col = get_col(index)

    if direction == UP:
        if x_row == 0:
            return game
        new_game = game[:]
        new_game[index] = game[get_index(x_row - 1, x_col)]
        new_game[get_index(x_row - 1, x_col)] = "x"
        #  print_game(new_game)
        return new_game
    elif direction == RIGHT:
        if x_col == 2:
            return game
        new_game = game[:]
        new_game[index] = game[get_index(x_row, x_col + 1)]
        new_game[get_index(x_row, x_col + 1)] = "x"
        #  print_game(new_game)
        return new_game
    elif direction == DOWN:
        if x_row == 2:
            return game
        new_game = game[:]
        new_game[index] = game[get_index(x_row + 1, x_col)]
        new_game[get_index(x_row + 1, x_col)] = "x"
        #  print_game(new_game)
        return new_game
    elif direction == LEFT:
        if x_col == 0:
            return game
        new_game = game[:]
        new_game[index] = game[get_index(x_row, x_col - 1)]
        new_game[get_index(x_row, x_col - 1)] = "x"
        #  print_game(new_game)
        return new_game


def get_index(row, col):
    return (row * 3) + col


def get_row(index):
    return index // 3


def get_col(index):
    return index % 3


def game_finished(game):
    return game == FINISHED_GAME


def play_game():
    game = create_game()
    print_game(game)
    return expand_level([[game]])


def main():
    play_game()
    print("Done")


if __name__ == "__main__":
    main()
