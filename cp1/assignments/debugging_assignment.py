#CC debug w/ debugger

# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? ")) #made quantity int

total = price * quantity

discounted_total = total*.90

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

#added crew member discount

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name)#mispelled variable name so it wouldn't run
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(total))#fixed price to be the actual total price before tax, used the wrong variable
if pirate_name== "Calix":
    crew_price= total_with_tax *.9
    print("Total with tax: " +str(round(crew_price, 2))+ " credits")
elif pirate_name== "Mrs. LaRose":
    crew_price= total_with_tax *.9
    print("Total with tax: " +str(round(crew_price, 2))+ " credits")
elif pirate_name== "Melissa":
    crew_price= total_with_tax *.9
    print("Total with tax: " +str(round(crew_price, 2))+ " credits")
else:
    print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")#added the missing parentheses
    #fixed it so it would print crew discount and regular price 
#fixed syntax
#one runtime done
#both runtime done
#both logic errors are fixed