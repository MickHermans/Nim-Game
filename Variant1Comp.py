import random


def stack_show_v1(x):
    a = x // 10
    b = "# " * 10 + "\n"
    c = "# " * (x % 10) + "\n"
    d = b * a + c
    return d


def main_gameplay(play, begin):
    while play:
        turns = True

        playing_stones = input("Enter amount of playing stones : ")
        while not playing_stones.isnumeric():
            playing_stones = input("Invalid input, try again : ")
        playing_stones = int(playing_stones)

        while turns:
            while begin == "yes" or begin == "y":
                print("Your turn")
                print(playing_stones, "stones on the stack")
                print(stack_show_v1(playing_stones), "\n")
                move1 = input(f"Enter amount of stones you take from the stack : ")
                while not move1.isnumeric() or (move1 != "1" and move1 != "2" and move1 != "3") or \
                        playing_stones - int(move1) < 0:
                    move1 = input("Invalid input, try again : ")
                move1 = int(move1)
                print("")
                playing_stones -= move1

                if playing_stones == 0:
                    print(f"!!! Congrats you wins !!!\n")
                    play_again = input("Do you want to play again? : ")
                    while play_again != "yes" and play_again != "y" and play_again != "no" and play_again != "n":
                        play_again = input("Invalid input, try again : ")
                    if play_again == "no" or play_again == "n":
                        play = False
                    break

                print("Computers turn")
                print(playing_stones, "stones on the stack")
                print(stack_show_v1(playing_stones), "\n")
                if playing_stones % 4 != 0:
                    move = playing_stones % 4
                elif playing_stones % 4 == 0:
                    move = random.randint(1, 3)
                print("")
                print(f"The computer took {move} stone(s) of the stack")
                playing_stones -= move

                if playing_stones == 0:
                    print(f"!!! You lose !!!\n")
                    play_again = input("Do you want to play again? : ")
                    while play_again != "yes" and play_again != "y" and play_again != "no" and play_again != "n":
                        play_again = input("Invalid input, try again : ")
                    if play_again == "no" or play_again == "n":
                        play = False
                    break

            while begin == "no" or begin == "n":
                print("Computers turn")
                print(playing_stones, "stones on the stack")
                print(stack_show_v1(playing_stones), "\n")
                if playing_stones % 4 != 0:
                    move = playing_stones % 4
                elif playing_stones % 4 == 0:
                    move = random.randint(1, 3)
                print("")
                print(f"The computer took {move} stone(s) of the stack")
                playing_stones -= move

                if playing_stones == 0:
                    print(f"!!! You lose !!!\n")
                    play_again = input("Do you want to play again? : ")
                    while play_again != "yes" and play_again != "y" and play_again != "no" and play_again != "n":
                        play_again = input("Invalid input, try again : ")
                    if play_again == "no" or play_again == "n":
                        play = False
                    break

                print("Your turn")
                print(playing_stones, "stones on the stack")
                print(stack_show_v1(playing_stones), "\n")
                move1 = input(f"Enter amount of stones you take from the stack : ")
                while not move1.isnumeric() or (move1 != "1" and move1 != "2" and move1 != "3") or \
                        playing_stones - int(move1) < 0:
                    move1 = input("Invalid input, try again : ")
                move1 = int(move1)
                print("")
                playing_stones -= move1

                if playing_stones == 0:
                    print(f"!!! Congrats you wins !!!\n")
                    play_again = input("Do you want to play again? : ")
                    while play_again != "yes" and play_again != "y" and play_again != "no" and play_again != "n":
                        play_again = input("Invalid input, try again : ")
                    if play_again == "no" or play_again == "n":
                        play = False
                    break
