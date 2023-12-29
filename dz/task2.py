from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet/', methods=['POST'])
def greet():
    username = request.form['username']
    email = request.form['email']

    
    response = make_response(render_template('greet.html', username=username))
    response.set_cookie('user_data', f'{username},{email}')
    
    return response

@app.route('/logout/')
def logout():
    
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('user_data')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)


