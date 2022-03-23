import time
import random


def play_game(player_weapon, player_health, monster):
    print_pause("\nEnter 'knock' to knock on the door of the house." +
                "\nEnter 'peek' to peek into the cave.")
    p_move = player_choice(["knock", "peek"])
    if p_move == "knock":
        print_pause(f"\nYou approach the door of the house. You are about " +
                    f"to knock when the door opens and out steps a {monster}!")
        print_pause(f"\nEep! This is the {monster}'s house! The {monster} " +
                    f"attacks you! Your weapon is a {player_weapon}!")
        print_pause("\nEnter 'fight' to fight.\nEnter 'run' to run away.")
        p_move = player_choice(["fight", "run"])
        if p_move == 'fight':
            if player_weapon == "wooden stick":
                return "lost"
            else:
                return "won"
        elif p_move == 'run':
            player_health = player_health - 1
            if player_health > 0:
                print_pause(f"\nYou returned to the open field safely, but " +
                            f"you lost a health point, you now have " +
                            f"{player_health} out of 3 health points")
                return play_game(player_weapon, player_health, monster)
            else:
                return "died"
    elif p_move == "peek":
        if player_weapon == "magical sword of ogoroth":
            print_pause("\nYou peek cautiously into the cave. You've been " +
                        "here before, and gotten all the good stuff. You " +
                        "walk back out to the field.")
        else:
            print_pause("\nYou peek cautiously into the cave. It turns out " +
                        "to be only a very small cave. Your eye catches a " +
                        "glint of metal behind a rock.")
            print_pause("\nYou have found the magical Sword of Ogoroth! You " +
                        "discard your silly wooden stick and take the sword " +
                        "with you. You walk back out to the field.")
            player_weapon = "magical sword of ogoroth"
        return play_game(player_weapon, player_health, monster)


def player_choice(choices):
    while True:
        p_move = input(f'\nWhat would you like to do? Please enter ' +
                       f'"{choices[0]}" or "{choices[1]}": ').lower()
        if p_move in choices:
            return p_move
        print_pause(f'\nYour choice was not valid.')


def game_outcome(outcome, monster):
    if outcome == "won":
        print_pause(f"\nCongratulations, you defeated the {monster} " +
                    "and won the game!")
    elif outcome == "died":
        print_pause("\nYou did your best... but you lost all your " +
                    "health points. You have been defeated!")
    else:
        print_pause(f"\nYou did your best... but your wooden stick " +
                    f"is no match for the {monster}! " +
                    "You have been defeated!")


def start_game():

    # Infinite loop
    while True:

        # Logic to play the game
        monsters = ["Ogre", "wicked Fairie", "Troll"]
        monster = random.choice(monsters)
        player_weapon = "wooden stick"
        player_health = 3
        print_pause("\nYou find yourself standing in an open field, " +
                    "filled with grass and yellow wildflowers.")
        print_pause(f"\nRumor has it that a {monster} is somewhere around " +
                    "here, and has been terrifying the nearby village.")
        print_pause("\nIn front of you is a house. To your right is a dark " +
                    "cave. In your hand you hold a wooden stick.")
        outcome = play_game(player_weapon, player_health, monster)
        game_outcome(outcome, monster)

        # The stop condition
        play_again()


def print_pause(statement, default=2):
    print(statement)
    # time.sleep(default)


def play_again():
    print_pause("\nDo you want to play again? Press 'yes' to play " +
                "again. Press 'no' to end the game")
    play_again = player_choice(["yes", "no"])
    if play_again == 'no':
        print_pause("\nThanks for playing! See you next time.\n")
        exit(0)


if __name__ == '__main__':
    start_game()
