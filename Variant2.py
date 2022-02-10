def stack_show_v2(x):
    a = x // 10
    b = "# " * 10 + "\n"
    c = "# " * (x % 10) + "\n"
    d = b * a + c
    return d


def main_gameplay(play, player1, player2):
    while play:
        turns = True
        stacks = input("Enter amount of stacks : ")
        while not stacks.isnumeric():
            stacks = input("Invalid input, try again : ")
        stacks = int(stacks)
        playing_stones = input("Enter amount of playing stones : ")
        while not playing_stones.isnumeric():
            playing_stones = input("Invalid input, try again : ")
        playing_stones = int(playing_stones)

        stack_register = []
        for i in range(0, stacks):
            stack_register.append(playing_stones)

        print("")

        while turns:
            print(f"{player1}'s turn")
            for i in range(0, stacks):
                print(f"{stack_register[i]} stones on stack {i + 1}")
                print(stack_show_v2(stack_register[i]))
            stack_choice = input(f"Enter number of stack from which {player1} takes stones : ")
            while not stack_choice.isnumeric() or int(stack_choice) > stacks or int(stack_choice) < 1:
                stack_choice = input("Invalid input, try again : ")
            while stack_register[int(stack_choice) - 1] == 0:
                stack_choice = input("Invalid input, try again : ")
            stack_choice = int(stack_choice)
            move = input(f"Enter amount of stones {player1} takes from the stack : ")
            while not move.isnumeric():
                move = input("Invalid input, try again : ")
            while stack_register[stack_choice - 1] - int(move) < 0 or (move != "1" and move != "2" and move != "3"):
                move = input("Invalid input, try again : ")
            move = int(move)
            print("")
            stack_register[stack_choice - 1] -= move

            if all([a == 0 for a in stack_register]):
                print(f"!!! congrats {player1} wins !!!\n")
                play_again = input("Do you want to play again? : ")
                while play_again != "yes" and play_again != "y" and play_again != "no" and play_again != "n":
                    play_again = input("Invalid input, try again : ")
                if play_again == "no" or play_again == "n":
                    play = False
                break

            print(f"{player2}'s turn")
            for i in range(0, stacks):
                print(f"{stack_register[i]} stones on stack {i + 1}")
                print(stack_show_v2(stack_register[i]))
            stack_choice = input(f"Enter number of stack from which {player2} takes stones : ")
            while not stack_choice.isnumeric() or int(stack_choice) > stacks or int(stack_choice) < 1:
                stack_choice = input("Invalid input, try again : ")
            while stack_register[int(stack_choice) - 1] == 0:
                stack_choice = input("Invalid input, try again : ")
            stack_choice = int(stack_choice)
            move = input(f"Enter amount of stones {player2} takes from the stack : ")
            while not move.isnumeric():
                move = input("Invalid input, try again : ")
            while stack_register[stack_choice - 1] - int(move) < 0 or (move != "1" and move != "2" and move != "3"):
                move = input("Invalid input, try again : ")
            move = int(move)
            print("")
            stack_register[stack_choice - 1] -= move

            if all([a == 0 for a in stack_register]):
                print(f"!!! congrats {player2} wins !!!\n")
                play_again = input("Do you want to play again? : ")
                while play_again != "yes" and play_again != "y" and play_again != "no" and play_again != "n":
                    play_again = input("Invalid input, try again : ")
                if play_again == "no" or play_again == "n":
                    play = False
                break
