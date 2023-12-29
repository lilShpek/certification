Создать страницу, на которой будет кнопка "Нажми меня", 
при нажатии на которую будет переход на другую страницу
с приветствием пользователя по имени.


from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    return render_template('greet.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)





# Создать страницу, на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма для загрузки изображений.
    

# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return f'Главная страница'


# @app.route('/page/')
# def page():
#     context = {'title': 'Одна из многих'}
#     return render_template('page.html', **context)


# @app.route('/upload/')
# def upload():
#     return render_template('upload.html')


# if __name__ == '__main__':
#     app.run(debug=True)





# Создать страницу, на которой будет форма для ввода логина и пароля,
# при нажатии на кнопку "Отправить" будет произведена проверка соответствия логина
# и пароля и переход на страницу приветствия пользователя или страницу с ошибкой.



# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# users = {
#     'user1': 'password1',
#     'user2': 'password2'
# }


# @app.route('/')
# def index():
#     return render_template('login.html')


# @app.post('/login/')
# def login():
#     username = request.form['username']
#     password = request.form['password']
#     if username in users and users[username] == password:
#         return redirect(url_for('welcome', username=username))
#     else:
#         return redirect(url_for('block'))


# @app.route('/welcome/<username>')
# def welcome(username):
#     return render_template('welcome.html', username=username)


# @app.route('/block/')
# def block():
#     return render_template('block.html')

# if __name__ == '__main__':
#     app.run(debug=True)



# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить",
# при нажатии на которую будет произведен подсчет количества
# слов в тексте и переход на страницу с результатом.



