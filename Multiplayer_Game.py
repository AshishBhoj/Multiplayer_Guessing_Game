import random
print("Multiplayer Random Number Guessing Game\n")
i = 0
j = 0
player_1 = input("Player_1 Enter your name : ")
player_2 = input("Player_2 Enter your name : ")

a = int(input(f"\n{player_1} enter lower_limit number : "))
b = int(input(f"{player_2} enter upper_limit number : "))

to_be_guessed_1 = random.randint(a,b)

print(f"\n***** {player_1} Turn *****")
guess_1 = 0
while guess_1 != to_be_guessed_1:
        guess_1 = int(input(f"\nEnter number between {a} and {b} : "))
        if guess_1 >= a  and guess_1 <= b:
            if guess_1 > to_be_guessed_1:
                print(f"{guess_1} is greater \nTry Again")

            elif guess_1 < to_be_guessed_1:
                print(f"{guess_1} is smaller\nTry Again")

            i += 1
else:
    print(f"{guess_1} is matched")
    print("Congratulation, You Did It!!!")

print(f"\n***** {player_2} Turn *****")
guess_2 = 0
to_be_guessed_2 = random.randint(min(a,b),max(a,b))
while guess_2 != to_be_guessed_2:
        guess_2 = int(input(f"\nEnter number between {a} and {b} : "))
        if guess_2 >= a and guess_2 <= b:
            if guess_2 > to_be_guessed_2:
                print(f"{guess_2} is greater \nTry Again")

            elif guess_2 < to_be_guessed_2:
                print(f"{guess_2} is smaller\nTry Again")

            j += 1
else:
    print(f"{guess_2} is matched")
    print("Congratulation, You Did It!!!")


print(f"\nTotal Chances taken by {player_1} : ",i)
print(f"Total Chances taken by {player_2} : ",j)
if i > j:
    print(f"\n******{player_2}****** WIN")
elif i < j:
    print(f"\n******{player_1}****** WIN")
else:
    print(f"\nMatch Tied {player_1} and {player_2} are joint winners")





