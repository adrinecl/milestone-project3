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
      '3': list_dropped_off_orders,
      '4': list_ready_for_pickup_orders,
      '5': list_picked_up_orders
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
    by user input. Finally, print a good bye message, because it is just polite.
    """
    print('')
    print('Welcome to Rinse and Repeat dry cleaning')
    print('----------------------------------------')
    print('Enter menu commands (1 through 5) from the list below using the keyboard.')
    print('Press return to perform the command. To exit the program, enter 0 or Q.')
    main_menu()
    print('')
    print('Good bye, have a fantastic day!')

main()