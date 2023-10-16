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
stock = SHEET.worksheet("stock")
stock_data = None

# Get all product names in stock worksheet
products = None


INPUT_INSTRUCTIONS = """
To compare ordered quantities with available stock:
Please enter product name when asked,
and then enter quantity ordered when asked too.
Product name should be correctly typed in lowercase characters
and quantity should be numbers only.\n
"""

USER_OPERATIONS = """
1. See available products.
2. Check stock availability for orders received in a day.
3. Update inventory for a product.
4. Exit
"""


def refresh_stock_data():
    global stock_data
    global products

    stock_data = stock.get_all_records()
    products = stock.col_values(1)


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

        another_product = input("Do you want to add another product? (y/n):\n")
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


def update_inventory():
    """
    Updates the stock inventory for a given product.
    If new product is being added, new record will be added to sheet.
    """

    while True:
        product = input("Enter product name: \n")
        new_product = False
        if product not in products:
            new_product = True
            confirm_insert = input(
                "This product does not exist in inventory. Do you want to "
                "add it as a new product? (y/n)\n"
            )
            if confirm_insert not in ("y", "yes"):
                break

        while True:
            try:
                new_quantity = int(input(f"Enter quantity of {product}: \n"))

            except ValueError:
                print("Invalid quantity value, please enter a number\n")
                continue
            break

        print(f"Updating inventory...\n")

        if new_product:
            stock.append_row([product, new_quantity])
        else:
            cell = stock.find(product)
            if cell:
                row = cell.row
                col = cell.col

                old_qty = int(stock.cell(row, col + 1).value)
                updated_qty = old_qty + new_quantity

                stock.update_cell(row, col + 1, updated_qty)
                pass

        print("Inventory updated successfully\n")
        refresh_stock_data()

        update_another_stock = input(
            "Do you want to add another update? (y/n):\n"
        )

        if update_another_stock.lower() not in ("y", "yes"):
            break

    return


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
            print(
                f"We can fulfill the request "
                f"for {ordered_quantity} units of {product}.\n")
            print(f"Available quantity: {available_quantity}")
            print(f"Ordered quantity: {ordered_quantity}\n")
        else:
            print(f"Insufficient stock for {product}.")
            print(f"Available quantity: {available_quantity}")
            print(f"Ordered quantity: {ordered_quantity}\n")


def main():
    """
    Calling all program functions
    """
    refresh_stock_data()
    print("Welcome to Smartwatch Hanker Inventory Management\n")

    while True:
        print(USER_OPERATIONS)
        user_input = input("Please enter your choice (serial no.):\n")

        if user_input == "1":
            # print("\n".join(products))
            for index, product in enumerate(products):
                print(f"{index}: {product}")
        elif user_input == "2":
            customer_orders = get_customer_orders()
            check_inventory(customer_orders)
        elif user_input == "3":
            update_inventory()
        elif user_input == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
