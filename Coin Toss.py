# This is the program file that will use blueprint, class definition file CoinClass.py

# Refers to the name of the file, not to the name of the class 
# c is an alias of CoinClass
import CoinClass as c


# The main function.
def main():
       # Create an object from the Coin class.
       # when running c.coin() it will run the __init__ automatically 
       # __init__ method is located in CoinClass.py
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       # Print the object we created my_coin
       # Do not add coin it is just the blueprint
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       # By calling the toss method it will carry out the toss method on CoinClass.py
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           my_coin.__sideup = 'Heads'
           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()
