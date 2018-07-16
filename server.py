from flask import Flask, render_template, request, flash, session
import random
app = Flask(__name__)
app.secret_key = "sunday"

@app.route('/', methods = ['GET','POST'])
def number_guess():
    # message = ""
   
    if 'guess' not in session:
        session['guess'] = 0
    if 'rand_num' not in session:
        session['rand_num'] = random.randrange(0, 101)  # random number between 0-100
    
    if request.method =='POST':
        session['guess'] = request.form['user_guess']
        print (session['guess'])
        print (session['rand_num'])
        if session['guess'] < session['rand_num']:
            # message = "your  too low"
            print ("TOO LOW")

        elif session['guess'] > session['rand_num']:
        #     session['message'] = "your too high"
            print ("TOO HIGH")
            print("session guess is:" + session['guess'])
        elif session['guess'] == session['rand_num']:
            # session['message'] = "OH YEAH! correct"
            print ("JUST RIGHT")
        return render_template('index.html')
    elif request.method == 'GET':
        return render_template('index.html')
        
    
   
app.run(debug=True)
