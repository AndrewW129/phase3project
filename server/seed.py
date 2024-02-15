from config import app
from models import *


if __name__ == "__main__":
  with app.app_context():
    print('clearing tables...')

    User.query.delete()
    Book.query.delete()
    Checkout.query.delete()

    print('seeding tables...')
    new_users = [
      User(
        user_name = 'William123',
        password = 'W123',
        account_name = 'William',
        email = 'Will123@email.com'),
      User(
        user_name ='Dave123',
        password = 'D123',
        account_name = 'Dave',
        email = 'Dave123@email.com'),
      User(
        user_name = 'Andrew123',
        password = 'A123',
        account_name = 'Andrew',
        email = 'Andrew123@email.com')
    ]
    db.session.add_all(new_users)
    db.session.commit()

    new_books = [
      Book(
        title = 'The Hitchhiker\'s Guide to the Galaxy',
        author =	'Douglas Adam\'s',
        genre = 'Science Fiction',
        pub_year = 1939,
        page_count = 392,
        available = 2),
      Book(
        title = 'Percy Jackson and the Olympians: Vol 1',
        author = 'Rick Riordan',
        genre = 'Sicence Fiction',
        pub_year = 2007,
        page_count = 552,
        available = 1),
      Book(
        title = 'Percy Jackson and the Olympians: Vol 2',
        author = 'Rick Riordan',
        genre = 'Science Fiction',
        pub_year = 2009,
        page_count = 673,
        available = 5)
    ]
    db.session.add_all(new_books)
    db.session.commit()
  
    new_checkouts = [
      Checkout(
        user_id= new_users[1].id, 
        book_id= new_books[2].id),
      Checkout(
        user_id= new_users[0].id,
        book_id= new_books[0].id),
      Checkout(
        user_id= new_users[2].id,
        book_id= new_books[1].id)
    ]
    db.session.add_all(new_checkouts)
    db.session.commit()