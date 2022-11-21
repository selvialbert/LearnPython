import random

print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")

player_name = input("Type in your name : ")
difficulty_level = int(input("Choose your difficulty level : [5-50]"))

print(player_name + ", do you think you can find the goblin hiding in the kitchen cupboards?")
cupboard = ("|_|")

print(difficulty_level * cupboard)

goblin_cupboard = random.randint(1,10)

input_incorrect = True
while input_incorrect:

    input_number = input("Which cupboard do you think the goblin is in [type in number]: ")
    input_number= int(input_number)
    if input_number == goblin_cupboard:
       print("Well done!! You have  found the goblin. He was so scared he ran away")
       break
    else:
       print("Sorry. The goblin is still lurking somewhere else.")