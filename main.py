import Variant1
import Variant2

play = True

variant = input("Enter variant : ").lower()
while variant != "1" and variant != "variant1" and variant != "variant 1" and variant != "variant-1" and \
      variant != "2" and variant != "variant2" and variant != "variant 2" and variant != "variant-2":
    variant = input("Invalid input, try again : ")

print("")

player1 = input("Name player 1 : ")
player2 = input("Name player 2 : ")

print("")

if variant == "1" or variant == "variant1" or variant == "variant 1" or variant == "variant-1":
    Variant1.main_gameplay(play, player1, player2)

if variant == "2" or variant == "variant2" or variant == "variant 2" or variant == "variant-2":
    Variant2.main_gameplay(play, player1, player2)
