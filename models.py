from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
#db.init_app(app)

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    login = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

def add_to_database(instance):
    """
    Добавляет экземпляр класса в базу данных.
    
    :param instance: Экземпляр класса, который нужно добавить в базу данных.
    """
    with app.app_context():
        db.session.add(instance)
        db.session.commit()
        return 'succsess'

def print_all_users():
    with app.app_context():
        # Получаем всех пользователей из базы данных
        all_users = User.query.all()
        
        # Выводим информацию о каждом пользователе
        for user in all_users:
            print(f"ID: {user._id}, Login: {user.login}, Password: {user.password}, Email: {user.email}")

def get_user(username):
    with app.app_context():
        # Получаем всех пользователей из базы данных
        this_user = User.query.filter_by(login=username).first()
        print("---------dsd-----", this_user)
        # Выводим информацию о каждом пользователе
        return this_user


# Пример использования функции для добавления пользователя в базу данных
if __name__ == "__main__":
    with app.app_context():
        db.create_all()