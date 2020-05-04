import random
finished_game = ["x", 1, 2, 3, 4, 5, 6, 7, 8]

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
    new_game = finished_game.copy()
    random.shuffle(new_game)
    return new_game


def play_turn(game):
    return


def play_game(game, past_state_list):
    if game_finished(game):
        return True

    if game in past_state_list:
        return False

def move(past_game_states, direction):
    game = past_game_states[-1]
    index = game.index("x")

    x_row = index // 3
    x_col = index % 3

    if direction == UP:
        if x_row == 0:
            return False
        new_game = list(game)
        new_game[x_row * 3 + x_col] = [(x_row - 1) * 3 + x_col]
        new_game[(x_row - 1) * 3 + x_col] = "x"



def game_finished(game):
    return game == finished_game


def mai():
    game = create_game()
    while not game_finished(game):
        play_turn(game)

    print(game)


if __name__ =="__main__":
    main()