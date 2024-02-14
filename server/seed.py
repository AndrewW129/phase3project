from config import app
from datetime import date, timedelta

from models import *


def display_welcome():
  print('*** Welcome to CLIbrary... We have all kinds of CRUD! ***')

def get_welcome_name():
  return (
    print('Enter your first & last name:'),
    input('>>')
  )

def display_main_menu():
  print('*** Hello, '+ welcome_name + '! What would you like to do? ***')
  print('1.) Create an account')
  print('2.) Log in')
  print('3.) Search Books')
  print('4.) Exit')

def get_main_selection():
  return input('Enter a number: ')

def create_an_account():
  new_user_name = input('Username: ')
  new_password = input('Password: ')
  new_account_email = input('Account Email: ')

  new_user = User(
    user_name = new_user_name,
    password = new_password,
    account_name = welcome_name,
    account_email = new_account_email
  )

  db.session.add(new_user)
  db.session.commit()


if __name__ == "__main__":
  with app.app_context():

    display_welcome()

    print('What is your name?')
    welcome_name = input('>>')

    first_name = welcome_name.split(' ')

    print(first_name)

    while True:

      display_main_menu()
      selection = get_main_selection()
      print('You selected:' + selection)
      if (selection == '1'):
        print('Fantastic! Let\'s make an account...')
        create_an_account()
      elif (selection == '2'):
        print('Welcome back')
      elif (selection == '3'):
        print('search books')
      else:
        break

    # print('Let\'s get started...')

    # new_name = input('What is your name: ')

    # print('Hello ' + new_name + '! What would you like to do?')
    # print('1.) Log in')
    # print('2.) Create an account')
    # print('2.) View Books')
    # print('3.) Exit')

    # response = input('Enter a number: ')

    # if (response == '1'):
    #   new_account_name = new_name
    #   new_user_name = input('Enter an a username: ')
    #   new_password = input('Enter a password: ')
    #   new_account_email = input('Enter an email: ')

    #   new_user = User(
    #     user_name = new_user_name,
    #     password = new_password,
    #     account_name = new_account_name,
    #     account_email = new_account_email
    #   )

    #   db.session.add(new_user)
    #   db.session.commit()

    #   print('Your account has been created successfully!')
      
    


    # print('clearing tables...')

    # User.query.delete()
    # Book.query.delete()
    # Checkout.query.delete()
    
    # print('seeding user table...')

    # new_users = [
    #   User(
    #     user_name = 'John',
    #     email = 'john123@email.com'
    #   ),
    #   User(
    #     user_name = 'Joe',
    #     email = 'joe123@email.com'
    #   ),
    #   User(
    #     user_name = 'Mary',
    #     email ='mary123@email.com'
    #   )
    # ]
    # db.session.add_all(new_users)
    # db.session.commit()

    # print('seeding book table...')
    # new_books = [
    #   Book(
    #     title = 'The Hitchhiker\'s Guide to the Galaxy',
    #     author = 'Douglas Adam\'s',
    #     genre = 'Science Fiction',
    #     pub_year = 1939,
    #     page_count = 392,
    #     available = True
    #   ),
    #   Book(
    #     title = 'Percy Jackson and the Olympians: Vol 1',
    #     author = 'Rick Riordan',
    #     genre = 'Science Fiction',
    #     pub_year = 2007,
    #     page_count = 552,
    #     available = True
    #   ),
    #   Book(
    #     title = 'Percy Jackson and the Olympians: Vol 2',
    #     author = 'Rick Riordan',
    #     genre = 'Science Fiction',
    #     pub_year = 2009,
    #     page_count = 673,
    #     available = True
    #   )
    # ]
    # db.session.add_all(new_books)
    # db.session.commit()

    # print('seeding checkout table...')
    # new_checkouts = [
    #   Checkout(
    #     user_id = new_users[2].id,
    #     book_id = new_books[1].id,
    #     checkout_date = date.today(),
    #     return_date = date.today() + timedelta(weeks=2)
    #   ),
    #   Checkout(
    #     user_id = new_users[0].id,
    #     book_id = new_books[1].id,
    #     checkout_date = date.today(),
    #     return_date = date.today() + timedelta(weeks=2)

    #   ),
    #   Checkout(
    #     user_id = new_users[1].id,
    #     book_id = new_books[2].id,
    #     checkout_date = date.today(),
    #     return_date = date.today() + timedelta(weeks=2)
    #   )
    # ] 
      
    # db.session.add_all(new_checkouts)
    # db.session.commit()

    # remove pass and write your seed data
