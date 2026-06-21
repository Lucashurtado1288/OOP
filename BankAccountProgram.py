#This program demonstrates the BankAccount class.
# the alias for BankAccountClass is bc, for faster referencing
import BankAccountClass as bc

def main():
    
   # Get the starting balance.
   start_bal = float(input('Enter your starting balance: '))

   # Create a BankAccount object.
   savings = bc.BankAccount(start_bal)

   # Deposit the user's paycheck.
   # calling the deposit method from BankAccountClass.py file
   # pay = amount within the deposit method, they dont need to match
   pay = float(input('How much were you paid this week? '))
   print('I will deposit that into your account.')
   savings.deposit(pay)

   # Display the balance.
   print('Your account balance is $', format(savings.get_balance(), ',.2f'),
        sep='')

   # Get the amount to withdraw.
   # calling the withdrawal method on BankAccountClass.py file
   # cash = amount within the deposit method, they dont need to match
   cash = float(input('How much would you like to withdraw? '))
   print('I will withdraw that from your account.')
   savings.withdraw(cash)

    

   # Display the balance.
   # sep='' is used in the print() function to control what separates multiple values.
   print('Your account balance is $', 
        format(savings.get_balance(), ',.2f'),
        sep='')

   print(savings)

# Call the main function.
main()