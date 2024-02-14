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
    if password == user.password and username == user.user_name:
        print('Logged into ' + user.user_name)  
        return user
    elif username != user.user_name:
        print('Invalid username')
    elif password != user.password:
        print('Invalid password')


def get_all_books():
    return db.session.query(Book).all()

def get_book_by_id(id):
  book = Book.query.filter_by(id=id).first()
  return book


