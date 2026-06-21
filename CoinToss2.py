# Passing an object as an argumment through a function

import CoinClass as c

def show_coin_status(coin_obj):
    print(f"This side of the coing is up: {coin_obj.get_sideup()}")


def flip(coin_obj):
    coin_obj.toss()         #creating toss method

#creatinng an instance called my_coin of the coin_obj object
my_coin = c.Coin()
#passing my object as an arguement through function called show_coin_status
# my_coin is now a reference through show_coin_status
    # which allows acess to the coin_obj object 
    # also means we can acess the methods, line 6, to that instance 
show_coin_status(my_coin)
flip(my_coin)
show_coin_status(my_coin)
