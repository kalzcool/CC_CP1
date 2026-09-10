#CC idiot proof 

#Full disclosure Ms. LaRose, I used AI to help me on this assignment, I have never used AI for any assignment before. I did not have AI write my code, I was very stuck on what I was doing wrong on the phone number section so I googled "how to split a full string in python and rejoin with spaces in certain parts", google was somewhat helpful but not at the same time. I asked the AI to not write the code but explain to me how to do the phone number section, it wanted me to use a list() function but I had no clue what that was and didn't want to possibly get in trouble. This whole thing is a peice together of trying to what the AI said I was doing wrong while using what I know and trying to figure it out on my own. I've been sitting here for like an hour trying to figure out every little thing I was messing up and fix it. I think there are some parts we havent learned yet that are in this but I am so tired and confused I think thats literally the only way to do this? Or we have talked about it and I'm just really tired. Please don't crucify me I swear I wrote all the code myself I jsut had AI explain it (though very poorly) to me to I could see where my brain failed me. Also I won't be in class on the 9th (im too lazy to email) I have a doctors appointment, I'll get the notes at home and email you if I don't understand anything trust
name =input("What is your full name: ").strip().title()
while True:
    phone=input("What is your phone number: ").strip()

    if phone.isdigit() and len(phone) >=7:
        break
    else:
        print("Nope try again")
 

phone_spaced=" ".join(str(phone))
phone_split=phone_spaced.split()
phone1="".join(phone_split[0:3])
phone2="".join(phone_split[3:6])
phone3="".join(phone_split[6:])
while True:
    try:
        gpa=float(input('What is your gpa: '))
    except:
        print("Nope try again")
    if gpa >=5.1:
        print("Yeah no twinith")
    else:
        break



print(f"Hello {name}, your phone number is: {phone1} {phone2} {phone3}, your gpa is {round(gpa, 2)}")