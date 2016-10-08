from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)

app.secret_key="I love the coding dojo"

@app.route('/')
def HOME():
    if 'staticnum' not in session:
        session['staticnum']=random.randrange(1,100)
    return render_template("/index.html")

@app.route('/try',methods=["post"])
def retry():
    number = request.form['number']
    number = int(number)
    if session['staticnum']<number:
        session['advice']='Lower'
    elif session['staticnum']==number:
        session.clear()
        session['advice']="got it! New Number Try again"
    else:
        session['advice']='higher'
    return redirect('/')
app.run(debug=True)
