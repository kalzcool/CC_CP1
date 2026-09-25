#CC user sign in
print("Hello, welcome to Artimis studios") 
#intro because I wanted too

occupation=input("Are you a new recruit? ")
if occupation =="Yes":
    print("Wonderful lets get you signed in so you can complete your tasks!")
elif occupation =="No I've been here":
    print("Welcome back honey let's get you signed in")
elif occupation == "No":
    print("Please go to a recruitment agent if you would like to work here")
elif occupation == "Yellow":
    print("Welcome back sugar let's get you signed in ")
elif occupation== "Maybe":
    print("Well go check with a recruitment agent to see if you would like to work here honey I can't help you with that")
else:
    print("Not a valid input loves")
#starting out and asking if they work here so I can get their user and password

known_users= ["Calixxxx", "Andys_so_peak", "Kitkatz", "talia", "yellow_mellow", "Myrainbowpenahtesme", "IDKWHATIMSUPPOSEDTOEVENDOHEREMAN", "iwantcofe"] #worker usernames that will be accepted
known_passwords= ["451233", "I_hate_samual", "id!dntsl33pbr0", "mydear3st", "iaman3gg", "Z@wG!l!S1oUs", "freaksTER400000000x52", "password1345679027"] #worker passwords that will be accepted if they match up with the user names

user_name = input("Please input your username: ").strip() #getting the username
user_password= input("Please input your password: ").strip() #getting the password

if user_name in known_users:
    user_index = known_users.index(user_name)
    if  user_password == known_passwords[user_index]:
        print("Great Welcome back! Please get to work quickly.")
    else:
        print("Password is wrong")
else:
    print("Either you messed up or you aren't on the list buddy")
    #this whole chunk is making sure the passwords match up with the usernames because I don't want them to mix and match
#Ms. LaRose I'm so tired holy crap. I put this through AI to see what grade I would get and it basically yelled at me for being an idiot a million times oh my ancients, but now I actually added comments and the users can't mix and match passwords. I thought it would be funny but apperently AI and the rubric have no humor. Don't slime me out im exhausted and for some reason this is making my laptop run slowly. 