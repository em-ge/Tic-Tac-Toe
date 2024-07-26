import time
import random
import sys
from colorama import Style

example = "\nType a number between 1 to 9\n1 2 3\n4 5 6\n7 8 9\n\n> "


def start():
    print(Style.BRIGHT + "\n\nTicTacToe:\n" + Style.RESET_ALL)
    time.sleep(1)
    print("Type your number, where you want to set the x or o\n\n1 2 3\n4 5 6\n7 8 9")
    print(
        "If you have your item (x or o) in a row, ... or ... you win!\nType 'help' for help\nLet's Go!"
    )


def game_Human():
    output = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    check_Item = "x"
    for i in range(9):
        print(f"It's the turn of {check_Item}.")
        number = input("\nType a number between 1 to 9\n> ")

        while True:
            if number == "help":
                start()

            if number.isalpha():
                print("Please type a number and no letter!")
                number = input("\nType a number between 1 to 9\n> ")
                continue

            number = int(number)

            if number >= 10:
                print("Please type a number with a free Field!")
                number = input("\nType a number between 1 to 9\n> ")
                continue
            if (
                output[number - 1] == "\x1b[1mo\x1b[0m"
                or output[number - 1] == "\x1b[1mx\x1b[0m"
            ):
                print("Please select an empty Field")
                number = input("\nType a number between 1 to 9\n> ")
                continue
            break

        output[number - 1] = Style.BRIGHT + check_Item + Style.RESET_ALL

        game = f"\n{output[0]}  {output[1]}  {output[2]}\n{output[3]}  {output[4]}  {output[5]}\n{output[6]}  {output[7]}  {output[8]}\n\n"

        print(game)
        time.sleep(1)

        if output[0] == output[1] == output[2]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[3] == output[4] == output[5]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[6] == output[7] == output[8]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[0] == output[3] == output[6]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[1] == output[4] == output[7]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[2] == output[5] == output[8]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[0] == output[4] == output[8]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[2] == output[4] == output[6]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break

        if check_Item == "x":
            check_Item = "o"
        else:
            check_Item = "x"

    print("This is a draw!")


def game_AI():
    opportunity_to_win = False
    output = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        print("It's your turn")
        check_Item = "x"
        number = input("\nType a number between 1 to 9\n> ")

        while True:
            if number == "help":
                start()

            if number.isalpha():
                print("Please type a number and no letter!")
                number = input("\nType a number between 1 to 9\n> ")
                continue

            number = int(number)

            if number >= 10:
                print("Please type a number with a free Field!")
                number = input("\nType a number between 1 to 9\n> ")
                continue
            if (
                output[number - 1] == "\x1b[1mo\x1b[0m"
                or output[number - 1] == "\x1b[1mx\x1b[0m"
            ):
                print("Please select an empty Field")
                number = input("\nType a number between 1 to 9\n> ")
                continue
            break

        output[number - 1] = Style.BRIGHT + check_Item + Style.RESET_ALL

        game = f"\n{output[0]}  {output[1]}  {output[2]}\n{output[3]}  {output[4]}  {output[5]}\n{output[6]}  {output[7]}  {output[8]}\n\n"

        print(game)
        time.sleep(1)

        if output[0] == output[1] == output[2]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            opportunity_to_win = True
            break
        elif output[3] == output[4] == output[5]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            opportunity_to_win = True
            break
        elif output[6] == output[7] == output[8]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            opportunity_to_win = True
            break
        elif output[0] == output[3] == output[6]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            opportunity_to_win = True
            break
        elif output[1] == output[4] == output[7]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            opportunity_to_win = True
            break
        elif output[2] == output[5] == output[8]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            opportunity_to_win = True
            break
        elif output[0] == output[4] == output[8]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            opportunity_to_win = True
            break
        elif output[2] == output[4] == output[6]:
            time.sleep(1)
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            opportunity_to_win = True
            break

        print(f"It's the turn of AI.")
        check_Item = "o"
        ai_choice = random.choice(output)

        if opportunity_to_win == True:
            pass

        while True:
            if ai_choice == "\x1b[1mo\x1b[0m" or ai_choice == "\x1b[1mx\x1b[0m":
                ai_choice = random.choice(output)
                continue

            if (
                output[ai_choice - 1] == "\x1b[1mo\x1b[0m"
                or output[ai_choice - 1] == "\x1b[1mx\x1b[0m"
            ):
                ai_choice = random.choice(output)
                continue
            break

        time.sleep(1)
        output[ai_choice - 1] = Style.BRIGHT + check_Item + Style.RESET_ALL

        game = f"\n{output[0]}  {output[1]}  {output[2]}\n{output[3]}  {output[4]}  {output[5]}\n{output[6]}  {output[7]}  {output[8]}\n\n"

        print(game)
        time.sleep(1)

        if output[0] == output[1] == output[2]:
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[3] == output[4] == output[5]:
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[6] == output[7] == output[8]:
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[0] == output[3] == output[6]:
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[1] == output[4] == output[7]:
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[2] == output[5] == output[8]:
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[0] == output[4] == output[8]:
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break
        elif output[2] == output[4] == output[6]:
            print(f"{Style.BRIGHT}{check_Item} wins!{Style.RESET_ALL}")
            break

        if output[0:8] == "\x1b[1mo\x1b[0m" and output[0:8] == "\x1b[1mx\x1b[0m":
            time.sleep(1)
            print("This is a draw")
            break
    print("This is a draw!")


def check_choice():
    choice = input(
        "Do you want to play aganst an AI or a human?\nType 'AI' to play aganst a AI or 'human' to play angainst a human.\n> "
    )
    if choice == "AI":
        print("Ok, Let's Go!")
        game_AI()
    elif choice == "human":
        print("Ok, Let's Go!")
        game_Human()
    else:
        while True:
            print("Error, please type a right answer")
            choice = input(
                "Do you want to play aganst an AI or a human?\nType 'AI' to play aganst a AI or 'human' to play angainst a human.\n> "
            )
            if choice == "AI":
                print("Ok, Let's Go!")
                game_AI()
                break
            elif choice == "human":
                game_Human()
                print("Ok, Let's Go!")
                break


while True:
    start()
    check_choice()
    answer = input(
        "\n\nDo you want to play again? Then Type 'restart'. Else Type 'exit'\n> "
    )
    if answer == "exit":
        print("Ok, the Program will end. Bye\n")
        sys.exit("\n")
    elif answer == "restart":
        print("Ok, Programm wil restart")
    else:
        while True:
            print("Error, please type a right answer")
            answer = input(
                "\n\nDo you want to play again? Then Type 'restart'. Else Type 'exit'\n> "
            )
            if answer == "exit":
                print("Ok, the Program will end. Bye\n")
                sys.exit("\n")
            elif answer == "restart":
                print("Ok, Programm will restart")
                break
