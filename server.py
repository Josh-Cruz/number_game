from flask import Flask, render_template, request, flash, session
import random
app = Flask(__name__)
app.secret_key = "sunday"

@app.route('/', methods = ['GET','POST'])
def number_guess():
    if 'guess' not in session:
        session['guess'] = 0
    if 'addclass' not in session:
        session['addclass'] = "class ='.d-none'"
    if 'rand_num' not in session:
        session['rand_num'] = random.randrange(0, 101)  # random number between 0-100
        print session['rand_num']
    if request.method =='POST':
        session['guess'] = request.form['user_guess']
        if session['guess'] < session['rand_num']:
            flash("your lower")
            session['addclass'] = "class =''"
        elif session['guess'] > session['rand_num']:
           flash ("its higher")
        elif session['guess'] == session['rand_num']:
            flash("correct")
    elif request.method == 'GET':
        pass
    return render_template('index.html')
    
   
app.run(debug=True)
