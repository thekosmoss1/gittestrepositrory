from flask import Flask, render_template, request
import math

app = Flask(__name__, template_folder='teamplate')

@app.route('/')
def start():
    return render_template('form.html')

@app.route("/submit", methods=['POST'])
def get_data():
    first = int(request.form['first'])
    second = int(request.form['second'])

    return f"<h3>Привет, Гипотенуза={math.sqrt(first**2+second**2)}</h3>"




if __name__ == '__main__':
    app.run(debug=True)
