from flask import Flask, render_template, session , redirect, request 
import random

app = Flask(__name__)

app.secret_key = "Don't tell"

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,101)
    if 'guess' not in session:
        session['guess'] = None
    return render_template('guess.html')

@app.route('/guess', methods = ['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ =="__main__":
    app.run(debug=True)