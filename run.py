# -*- coding: utf-8 -*-

import datetime
import gspread
from tabulate import tabulate
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Rinse and Repeat')


def print_orders(orders):
    """
    Print a list of orders in a nicely formatted table. The column titles are
    the keys of the row dictionaries. Note that this function works with lists
    of rows as dictionaries, not lists of rows as lists. This is the format we
    use in most functions, e.g., `fetch_orders[_...]`.
    """
    print(tabulate(orders, headers="keys"))


def print_customers(customers):
    """
    Print a list of customers in a nicely formatted table. The column titles
    are the keys of the row dictionaries. Note that this function works with
    lists of rows as dictionaries, not lists of rows as lists. This is the
    format we use in most functions, e.g., `fetch_customers[_...]`.
    """
    print(tabulate(customers, headers="keys"))


def fetch_orders():
    """
    Fetch all rows from the Orders worksheet. Each row is represented by a
    dictionary with the column headers as the key names. The data type of each
    value is determined by the data type in the columns of the worksheet.
    """
    return SHEET.worksheet('Orders').get_all_records()


def fetch_orders_with_status(status):
    """
    Fetch rows from the Orders worksheet, which has a certain status. The
    status should be one of "Dropped off", "Ready for pickup", and "Picked up".
    The status string must be an exact match, including case and whitespace.
    The result will be a list of zero or more items, depending on whether the
    ID was found in the worksheet or not.
    """
    all = fetch_orders()
    return list(filter(lambda order: order['Status'] == status, all))


def fetch_orders_with_id(order_id):
    """
    Fetch rows from the Orders worksheet, which has a certain ID. The ID must
    be a number, not a string. The result will be a list of one or zero items,
    depending on whether the ID was found in the worksheet or not. We return
    the single matching row as a list so that we can easily pass it to the
    functions that works with lists of rows, e.g., `print_orders`.
    """
    all = fetch_orders()
    return list(filter(lambda order: order['ID'] == order_id, all))


def list_dropped_off_orders():
    """
    Fetch all orders that have the status "Dropped off" and print them to the
    terminal as a table. There is no pagination, so if the list is long, then
    the printed table will also be long.
    """
    print_orders(fetch_orders_with_status('Dropped off'))


def list_ready_for_pickup_orders():
    """
    Fetch all orders that have the status "Ready for pickup" and print them to
    the terminal as a table. There is no pagination, so if the list is long,
    then the printed table will also be long.
    """
    print_orders(fetch_orders_with_status('Ready for pickup'))


def list_picked_up_orders():
    """
    Fetch all orders that have the status "Picked up" and print them to the
    terminal as a table. There is no pagination, so if the list is long, then
    the printed table will also be long.
    """
    print_orders(fetch_orders_with_status('Picked up'))


def list_all_orders():
    """
    Fetch all orders and print them to the terminal as a table. There is no
    pagination, so if the list is long, then the printed table will also be
    long.
    """
    print_orders(fetch_orders())


def fetch_customers():
    """
    Fetch all rows from the Customers worksheet. Each row is represented by a
    dictionary with the column headers as the key names. The data type of each
    value is determined by the data type in the columns of the worksheet.
    """
    return SHEET.worksheet('Customers').get_all_records()


def fetch_customers_with_order_id(order_id):
    """
    Fetch rows from the Customers worksheet, which has a certain order ID. The
    order ID must be a number, not a string. The result will be a list of one
    or zero items, depending on whether the order ID was found in the worksheet
    or not. We return the single matching row as a list so that we can easily
    pass it to the functions that works with lists of rows, e.g.,
    `print_customers`.
    """
    all = fetch_customers()
    return list(filter(lambda customer: customer['Order ID'] == order_id, all))


def mark_order(order, status, date_column, clear_column_letters):
    """
    Change the value of the "Status" column of the given order. We first find
    the order in the spreadsheet and then update both the "Status" column and
    set the specified date column to today's date, e.g., the "Ready for pickup"
    column. Optionally, one or more columns can be cleared, e.g., the date
    columns that are only set for later "Status" value, allowing the user to
    undo changes to the order status. It is the responsibility of the caller to
    ensure that the order exists in the sheet. If not, an unspecified error is
    raised and the program likely exits.
    """
    today = datetime.date.today().strftime('%Y-%m-%d')
    sheet = SHEET.worksheet('Orders')
    order_id = order['ID']
    order_id_string = str(order_id)
    order_id_cell = sheet.find(order_id_string, in_column=1)  # 1 = ID column
    row = order_id_cell.row
    sheet.update_cell(row, 2, status)  # 2 = Status column

    # Only set the date column to today if it does not already have a value.
    # This is so that we support moving between states to undo mistakes,
    # without accidentally messing up the date that was already set.
    if not sheet.cell(row, date_column).value:
        sheet.update_cell(row, date_column, today)

    # Clear the date columns that don't make sense for the new status, e.g.,
    # clear "Picked up" when changing the status to "Ready for pickup".
    sheet.batch_clear([f'{col}{row}' for col in clear_column_letters])


