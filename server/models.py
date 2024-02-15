from config import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    genre = db.Column(db.String)
    pub_year = db.Column(db.Integer)
    page_count = db.Column(db.Integer)
    available = db.Column(db.Integer)

    def __repr__(self):
        return (
            f"Title: {self.title}; Author: {self.author}; Genre: {self.genre}; Pub Year: {self.pub_year}; Page Count: {self.page_count}; Available: {self.available}"
            )
    

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    account_name = db.Column(db.String)
    email = db.Column(db.String, unique = True)

    def __repr__(self):
        return (
            f"User Name: {self.user_name}; Account: {self.account_name} Email: {self.email} Password: {self.password}"
        )
        
class Checkout(db.Model):
    __tablename__ = 'checkouts'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    checkout_date = db.Column(db.String)
    return_date = db.Column(db.String)

    def __repr__(self):
        return (
            f"User ID: {self.user_id}; Book ID: {self.book_id}; Checkout Date: {self.checkout_date}; Return Date: {self.return_date}"
        )

