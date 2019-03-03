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
        for food in items:
            type = itemTypes.get(food)
        
            print("{}". format(type))
            print("  {}". format(food))
            print(" ")

            money = itemPrices.get(food)
            sum += money
        print("total : {}". format(sum))
    print("\n")

print(printOrder([]))
print(printOrder(['ramen']))
print(printOrder(['ramen', 'chashu', 'sprite', 'ramen']))
