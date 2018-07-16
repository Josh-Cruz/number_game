from flask import Flask, render_template, request, flash, session
import random
app = Flask(__name__)
app.secret_key = "sunday"

@app.route('/', methods = ['GET','POST'])
def number_guess():
    message = ""
    reset = '"hidden"'
    if 'guess' not in session:
        session['guess'] = 0
    if 'rand_num' not in session:
        session['rand_num'] = int(random.randrange(0, 101))  # random number between 0-100
        print(session['rand_num'])
    if request.method =='POST':
        if request.form['submit'] == 'submit':
            session['guess'] = int(request.form['user_guess'])
            print(session['rand_num'])
            if session['guess'] < session['rand_num']:
                message = "your  too low"
            elif session['guess'] > session['rand_num']:
                message = "your too high"
            elif session['guess'] == session['rand_num']:
                message = session['rand_num'], "Is correct!"
                reset = 'submit'
        elif request.form['submit'] == 'reset':
            # message = ""
            # reset = 'hidden'
            # session['guess'] = 0
            # session['rand_num'] = int(random.randrange(0, 101))
            # return render_template('index.html')
            print "reset hit"
        return render_template('index.html', message = message, reset = reset)
    elif request.method == 'GET':
        return render_template('index.html')
        
    
   
app.run(debug=True)
