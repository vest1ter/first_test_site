from flask import Flask, request, render_template, redirect, url_for
from models import User, db, add_to_database, print_all_users

app = Flask(__name__)


@app.route('/auth', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']
        
        if login == 'admin' and password == '1234':
            print('------------', login, password, '-------------')
            return redirect(url_for('main'))
    
        else:
            add_to_database(User(login=login, password=password))
    
    return render_template('auth.html')

@app.route('/ma')
def main():
    # Загрузка и отображение главной страницы (landing page)
    return render_template('main.html') 
        
if __name__ == '__main__':
    app.run(debug=True)