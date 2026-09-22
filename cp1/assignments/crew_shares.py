#CC crew shares
import random
while True:
    num_pirates= input("How many pirates including Yondu and Peter: ")

    if num_pirates.isdigit():
        num_pirates=int(num_pirates)
        break

    else:
        print("Nope try again")
 
num_units= random.randint(500, 5000)
left_units= num_units -((num_pirates-2)*3)
yondus_share=round( left_units*.13 , 2) 
peters_share=round( (left_units- yondus_share)*.11, 2)
left_total= left_units -(yondus_share+peters_share)
crew_share= round(left_total/ num_pirates, 2 )

print(f"Pirates = {num_pirates}")
print(f"units = {num_units}")
print(f"Yondu's share = {yondus_share: .2f}")
print(f"peter's share = {peters_share:.2f}")
print(f"crew share = {crew_share: .2f}")
