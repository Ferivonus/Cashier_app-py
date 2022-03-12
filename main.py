
###############################################################################
# developer : Fahrettin Baştürk
# date : 12.05.2020
# version : 2.0.0
# leanguage : python
# description : This program is a simple shopping program.
#              It asks the user to buy things and it calculates the money
#              left after buying. It asks the user if he wants to buy again.
###############################################################################

from time import sleep


def BuyThings(money):
    print("Type what you want to buy")
    print("1. Milk is $1.99")
    print("2. Eggs are $2.99")
    print("3. Bread is $1.99")
    print("4. Chicken is $5.99")
    print("5. Apple is $5.99")
    print("6. Orange is $6.99")
    item = input('Enter the number of the item you want to buy: ')
    if (item == '1' or item == 'milk') and (money >= float(1.99)):
        howmany = int(input('How many do you want to buy: '))
        if howmany * float(1.99) > money:
            print("You don't have enough money")
            return money
        else:
            print("You bought " + str(howmany) + " milk")
            return money - howmany * float(1.99)
    elif (item == '2' or item == 'eggs') and (money >= float(2.99)):
        howmany = int(input('How many do you want to buy: '))
        if howmany * float(2.99) > money:
            print("You don't have enough money")
            return money
        else:
            print("You bought " + str(howmany) + " eggs")
            return money - howmany * float(2.99)
    elif (item == '3' or item == 'bread') and (money >= float(1.99)):
        howmany = int(input('How many do you want to buy: '))
        if howmany * float(1.99) > money:
            print("You don't have enough money")
            return money
        else:
            print("You bought " + str(howmany) + " bread")
            return money - howmany * float(1.99)
    elif (item == '4' or item == 'chicken') and (money >= float(5.99)):
        howmany = int(input('How many do you want to buy: '))
        if howmany * float(5.99) > money:
            print("You don't have enough money")
            return money
        else:
            print("You bought " + str(howmany) + " chicken")
            return money - howmany * float(5.99)
    elif (item == '5' or item == 'apple') and (money >= float(5.99)):
        howmany = int(input('How many do you want to buy: '))
        if howmany * float(5.99) > money:
            print("You don't have enough money")
            return money
        else:
            print("You bought " + str(howmany) + " apple")
            return money - howmany * float(5.99)
    elif (item == '6' or item == 'orange') and (money >= float(6.99)):
        howmany = int(input('How many do you want to buy: '))
        if howmany * float(6.99) > money:
            print("You don't have enough money")
            return money
        else:
            print("You bought " + str(howmany) + " orange")
            return money - howmany * float(6.99)
    else:
        print("You didn't buy anything")
    
    return money


def BuyAgain():
    print("Do you want to buy more: ")
    Decision = input("1. Yes\n2. No\n")
    #make decision lowercase
    Decision = Decision.lower()
    if Decision == 'yes' or Decision == '1':
        return True
    elif Decision == 'no' or Decision == '2':
        return False
    else:
        print("I guess you don't want to buy anything")
        return False
    

if __name__ == '__main__':
    BuyMore = True
    print("Welcome to the Ferivonus' store!")
    Money = float(input("Enter the amount of money you have: "))

    while Money > float(0) and BuyMore:
        Money = BuyThings(Money)
        print("You have $", Money, "left")
        BuyMore = BuyAgain()

    if Money < float(0):
        print("You have no money left")
    else:
        print("You have $", Money, "left")

    print("Thank you for shopping at Ferivonus' store!")
    sleep(2)
    print("Have a nice day!")
    print("Goodbye!")