#CC dice roller
import random
dice= int(input("What size dice would you like to roll? (D4, D6, D8, D10, D12, D20): D"))

if dice>= 20:
    dice_num= random.randint(1,20)
    print(f'You rolled a {dice_num}!')
elif dice>= 12:
    dice_num= random.randint(1,12)
    print(f'You rolled a {dice_num}!')
elif dice>= 10:
    dice_num= random.randint(1,10)
    print(f'You rolled a {dice_num}!')
elif dice>= 8:
    dice_num= random.randint(1,8)
    print(f'You rolled a {dice_num}!')
elif dice>= 6:
    dice_num= random.randint(1,6)
    print(f'You rolled a {dice_num}!')
elif dice>= 4:
    dice_num= random.randint(1,4)
    print(f'You rolled a {dice_num}!')
else:
    print("Not an option buddy pick again, only the number please")