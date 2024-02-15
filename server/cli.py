from seed import *
from db_utils import *
from models import *


def display_welcome():
  print('****** Welcome to CLIbrary! ******')
logged_in_account = False
def display_main_menu():
  print('****** Select A Main Menu Option! ******')
  print('1.) Create An Account')
  print('2.) Log In')
  print('3.) Update An Account')
  print('4.) See All Books')
  print('5.) Exit')

def get_selection():
  print('Enter a number: ')
  return input('>>')

def create_an_account():
  print('Create a Username:')
  new_user_name = input('Username: ')
  print('Create a Password: ')
  new_password = input('Password: ')
  print('Create an Account Name:')
  new_account_name = input('Account Name:')
  print('Enter Your Email:')
  new_account_email = input('Email: ')

  create_user(new_user_name, new_password, new_account_name, new_account_email)
  print('Account created, Thanks for joining CLIbrary ' + new_account_name + '!')

def check_account():
  print('Enter your username:')
  username = input('>>')
  print('Enter your password:')
  password = input('>>')
  if isinstance(username, str) and isinstance(password, str or int):
     login(username, password)

def display_all_books():
  books = get_all_books()
  for book in books:
    print(f"{book.id} Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Pub Year: {book.pub_year}, Page Count: {book.page_count}, Available: {book.available}")

def display_user_menu():
  print('****** Select A User Menu Option ******')
  print('1.) Manage Books') # ADD/DELETE BOOK/BOOK REVIEW FROM USER
  print('2.) Check-Out/View Checkouts') #ADD OR REMOVE FROM USERS BOOKS
  print('3.) Search Books') #SEARCH ALL BOOKS FOR SPECIFIC BOOKS
  print('4.) Return to Main Menu') #LOG OUT

def search_book_by_id(): 
   print('Enter an ID')
   search_id = input('>>')
   book = get_book_by_id(search_id)
   print(f"{book.id} Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Pub Year: {book.pub_year}, Page Count: {book.page_count}, Available: {book.available}")

def display_book_menu():
  print('****** Select A Book Menu Option ******')
  print('1.) Add a Book')
  print('3.) Delete a Book')
  print('2.) Update a Book')
  print('4.) Find Book Quanity')
  print('5.) Return to Main Menu')

def add_book():
   print('Book Title: ')                
   title = input('>>')
   print('Author: ')
   author = input('>>')
   print('Genre: ')
   genre = input('>>')
   print('Publication Year: ')
   pub_year = input('>>')
   print('Enter a page count:')
   page_count = input('>>')
   print('Amount of Available Books:')
   available = input('>>')
   new_book = Book(title = title, author = author, genre = genre, pub_year = pub_year, page_count = page_count, available = available)
   print('Adding your book!')
   db.session.add(new_book)
   db.session.commit()
   print('Your book has been added')

def delete_book():
   print('Enter the ID of the book you want to delete:')
   book_id = input('>>')
   book = get_book_by_id(book_id)
   print(f"{book.id} Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Pub Year: {book.pub_year}, Page Count: {book.page_count}, Available: {book.available}")
   db.session.delete(book)
   db.session.commit()
   print('Your book has been deleted')

def display_book_update_menu():
   print('****** Book Update Menu  ******')
   print('1.) Title')
   print('2.) Author')
   print('3.) Genre')
   print('4.) Publication Year')
   print('5.) Page Count')
   print('6.) Available')
   print('7.) Return to Main Menu')

def update_book():
   print('Enter the ID of the book you want to update')
   book_id = input('>>')
   book = get_book_by_id(book_id)
   display_book_update_menu()
   print('Enter the number for the detail you would like to update')
   umenu_selection = get_selection()

   if (umenu_selection == '1'):
      print('New Title:')
      new_title = input('>>')
      update_book_title(new_title, book)
   
   elif (umenu_selection == '2'):
      print('New Author:')
      new_author = input('>>')
      update_book_author(new_author, book)
    
   elif (umenu_selection == '3'):
      print('New Genre:')
      new_genre = input('>>')
      update_book_genre(new_genre, book)
  
   elif (umenu_selection == '4'):
      print('New Pub Year:')
      new_year = input('>>')
      update_book_year(new_year, book)
  
   elif (umenu_selection == '5'):
      print('New Page Count:')
      new_page_count = input('>>')
      update_page_count(new_page_count, book)
    
   elif (umenu_selection == '6'):
      print('New Amount:')
      new_amount = input('>>')
      update_book_available(new_amount, book)

   else:
      print('returning to main menu')

