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
To compare ordered quantities with available stock:
Please enter product name when asked,
and then enter quantity ordered when asked too.
Product name should be correctly typed in lowercase characters
and quantity should be numbers only.\n
"""


def update_inventory():
    """
    Update the stock inventory,
    adding a new row containing the new product and quantity
    at the end of the stock inventory.
    """
    while True:
        update_stock = input("Do you want to update the inventory (y/n): ")
        
        if update_stock.lower() not in ("y", "yes"):
            break                    
        else:
            new_product = input("Enter new product name: \n")

            try:
                new_quantity = int(input(f"Enter quantity of {new_product}: \n"))

            except ValueError:
                print("Invalid quantity value, please enter a number\n")
                continue

            print(f"Updating inventory...\n")

            stock.append_row([new_product, new_quantity])   

    print("Inventory updated successfully\n")

    return


# Get customer orders from the inventory manager
def get_customer_orders():
    """
    Get customer orders input from the user.
    I run a while loop to collect a valid string of product name
    and of product quantity from the user via the terminal,
    The while loop will repeatedly request input data, until it is valid.
    """    
    
    orders = []

    print(INPUT_INSTRUCTIONS)

    while True:        

        product = validate_product()

        quantity = validate_quantity(product)

        orders.append({"Product": product, "Quantity": quantity})

        another_product = input("Do you want to add another product? (y/n): ")
        if another_product.lower() not in ("y", "yes"):
            break

    return orders


def validate_product():
    while True:

        product = input("Enter product name: \n")

        if product not in products:
            print("Invalid product name, please enter a valid product name\n")
            continue
 
        return product


def validate_quantity(product):
    
    while True:
    
        try:
            quantity = int(input(f"Enter quantity of {product}: \n"))

        except ValueError:
            print("Invalid quantity value, please enter a number\n")
            continue

        return quantity


# Compare customer orders with available stock
def check_inventory(orders):

    """
    Compare orders with stock and for each item product
    and report possibility of fulfilling order requests.
    """

    print("Checking stock ...\n")
    print("Determining the possibility of meeting your orders ...\n")
    
    for order in orders:
        product = order['Product']
        ordered_quantity = order['Quantity']
        available_quantity = 0
        
        # find available quantity in stock data
        for item in stock_data:
            if item['Product'] == product:
                available_quantity = item['Quantity']
                break
        
        # compare available quantity with ordered quantity        
        if available_quantity >= ordered_quantity:
            print(f"We can fulfill the request for {ordered_quantity} units of {product}.\n")
        else:
            print(f"Insufficient stock for {product}. Available quantity: {available_quantity}. Ordered quantity: {ordered_quantity}.\n")


def main():
    """
    Calling all program functions
    """
    # calls the function to update inventory
    update_inventory()

    # gets customer orders from the inventory manager
    customer_orders = get_customer_orders()
 
    # calls the function to check inventory
    check_inventory(customer_orders)

print("Welcome to Smartwatch Hanker Inventory Management\n")
main()