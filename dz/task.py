from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clothing/')
def clothing():
    return render_template('clothing.html')

@app.route('/jacket/')
def jacket():
    return render_template('jacket.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')

if __name__ == '__main__':
    app.run(debug=True)


