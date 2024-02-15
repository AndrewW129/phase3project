from models import User, Book, Checkout, db

def create_user(user, password, name, email):

    new_user = User(
        user_name = user,
        password = password,
        account_name = name,
        email = email
    )
    db.session.add(new_user)
    db.session.commit()

def login(username, password):
        user = User.query.filter_by(user_name=username).first()
        if isinstance(user, User):
            if password == user.password and username == user.user_name:
                print('Logged into ' + user.user_name)
            elif username!= user.user_name:
                print('Invalid Username')
            elif password != user.password:
                print('Invalid Password')

def get_all_books():
    return db.session.query(Book).all()

def get_book_by_id(id):
    return Book.query.filter_by(id=id).first()

def get_user_by_username(username):
    return User.query.filter_by(user_name=username).first()

def get_checkout_by_user_id(id):
    return Checkout.query.filter_by(user_id=id).all()


def update_book_title(new_title, book):
    book.title = new_title
    db.session.commit()

def update_book_author(new_author, book):
    book.author = new_author
    db.session.commit()

def update_book_genre(new_genre, book):
    book.genre = new_genre
    db.session.commit()

def update_book_year(new_year, book):
    book.pub_year = new_year
    db.session.commit()

def update_page_count(new_page_count, book):
    book.page_count = new_page_count
    db.session.commit()

def update_book_available(new_amount, book):
    book.available = new_amount
    db.session.commit()

def create_checkout(book, user):
    new_checkout = Checkout(
        user_id = user,
        book_id = book
    )
    print(new_checkout)
    db.session.add(new_checkout)
    db.session.commit()
    print('Book checked out!')

    

def update_user_name(new_username, username):
    user = User.query.filter_by(user_name=username).first()
    user.user_name = new_username
    db.session.commit()
    print('Username changed!')

def update_user_password(new_password, username):
    user = User.query.filter_by(user_name=username).first()
    user.password = new_password
    db.session.commit()
    print('Password changed!')

def update_user_account_name(account_name, username):
    user = User.query.filter_by(user_name=username).first()
    user.account_name = account_name
    db.session.commit()
    print('Account name updated to '+ user.account_name + '!')

def update_user_email(new_email, username):
    user = User.query.filter_by(user_name=username).first()
    user.email = new_email
    db.session.commit()
    print('Email updated to '+ user.email + '!')



