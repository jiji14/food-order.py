itemNames = ['ramen', 'udon', 'katsudon', 'egg', 'chashu', 'coke', 'sprite']

itemTypes = {'ramen' : 'main',
            'udon' : 'main',
            'egg' : 'side',
            'chashu' : 'side',
            'coke' : 'drink',
            'sprite' : 'drink'}

itemPrices = {'ramen' : 10000,
            'udon' : 9000,
            'egg' : 2000,
            'chashu' : 2000,
            'coke' : 1000,
            'sprite' : 1000}


def printOrder(items):
    print("prints out")

    if len(items) == 0:
        print("empty order")
    else:
        sum = 0
        type_list = []
        for food in items:
            type = itemTypes.get(food)
            if type not in type_list:
                type_list.append(type)

        for type in type_list:
            print("{}". format(type))
            for food in items:
                money = itemPrices.get(food)
                if itemTypes.get(food) == type:
                    print(" {}". format(food))
                    sum += money   

        print("total : {}". format(sum))
    print("\n")

printOrder([])
printOrder(['ramen'])
printOrder(['ramen', 'chashu', 'sprite', 'ramen'])
