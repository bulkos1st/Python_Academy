import os

"""
Python Academy Project 2 - Tic Tac Toe
"""

WELCOME_TEXT = """
Welcome to Tic Tac Toe
GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row
You can exit at any time by pressing 'q'

Let's start the game
"""

playgrid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ROW_SEPARATOR = "-----"
ROW_TEMPLATE = "{}|{}|{}"

WIN_COMBINATIONS = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},  # horizontal
                    {1, 4, 7}, {2, 5, 8}, {3, 6, 9},  # vertical
                    {1, 5, 9}, {3, 5, 7}  # diagonal
                    ]

PLAYERS = ("X", "O")
START_PLAYER_INDEX = 0
player_choices = {0: [], 1: []}


def switch_player_index(player_index: bool) -> bool:
    return not player_index


def print_playgrid(grid: list, row_template: str, row_separator: str, winner: bool, message="") -> None:
    """
    Loop and fill template with 3 items extracted from slice of 3 items from play grid in each iteration.
    """
    os.system('clear')
    print("Tic Tac Toe")
    for start_value in range(0, 9, 3):
        print(row_separator, row_template.format(*grid[start_value:start_value + 3]), sep="\n")
    print(row_separator, "\n")

    if len(set(playgrid)) == 2:
        print("Game finished no winner!")
    elif winner:
        print(f"Congratulations player {PLAYERS[player_index]} WON!")
    else:
        print(message)


def player_is_winner(win_combinations: list, player_turns: dict, current_player_index: int) -> bool:
    """
    Player can win after 3 turns, if less then 2 turns made return False.
    Check if all numbers from any win combination are presented in players choices, if yes return True.
    """
    if len(player_turns[current_player_index]) < 3:
        return False

    for win_combination in win_combinations:
        for number in win_combination:
            if number not in player_turns[current_player_index]:
                break
        else:
            return True
    else:
        return False


# def is_winner(win_combinations: list, player_turns: dict, current_player_index: int):
#     """
#     Player can win after 3 turns, if less then 2 turns made return False.
#     Check if all numbers from any win combination are presented in players choices, if yes return True.
#     """
#     if len(player_turns[current_player_index]) < 3:
#         return False
#
#     for win_combination in win_combinations:
#         num1, num2, num3 = win_combination
#         if num1 not in player_turns[current_player_index]:
#             continue
#         elif num2 not in player_turns[current_player_index]:
#             continue
#         elif num3 not in player_turns[current_player_index]:
#             continue
#         else:
#             return True
#     else:
#         return False


os.system('clear')
print(WELCOME_TEXT)
input("Press enter to continue")
player_index = START_PLAYER_INDEX
game_winner = False
message = ""
while not game_winner and len(set(playgrid)) != 2:
    print_playgrid(playgrid, ROW_TEMPLATE, ROW_SEPARATOR, game_winner, message)
    message = ""
    user_input = input(f"Player {PLAYERS[player_index]} turn. Select position on grid to place your mark: ")

    # Quit
    if user_input == "q":
        print("You closed game")
        exit()

    # Valid input
    elif user_input.isnumeric() and int(user_input) in range(1, 10):
        # check if field not taken
        if playgrid[int(user_input) - 1] in PLAYERS:
            message = f"Position {user_input} already taken, try again please."
            continue

        playgrid[int(user_input) - 1] = PLAYERS[player_index]
        player_choices[player_index].append(int(user_input))

        if not (game_winner := player_is_winner(WIN_COMBINATIONS, player_choices, player_index)):
            player_index = switch_player_index(player_index)

    # invalid input
    else:
        message = f"Input '{user_input}' not valid, try again please."
        continue

else:
    print_playgrid(playgrid, ROW_TEMPLATE, ROW_SEPARATOR, game_winner)
