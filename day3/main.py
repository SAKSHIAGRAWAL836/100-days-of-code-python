print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
move = input("type left or right to take inital step.")

if move == "left" or "Left":
    select = input("select door to move in: 1,  2 or  3.")
    if select == "1":
        weapon = input("select a weapon: gun, knife or sword.")
        if weapon == "sword":
            print("Just one right step away from treasure.")
            print("Remember the right colour of sword is the key to the treasure.")
            colour = input("select colour for your sword: red, yellow or green.")
            if colour == "green":
                print("CONGRATULATIONS. RAJA KA SAARA SONA AAJ SE TUMHARA.")

    elif select == "2" or "3":
        print("GAME OVER.")
    else:
        print("you types in something wrong.")
elif move == "right" or "Right":
    print("YOU ARE NOT MADE OF THIS GAME.")
else:
    print("you typed something wrong.")
