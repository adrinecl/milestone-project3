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
      options = {}
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
    print('Welcome to Rinse and Repeat Dry Cleaning')
    print('----------------------------------------')
    print('Enter menu commands (1 through 5) from the list below using the keyboard.')
    print('Press return to perform the command. To exit the program, enter 0 or Q.')
    main_menu()
    print('')
    print('Good bye, have a fantastic day!')

main()