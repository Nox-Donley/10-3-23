import random

def MonsterGen():
    num = random.randrange(0, 100)
    if num < 20:
        print("echoed screeches fill the hall...")
    elif num < 25:
        print("THE SKELETON APPEARS")
    elif num < 75:
        print("you hear whispers all around you...")
    elif num < 100:
        print("The shadows start to move...")
    else:
        print("nothing happened...")
while True:
    MonsterGen()
    choice = input("enter any key to continue...")