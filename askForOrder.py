def askForOrder():
    print("Welcome to ramen shop.") 
    print("Your current order: ")
    print("empty order")
    menu_list = []

    while True:
        menu = askForItem()
        if menu == None:
            print("your final order is:")
            printOrder(menu_list)  
            break;
        menu_list.append(menu)
        print("your current order is:")
        printOrder(menu_list)

askForOrder()