def mark_orders(orders, status, date_column, clear_columns):
    """
    Change the value of the "Status" column of the given list of orders. We
    first find the orders in the spreadsheet and then update both the "Status"
    column and set the specified date column to today's date, e.g., the "Ready
    for pickup" column. It is the responsibility of the caller to ensure that
    all orders exist in the sheet. If not, an unspecified error is raised and
    the program likely exits.
    """
    for order in orders:
        mark_order(order, status, date_column, clear_columns)


def mark_orders_ready_for_pickup(orders):
    """
    Change the value of the "Status" column of the given list of orders to
    "Ready to pickup", and update set the "Ready for pickup" date column to
    today's date. The "Picked up" date column is cleared. It is the
    responsibility of the caller to ensure that all orders exist in the sheet.
    If not, an unspecified error is raised and the program likely exits.
    """
    mark_orders(orders, 'Ready for pickup', 4, ['E'])


def mark_orders_picked_up(orders):
    """
    Change the value of the "Status" column of the given list of orders to
    "Picked up", and update set the "Picked up" date column to today's date.
    It is the responsibility of the caller to ensure that all orders exist in
    the sheet. If not, an unspecified error is raised and the program likely
    exits.
    """
    mark_orders(orders, 'Picked up', 5, [])


def view_customer_information(orders):
    """
    Fetch the customer for the given order and print their information in a
    nice table. Note that this function currently has the limitation that it
    accepts exactly one order in the list, no more, no less. It is the
    responsibility of the caller to make sure that the list contains exaclly
    one order.
    """
    order_id = orders[0]['ID']
    customers = fetch_customers_with_order_id(order_id)
    print_customers(customers)


def print_edit_menu(orders):
    """
    Print a list of commands for the order editing. This function does not
    handle user input, it just prints the list to the terminal. The commands
    are numbered from 1 through 4, with a special 0 command to go back to the
    previous menu.
    """
    status = orders[0]['Status']
    print('')
    if status != 'Ready for pickup':
        print('1: Mark as ready for pickup')
    if status == 'Ready for pickup':
        print('2: Mark as picked up')
    print('')
    print('3: View customer information')
    print('')
    print('0: Back')
    print('')


def edit_menu(orders):
    """
    Display the order editing menu, given a list of orders. The user can input
    a command number from the list. If the command is valid, the corresponding
    command function is executed; otherwise print an error message and the ask
    the user again to enter a menu command. Returns True if the user exited the
    menu, and False if the user executed a command that changed the orders.
    """
    while True:
        command = input('> \n').strip()
        options = {
            '1': mark_orders_ready_for_pickup,
            '2': mark_orders_picked_up,
            '3': view_customer_information
        }
        if not command:
            continue
        if command in ['0', 'b', 'B']:
            return (True, False)
        if command not in options:
            print('Unknown command:', command)
            print('')
            continue
        print('')
        options[command](orders)
        return (False, command != '3')


def edit_order_by_id(order_id):
    """
    Fetch the order matching the order ID entered by the user. If the order can
    be found, display the edit menu, otherwise print an error message and exit.
    The user stays in the edit manu until the explicitly going back to the
    previous menu.
    """
    print('')
    orders = []
    back = False
    load = True
    while not back:
        if load:
            orders = fetch_orders_with_id(order_id)
            if len(orders) == 0:
                print('Could not find an order with a matching ID.')
                break
            print_orders(orders)
        print_edit_menu(orders)
        (back, load) = edit_menu(orders)


def parse_order_id(order_id_string):
    """
    Given a string, as entered by the user, convert it to a validated order ID.
    If the string does not represent a valid order ID, e.g., not a number or a
    negative number, a ValueError is raised for the caller to handle.
    """
    order_id = int(order_id_string)
    if order_id <= 0:
        raise ValueError('Must be greater than 0.')
    return order_id


