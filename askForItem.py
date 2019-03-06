def askForItem():
    
    while True:
        print("What else do you want to order? Type one of ramen, udon, katsudon, egg, chashu, coke, sprite.")
        print("If you are done, press Enter.")
        menu = input("> ")

        if (len(menu) == 0):
            return;
        elif (menu not in itemNames):
            print("Unknown item.")
        else:
            return menu;

print(askForItem())
