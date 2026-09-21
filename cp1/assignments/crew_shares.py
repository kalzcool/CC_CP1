#CC crew shares
import random
num_pirates= int(input("How many pirates including Yondu and Peter: "))
num_units= random.randint(500, 5000)
yondus_share=round( num_units*.13, 2) 
peters_share=round( (num_units- yondus_share)*.11, 2)
left_total= num_units -(yondus_share+peters_share)
crew_share= round(left_total/ num_pirates, 2 )

print(f"Pirates = {num_pirates}")
print(f"units = {num_units}")
print(f"Yondu's share = {yondus_share}")
print(f"peter's share = {peters_share}")
print(f"crew share = {crew_share}")
