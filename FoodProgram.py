import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

# Initializing a variable to store the total cost
order_total = 0


# Customer 1 object
customer = fc.Customer(
    570,
    "Danni Sellyar",
    "97 Mitchell Way Hewitt Texas 76712",
    "dsellyarft@gmpg.org",
    "254-555-9362",
    False
)

# Blocking this customer #2 until ready for second run
'''
customer = fc.Customer(
    569,
    "Aubree Himsworth",
    "1172 Moulton Hill Waco Texas 76710",
    "ahimsworthfs@list-manage.com",
    "254-555-2273",
    True
)
'''


# Processing the transactions
order_total = 0                         #Reseting total cost to store matching transactions
customer_transactions = []              #Create an empty list to store matching transactions




#Start looping process for each dictionary item in transaction
for trans_id, data in dict.items():
    #Creating transaction object using a list
    transaction = fc.Transaction(data[0], data[1], data[2], data[3])

    # Matching class transaction customer id with class customer id 
    if transaction.get_customerid() == customer.get_customerid():
        #Saving matching transactions in a list
        customer_transactions.append(transaction)           #appending all matching transactions
        order_total += transaction.get_cost()               #Adding all matching transactions for total costs





# Initializing discount to zero and applying the 20% Discount
discount = 0
if customer.get_member_status():
    discount = order_total * 0.20

final_total = order_total - discount    #Calculing total cost if discount is found





# Printing customer report
print(f"Customer Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")

for t in customer_transactions:
    print(f"Order Item: {t.get_item_name()}     Price: ${t.get_cost():.2f}")

print(f"Total Cost: ${order_total:.2f}")

if discount > 0:
    print(f"Member Discount: ${discount:.2f}")
    print(f"Total Cost after discount: ${final_total:.2f}")




