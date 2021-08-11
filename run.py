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
SHEET = GSPREAD_CLIENT.open('rinse_and_repeat')

def print_orders(orders):
    """
    Print a list of orders in a nicely formatted table. The column titles are the
    keys of the row dictionaries. Note that this function works with lists of rows
    as dictionaries, not lists of rows as lists. This is the format we use in most
    functions, e.g., `fetch_orders[_...]`.
    """
    print(tabulate(orders, headers="keys"))

def fetch_orders():
    """
    Fetch all rows from the Orders worksheet. Each row is represented by a
    dictionary with the column headers as the key names. The data type of each
    value is determined by the data type in the columns of the worksheet.
    """
    return SHEET.worksheet('Orders').get_all_records()

def fetch_orders_with_status(status):
    """
    Fetch rows from the Orders worksheet, which has a certain status. The status
    should be one of "Dropped off", "Ready for pickup", and "Picked up". The
    status string must be an exact match, including case and whitespace. The
    result will be a list of zero or more items, depending on whether the ID was
    found in the worksheet or not.
    """
    return list(filter(lambda order: order['Status'] == status, fetch_orders()))

def fetch_orders_with_id(order_id):
    """
    Fetch rows from the Orders worksheet, which has a certain ID. The ID must be
    a number, not a string. The result will be a list of one or zero items,
    depending on whether the ID was found in the worksheet or not. We return the
    single matching row as a list so that we can easily pass it to the functions
    that works with lists of rows, e.g., `print_orders`.
    """
    return list(filter(lambda order: order['ID'] == order_id, fetch_orders()))

def list_dropped_off_orders():
    """
    Fetch all orders that have the status "Dropped off" and print them to the
    terminal as a table. There is no pagination, so if the list is long, then the
    printed table will also be long.
    """
    print_orders(fetch_orders_with_status('Dropped off'))

def list_ready_for_pickup_orders():
    """
    Fetch all orders that have the status "Ready for pickup" and print them to the
    terminal as a table. There is no pagination, so if the list is long, then the
    printed table will also be long.
    """
    print_orders(fetch_orders_with_status('Ready for pickup'))

def list_picked_up_orders():
    """
    Fetch all orders that have the status "Picked up" and print them to the
    terminal as a table. There is no pagination, so if the list is long, then the
    printed table will also be long.
    """
    print_orders(fetch_orders_with_status('Picked up'))

def list_all_orders():
    """
    Fetch all orders and print them to the terminal as a table. There is no
    pagination, so if the list is long, then the printed table will also be long.
    """
    print_orders(fetch_orders())

def mark_order(order, status, date_column, clear_column_letters):
    """
    Change the value of the "Status" column of the given order. We first find the
    order in the spreadsheet and then update both the "Status" column and set the
    specified date column to today's date, e.g., the "Ready for pickup" column.
    Optionally, one or more columns can be cleared, e.g., the date columns that
    are only set for later "Status" value, allowing the user to undo changes to
    the order status. It is the responsibility of the caller to ensure that the
    order exists in the sheet. If not, an unspecified error is raised and the
    program likely exits.
    """
    today = datetime.date.today().strftime('%Y-%m-%d')
    sheet = SHEET.worksheet('Orders')
    order_id = order['ID']
    order_id_string = str(order_id)
    order_id_cell = sheet.find(order_id_string, in_column=1) # 1 = ID column (A)
    row = order_id_cell.row
    sheet.update_cell(row, 2, status) # 2 = Status column (B)
    sheet.update_cell(row, date_column, today)
    sheet.batch_clear([f'{col}{row}' for col in clear_column_letters])

def mark_orders(orders, status, date_column, clear_columns):
    """
    Change the value of the "Status" column of the given list of orders. We first
    find the orders in the spreadsheet and then update both the "Status" column
    and set the specified date column to today's date, e.g., the "Ready for
    pickup" column. It is the responsibility of the caller to ensure that all
    orders exist in the sheet. If not, an unspecified error is raised and the
    program likely exits.
    """
    for order in orders:
        mark_order(order, status, date_column, clear_columns)

def mark_orders_dropped_off(orders):
    """
    Change the value of the "Status" column of the given list of orders to
    "Dropped off", and update set the "Dropped off" date column to today's date.
    The "Ready for pickup" and "Picked up" date columns are cleared. It is the
    responsibility of the caller to ensure that all orders exist in the sheet. If
    not, an unspecified error is raised and the program likely exits.
    """
    mark_orders(orders, 'Ready for pickup', 3, ['D', 'E'])

