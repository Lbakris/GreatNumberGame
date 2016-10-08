from flask import Flask, render_template, redirect, request
import random
app = Flask(__name__)



@app.route('/')
def Main():
    global count,name
    return render_template('index.html')

@app.route('/try',methods=["post"])
def results():
    name=request.form["name"]
    name = int(name)
    try:
        num!=int
        session['num'] = random.randrange(1,1000000)
    except:
        num=num
    if name<num:
        count="Higher"
    else:
        count="Lower"
    return redirect('/')
app.run(debug=True)
