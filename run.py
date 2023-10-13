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

# Get customer orders from the inventory manager
def get_customer_orders():
    orders = []
    while True:
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