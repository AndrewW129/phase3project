from seed import *
from db_utils import *
from models import *


def display_welcome():
  print('*** Welcome to CLIbrary... We have all kinds of CRUD! ***')

def get_welcome_name():
  return (
    print('Enter your first & last name:'),
    input('>>')
  )

def display_main_menu():
  print('*** Select a menu option, ' + welcome_name + ' ***')
  print('1.) Create an account')
  print('2.) Log in')
  print('3.) See all Books')
  print('4.) Exit')

def get_main_selection():
  print('Enter a number: ')
  return input('>>')

def create_an_account():
  new_user_name = input('Username: ')
  new_password = input('Password: ')
  new_account_email = input('Account Email: ')

  create_user(new_user_name, new_password, welcome_name, new_account_email)
  print('Account created, Thanks for joining CLIbrary ' + new_user_name + '!')

def check_account():
  print('Enter your username:')
  username = input('>>')
  print('Enter your password:')
  password = input('>>')
  login(username, password)

def display_all_books():
  books = get_all_books()
  for book in books:
    print(f"{book.id} Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Pub Year: {book.pub_year}, Page Count: {book.page_count}, Available: {book.available}")

def display_user_menu():
  print('*** Select a menu option ***')
  print('1.) Manage Books') # ADD/DELETE BOOK/BOOK REVIEW FROM USER
  print('2.) Checkout/Checkin a book') #ADD OR REMOVE FROM USERS BOOKS
  print('3.) Search books') #SEARCH ALL BOOKS FOR SPECIFIC BOOKS
  print('4.) See all Books')
  print('5.) Log out') #LOG OUT

def get_user_selection():
  print('Enter a number')
  return input('>>')

def search_book_by_id():
   print('Enter an ID')
   search_id = input('>>')
   book = get_book_by_id(search_id)
   print(f"{book.id} Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Pub Year: {book.pub_year}, Page Count: {book.page_count}, Available: {book.available}")

def check_book_available():
    print('Enter an ID')
    search_id = input('>>')
    book = get_book_by_id(search_id)
    if (book.available == True):
        print('Book is available')
    elif (book.available == False):
        print('Book is not available')

def display_book_menu():
  print('*** Select a menu option ***')
  print('1.) Add a book')
  print('2.) Delete a book')
  print('3.) Review a book')
  print('4.) Delete a Review')
  print('5.) Return to User Menu')

def get_bookmenu_selection():
  print('Enter a number')
  return input('>>')
  
if __name__ == "__main__":
  with app.app_context():

    display_welcome()

    print('What is your name?')
    welcome_name = input('>>')

    while True:
      
      display_main_menu()
      main_selection = get_main_selection()
      print('You selected:' + main_selection)

      if (main_selection == '1'):
        print('Fantastic! Let\'s make an account...')
        create_an_account() 


      elif (main_selection == '2'):
        print('Welcome back!')

        check_account() #AFTER LOG IN GO TO LOGGED IN MENU
        display_user_menu() #DISPLAY THE USER MENU AFTER LOG IN

        user_selection = get_user_selection()

        logged_in = True

        if (user_selection == '1'):
            print('Manage Book menu!')    

            bmenu_selection = display_book_menu()

            if (bmenu_selection == '1'):
                print('Add a book!')
            elif (bmenu_selection == '2'):
                print('Delete a book!')
            elif (bmenu_selection == '3'):
                print('Review a book!')
            elif (bmenu_selection == '4'):
                print('Delete a review!')
            else:
                break

        elif (user_selection == '2'):
            print('Checkin/Checkout Book!')
            check_book_available()
            search_book_by_id()
            


        elif (user_selection == '3'):
            display_all_books()
            print('Which book would you like to view more details on?')
            search_book_by_id()

        elif (user_selection == '4'):
            display_all_books()
            print('Here are all the books!')
        else:
            break

      elif (main_selection == '3'):
        print('Searching for books') #SEARCH BOOKS
        display_all_books()
      else:
        break