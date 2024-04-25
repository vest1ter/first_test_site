from flask import Flask, request, render_template, redirect, url_for, session, flash
import secrets
from models import User, db, add_to_database, print_all_users, get_user

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)



@app.route('/main')
def main():
    # Проверяем, авторизован ли пользователь
    if 'username' in session:
        # Если пользователь авторизован, передаем информацию о пользователе в шаблон
        return render_template('main.html', user_authenticated=True)
    else:
        # Если пользователь не авторизован, передаем информацию о неавторизованном пользователе в шаблон
        return render_template('main.html', user_authenticated=False)



@app.route('/auth', methods=['GET', 'POST'])
def auth():
    '''
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']
        email = request.form['email']

        session['username'] = login
        
        if login != None and password != None:
            print('------------', login, password, '-------------')
            return redirect(url_for('main'))
    
        else:
            add_to_database(User(login=login, password=password, email = email))
    '''
    return render_template('auth.html')

@app.route('/signin', methods=['POST'])
def signin():
    login = request.form['username']
    password = request.form['password']

    session['username'] = login

    this_user = get_user(login)

    if this_user != None and this_user.password == password:
        redir = True
    else:
        redir = False

    if redir:
        print('------------', login, password, this_user.login, this_user, '-------------')
        return redirect(url_for('main'))
    
    else:
        #add_to_database(User(login=login, password=password, email = email))
        flash("wertyuiopojhgfcxcghjkl")
        print('--------------------------------------------------------')
        return render_template('auth.html', input_class='form-control-error')


@app.route('/profile')
def profile():
    user = get_user(session['username'])

    print("/////////", user.login, session['username'])


    # Проверяем, авторизован ли пользователь
    if 'username' in session:

        # Если пользователь авторизован, перенаправляем его на страницу профиля
        return render_template('profile.html', user_login = user.login, user_email = user.email)
    else:
        # Если пользователь не авторизован, перенаправляем его на страницу входа или регистрации
        return redirect(url_for('auth'))  # Замените 'login' на ваш маршрут для страницы входа
    





if __name__ == '__main__':
    app.run(debug=True)