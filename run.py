import gspread
from google.oauth2.service_account import Credentials
import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('smartwatch_hanker')


# Get available stock data
stock = SHEET.worksheet('stock')
stock_data = stock.get_all_records()

# Get all product names in stock worksheet
products = stock.col_values(1)


INPUT_INSTRUCTIONS = """
Please enter product name where asked,
and then enter quantity ordered where asked too.
Type the word 'done' without the quotations when you finish.
Product name should be correctly typed in lowercase characters
and quantity should be numbers only\n
"""


# Get customer orders from the inventory manager
def get_customer_orders():
    """
    Get customer orders input from the user.
    I run a while loop to collect a valid string of product name
    and of product quantity from the user via the terminal,
    The while loop will repeatedly request data, until it is valid
    and the user types the word- 'done'.
    """    
    
    orders = []

    while True:
        print("Please enter product name where asked,")
        print("and then enter quantity ordered where asked too.")
        print("Type the word 'done' without the quotations when you finish.")
        print("Product name should be correctly typed in lowercase characters")
        print("and quantity should be numbers only\n")

        product = input("Enter product name (or 'done' to finish): ")

        if product.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity of {product}: "))
        orders.append({"Product": product, "Quantity": quantity})

    return orders


# Compare customer orders with available stock
def check_inventory(orders):
    
    for order in orders:
        product = order['Product']
        ordered_quantity = order['Quantity']
        available_quantity = 0
        
        # Find available quantity in stock data
        for item in stock_data:
            if item['Product'] == product:
                available_quantity = item['Quantity']
                break
        
        # Compare available quantity with ordered quantity
        if available_quantity >= ordered_quantity:
            print(f"We can fulfill the request for {ordered_quantity} units of {product}.")
        else:
            print(f"Insufficient stock for {product}. Available quantity: {available_quantity}. Ordered quantity: {ordered_quantity}.")


# Get customer orders from the inventory manager
customer_orders = get_customer_orders()

# Call the function to check inventory
check_inventory(customer_orders)