def find_order_by_id():
    """
    Ask the user to enter an order ID and look it up in the Orders worksheet.
    If the order is found, print it and enter a submenu with operations that
    can be performed on the single order, e.g., marking it as being ready for
    pickup.
    """
    try:
        order_id = parse_order_id(input('Order ID: \n'))
        edit_order_by_id(order_id)
    except ValueError as e:
        print('Invalid order ID:', e)


def input_count(prompt):
    """
    Input the count of an item that can be dry cleaned, accepting positive
    integers, including zero and empty (meaning zero as well). Keeps asking
    the user for the count until a valid number is entered.
    """
    while True:
        try:
            count = input(f'{prompt}: \n').strip()
            return 0 if not count else int(count)
        except ValueError as e:
            print('Number of items must be a positive number or empty/zero.')


def input_non_empty(prompt):
    """
    Input a non-empty string. Keeps asking the user for the string until a non-
    empty string is entered. The string is stripped from surrounding whitspace.
    """
    while True:
        string = input(f'{prompt}: \n').strip()
        if string:
            return string
        print('This field cannot be empty.')


def input_order_items():
    """
    Input the count of each item that can be dry cleaned. Asks about each item
    one by one, based on the available item types in the "Prices" sheet.
    Returns a list with the total price of the order and the count of each
    item.
    """
    print('Enter the number of items to clean, per item type.')
    prices = SHEET.worksheet('Prices').get_all_records()[0]
    total = 0
    items = []
    for item in prices.keys():
        count = input_count(f'{item} {prices[item]}')
        price = float(prices[item][1:])  # Drop the €
        total = total + (count * price)
        items.append(count)
    items.insert(0, f'€{total}')
    return items


def input_customer():
    """
    Input the customer information for the current order. Asks for the customer
    name, email, and phone number. Returns a list of these values in this
    order. None of the fields may be empty, but we don't validate that the
    email and phone number are correct.
    """
    print('Enter customer information.')
    name = input_non_empty('Name')
    email = input_non_empty('Email')
    mobile = input_non_empty('Mobile')
    return [name, email, mobile]


def enter_new_order():
    """
    Enter a new order by asking the user to input the customer information
    (name, email, and phone number) and the count of each type of item to
    clean. Once the information has been entered, a new row is added to the
    "Orders" sheet and also the "Customers" sheet.
    """
    orders = fetch_orders()
    order_id = max([order['ID'] for order in orders]) + 1
    today = datetime.date.today().strftime('%Y-%m-%d')
    order = [order_id, 'Dropped off', today, '', '']
    order.extend(input_order_items())
    SHEET.worksheet('Orders').append_row(order)

    print('')
    customer = [order_id]
    customer.extend(input_customer())
    SHEET.worksheet('Customers').append_row(customer)

    edit_order_by_id(order_id)


def print_main_menu():
    """
    Print a list of commands for the main menu. This function does not handle
    user input, it just prints the list to the terminal. The commands are
    numbered from 1 through 6, with a special 0 command to quit the program.
    """
    print('')
    print('1: Enter a new order')
    print('2: Find order by ID')
    print('')
    print('3: List dropped off orders')
    print('4: List ready for pickup orders')
    print('5: List picked up orders')
    print('6: List all orders')
    print('')
    print('0: Quit')
    print('')


def main_menu():
    """
    Display the program main menu, given a list of orders. The user can input a
    command number from the list. If the command is valid, the corresponding
    command function is executed; otherwise print an error message and the ask
    the user again to enter a menu command.
    """
    while True:
        print_main_menu()
        command = input('> \n').strip()
        options = {
            '1': enter_new_order,
            '2': find_order_by_id,
            '3': list_dropped_off_orders,
            '4': list_ready_for_pickup_orders,
            '5': list_picked_up_orders,
            '6': list_all_orders,
        }
        if not command:
            continue
        if command in ['0', 'q', 'Q']:
            break
        if command not in options:
            print('Unknown command:', command)
            continue
        print('')
        options[command]()


def main():
    """
    Print a welcome message and some instructions on how to use the program,
    after which the main menu is displayed and run until the program is asked
    to quit, by user input. Finally, print a goodbye message, because it is
    just polite.
    """
    print('')
    print('Welcome to Rinse and Repeat dry cleaning')
    print('----------------------------------------')
    print((
        'Enter menu commands (1 through 6)'
        'from the list below using the keyboard.'))
    print((
        'Press return to perform the command.'
        'To exit the program, enter 0 or Q.'))
    main_menu()
    print('')
    print('Goodbye, have a fantastic day!')

main()