def book_quanity():
   print('Enter ID to get book\'s quanity: ')
   book_id = input('>>')
   book = get_book_by_id(book_id)
   print(f"Available Copies: {book.available}")

def display_checkout_menu():
   print('****** Check-Out Menu ******')
   print('1.) Check-Out a Book')
   print('2.) View Checkouts')
   print('3.) Return to Main Menu')

def check_out_book():
  print('Enter the ID of the book you want to check-out:')
  id = input('>>')
  book = get_book_by_id(id)
  print('Enter your username:')
  username = input('>>')
  user = get_user_by_username(username)
  create_checkout(book.id, user.id)
  book.available -= 1

def view_user_checkouts():
   print('Enter user ID to view all checkouts:')
   id = input('>>')
   checkouts = get_checkout_by_user_id(id)
   print(checkouts)

def display_user_update_menu():
   print('****** What would you like to update ******')
   print('1.) Username')
   print('2.) Password')
   print('3.) Account Name')
   print('4.) Email')
   print('4.) Return to Main Menu')

def update_username():
   print('Enter your new username:')
   new_username = input('>>')
   update_user_name(new_username, username)

def update_password():
   print('Enter your new password:')
   new_password = input('>>')
   update_user_password(new_password, username)

def update_account_name():
   print('Enter your new account name:')
   new_account_name = input('>>')
   update_user_account_name(new_account_name, username)

def update_email():
   print('Enter your new email:')
   new_email = input('>>')
   update_user_email(new_email, username)

if __name__ == "__main__":
  with app.app_context():
    display_welcome()

    while True:
      
      display_main_menu()
      main_selection = get_selection()

      if (main_selection == '1'):
        print('Create an account!')
        create_an_account() 

      elif (main_selection == '2'):
        print('Login To View Your Menu!')

        check_account()
         #AFTER LOG IN GO TO LOGGED IN MENU
        logged_in_account = True
        display_user_menu() #DISPLAY THE USER MENU AFTER LOG IN
        user_selection = get_selection()

        if (user_selection == '1'):   
            display_book_menu()
            bmenu_selection = get_selection()

            if (bmenu_selection == '1'):
                print('Add a Book!')
                new_book = add_book()

            elif (bmenu_selection == '2'):
                print('Delete a Book!')
                deleted_book = delete_book()

            elif (bmenu_selection == '3'):
                print('Update a Book!')
                updated_book = update_book()

            elif (bmenu_selection == '4'):
                print('Getting Book Quanity!')
                book_quanity_total = book_quanity()

            else:
              break

        elif (user_selection == '2'):
            print('Checkin/Checkout Book!')
            display_checkout_menu()
            checkout_selection = get_selection()

            if (checkout_selection == '1'):
                print('Check-Out a Book!')
                check_out_book()
            
            elif (checkout_selection == '2'):
                print('View Books You checked out!')
                view_user_checkouts()

            else:
              break
            
        elif (user_selection == '3'):
            display_all_books()
            print('Which book would you like to view more details on?')
            search_book_by_id()
            
        else:
          break

      elif (main_selection == '3'):
        print('Enter the username for the account you want to update')
        username = input('>>')
        display_user_update_menu()
        update_selection = get_selection()

        if (update_selection == '1'):
          print('Update Username!')
          update_username()

        elif (update_selection == '2'):
          print('Update Password!')
          update_password()

        elif (update_selection == '3'):
          print('Update Account Name!')
          update_account_name()

        elif (update_selection == '4'):
          print('Update Email!')
          update_email()

        else:
           break
        
      elif (main_selection == '4'):
        print('Gathering Books to Display') #SEARCH BOOKS
        display_all_books()

      else:
        break