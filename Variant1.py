def stack_show_v1(x):
    a = x // 10
    b = "# " * 10 + "\n"
    c = "# " * (x % 10) + "\n"
    d = b * a + c
    return d


def main_gameplay(play, player1, player2):
    while play:
        turns = True

        playing_stones = input("Enter amount of playing stones : ")
        while not playing_stones.isnumeric():
            playing_stones = input("Invalid input, try again : ")
        playing_stones = int(playing_stones)

        while turns:
            print(f"{player1}'s turn")
            print(playing_stones, "stones on stack")
            print(stack_show_v1(playing_stones), "\n")
            move1 = input(f"Enter amount of stones {player1} takes from the stack : ")
            while not move1.isnumeric() or (move1 != "1" and move1 != "2" and move1 != "3") or \
                    playing_stones - int(move1) < 0:
                move1 = input("Invalid input, try again : ")
            move1 = int(move1)
            print("")
            playing_stones -= move1

            if playing_stones == 0:
                print(f"!!! congrats {player1} wins !!!\n")
                play_again = input("Do you want to play again? : ")
                while play_again != "yes" and play_again != "y" and play_again != "no" and play_again != "n":
                    play_again = input("Invalid input, try again : ")
                if play_again == "no" or play_again == "n":
                    play = False
                break

            print(f"{player2}'s turn")
            print(playing_stones, "stones on stack")
            print(stack_show_v1(playing_stones), "\n")
            move2 = input(f"Enter amount of stones {player2} takes from the stack : ")
            while not move2.isnumeric() or (move2 != "1" and move2 != "2" and move2 != "3") or \
                    playing_stones - int(move2) < 0:
                move2 = input("Invalid input, try again : ")
            move2 = int(move2)
            print("")
            playing_stones -= move2

            if playing_stones == 0:
                print(f"!!! congrats {player1} wins !!!\n")
                play_again = input("Do you want to play again? : ")
                while play_again != "yes" and play_again != "y" and play_again != "no" and play_again != "n":
                    play_again = input("Invalid input, try again : ")
                if play_again == "no" or play_again == "n":
                    play = False
                break
