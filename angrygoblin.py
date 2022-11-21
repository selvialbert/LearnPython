
print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")

player_name = input("Type in your name : ")
print(player_name + ", do you think you can find the goblin hiding in the kitchen cupboards?")
print("|_||_||_||_||_|")

goblin_cupboard = 3

input_incorrect = True
while input_incorrect:

    input_number = input("Which cupboard do you think the goblin is in [type in number]: ")
    input_number= int(input_number)
    if input_number == goblin_cupboard:
       print("Well done!! You have  found the goblin. He was so scared he ran away")
       break
    else:
       print("Sorry. The goblin is still lurking somewhere else.")



