import gspread
from google.oauth2.service_account import Credentials
# import pandas as pd
# from sklearn.metrics.pairwise import cosine_similarity
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

orders = SHEET.worksheet('orders')

data = orders.get_all_values()

print(data)

# # Open the customer orders worksheet and stock worksheet
# orders = client.open('orders')
# stock = client.open('stock')

# # Get available stock data
# stock_data = stock_sheet.get_all_records()


# Get customer orders from the inventory manager
# def get_customer_orders():
#     orders = []
#     while True:
#         product_name = input("Enter product name (or 'done' to finish): ")
#         if product_name.lower() == 'done':
#             break
#         quantity = int(input(f"Enter quantity of {product_name}: "))
#         orders.append({"Product": product_name, "Quantity": quantity})
#     return orders

# def get_customer_data():

#     # Sample customer-product interaction data
#     customer_data = {
#         'customer_id': [1, 1, 2, 2, 3, 3, 4, 4],
#         'product_id': ['A', 'B', 'A', 'C', 'B', 'D', 'C', 'D']
#     }

#     # Create a DataFrame from the sample data
#     df = pd.DataFrame(data)
#     """
#     Get sales figures input from the user.
#     We run a while loop to collect a valid string of data from the user
#     via the terminal, which must be a string of 6 numbers separated
#     by commas. The loop will repeatedly request data, until it is valid.
#     """

#     while True:
#         print("Please enter sales data from the last market.")
#         print("Data should be six numbers, separated by commas.")
#         print("Example: 10,20,30,40,50,60\n")
#         data_str = input("Enter your data here: \n")

#         sales_data = list(data_str.split(","))

#         if validate_data(sales_data):
#             break

#     return sales_data