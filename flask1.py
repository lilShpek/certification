from flask import Flask

app = Flask(__name__)


@app.route("/strng/<strng>/")
def lenght(strng):
    return f"Длина строки {len(strng)}"


html = '''
<h1>Hello</h1>
<p>Hello python and Flask</p>
'''

@app.route("/text/")
def index():
    return html


if __name__ == "__main__":
    app.run(debug=True)