def mark_orders_ready_for_pickup(orders):
    """
    Change the value of the "Status" column of the given list of orders to "Ready
    to pickup", and update set the "Ready for pickup" date column to today's date.
    The "Picked up" date column is cleared. It is the responsibility of the caller
    to ensure that all orders exist in the sheet. If not, an unspecified error is
    raised and the program likely exits.
    """
    mark_orders(orders, 'Ready for pickup', 4, ['E'])

def mark_orders_picked_up(orders):
    """
    Change the value of the "Status" column of the given list of orders to "Picked
    up", and update set the "Picked up" date column to today's date. It is the
    responsibility of the caller to ensure that all orders exist in the sheet. If
    not, an unspecified error is raised and the program likely exits.
    """
    mark_orders(orders, 'Picked up', 5, [])

def print_edit_menu():
    """
    Print a list of commands for the order editing. This function does not handle
    user input, it just prints the list to the terminal. The commands are numbered
    from 1 through 2, with a special 0 command to go back to the previous menu.
    """
    print('')
    print('1: Mark as dropped off')
    print('2: Mark as ready for pickup')
    print('3: Mark as picked up')
    print('')
    print('0: Back')
    print('')

def edit_menu(orders):
    """
    Display the order editing menu, given a list of orders. The user can input a
    command number from the list. If the command is valid, the corresponding
    command function is executed; otherwise print an error message and the ask
    the user again to enter a menu command. Returns False if the user exited the
    menu, and True if the user executed a command that changed the orders.
    """
    while True:
        print_orders(orders)
        print_edit_menu()
        command = input('> ').strip()
        options = {
            '1': mark_orders_dropped_off,
            '2': mark_orders_ready_for_pickup,
            '3': mark_orders_picked_up
        }
        if not command: continue
        if command == '0': return False
        if command == 'b': return False
        if command == 'B': return False
        if command not in options:
            print('Unknown command:', command)
            print('')
            continue
        print('')
        options[command](orders)
        return True

def edit_order_by_id(order_id):
    """
    Fetch the order matching the order ID entered by the user. If the order can
    be found, display the edit meny, otherwise print an error message and exit. 
    """
    print('')
    while True:
        orders = fetch_orders_with_id(order_id)
        if len(orders) == 0:
            print('Could not find an order with a matching ID.')
            break
        if not edit_menu(orders):
            break

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
    Ask the user to enter an order ID and look it up in the Orders worksheet. If
    the order is found, print it and enter a submenu with operations that can be
    performed on the single order, e.g., marking it as being ready for pickup.
    """
    try:
        order_id = parse_order_id(input('Order ID: '))
        edit_order_by_id(order_id)
    except ValueError as e:
        print('Invalid order ID:', e)

def enter_count(prompt):
    while True:
        try:
            count = input(f'{prompt}: ').strip()
            if not count: return 0
            return int(count)
        except ValueError as e:
            print('Number of items must be a positive number or zero (or empty for zero).')

def enter_order_items():
    prices = SHEET.worksheet('Prices').get_all_records()[0]
    total = 0
    items = []
    for item in prices.keys():
        count = enter_count(f'{item} {prices[item]}')
        price = float(prices[item][1:]) # Drop the €
        total = total + (count * price)
        items.append(count)
    items.insert(0, f'€{total}')
    return items

def enter_new_order():
    orders = fetch_orders()
    order_id = max([order['ID'] for order in orders]) + 1
    today = datetime.date.today().strftime('%Y-%m-%d')
    order = [order_id, 'Dropped off', today, '', '']
    order.extend(enter_order_items())
    SHEET.worksheet('Orders').append_row(order)
    edit_order_by_id(order_id)

def print_main_menu():
    """
    Print a list of commands for the main menu. This function does not handle user
    input, it just prints the list to the terminal. The commands are numbered from
    1 through 5, with a special 0 command to quit the program.
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
        command = input('> ').strip()
        options = {
            '1': enter_new_order,
            '2': find_order_by_id,
            '3': list_dropped_off_orders,
            '4': list_ready_for_pickup_orders,
            '5': list_picked_up_orders,
            '6': list_all_orders,
        }
        if not command: continue
        if command == '0': break
        if command == 'q': break
        if command == 'Q': break
        if command not in options:
            print('Unknown command:', command)
            continue
        print('')
        options[command]()

def main():
    """
    Print a welcome message and some instructions on how to use the program, after
    which the main menu is displayed and run until the program is asked to quit,
    by user input. Finally, print a goodbye message, because it is just polite.
    """
    print('')
    print('Welcome to Rinse and Repeat Dry Cleaning')
    print('----------------------------------------')
    print('Enter menu commands (1 through 6) from the list below using the keyboard.')
    print('Press return to perform the command. To exit the program, enter 0 or Q.')
    main_menu()
    print('')
    print('Goodbye, have a fantastic day!')

main()