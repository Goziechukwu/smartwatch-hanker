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
print(stock_data)

# # Get customer orders from the inventory manager
# def get_customer_orders():
#     orders = []
#     while True:
#         product_name = input("Enter product name (or 'done' to finish): ")
#         if product_name.lower() == 'done':
#             break
#         quantity = int(input(f"Enter quantity of {product_name}: "))
#         orders.append({"Product": product_name, "Quantity": quantity})
#     return orders
