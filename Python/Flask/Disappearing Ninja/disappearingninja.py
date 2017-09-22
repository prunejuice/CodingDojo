from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)

app.secret_key = 'bcxjnmkbnhbfrvsghfn'

@app.route('/')
def index():

    return render_template("index.html", )

@app.route('/ninjas')
def ninjas():

    if session.get('ninjas') is None:
        session['ninjas'] = []
    session['ninjas'].append({'name': 'images/donatello.jpg'})
    session['ninjas'].append({'name':'images/leonardo.jpg'})
    session['ninjas'].append({'name':'images/michelangelo.jpg'})
    session['ninjas'].append({'name':'images/raphael.jpg'})
    return render_template("ninjas.html", ninjas = session['ninjas'])



@app.route('/ninjas/<vararg>')
def handler_function(vararg):
    session['ninjas'] = []
    if vararg == 'orange':
        session['ninjas'].append({'name': 'images/michelangelo.jpg'})
    elif vararg == 'blue':
        session['ninjas'].append({'name': 'images/leonardo.jpg'})
    elif vararg == 'red':
        session['ninjas'].append({'name': 'images/raphael.jpg'})
    elif vararg == 'purple':
        session['ninjas'].append({'name': 'images/donatello.jpg'})
    else:
        session['ninjas'].append({'name': 'images/notapril.jpg'}) 


    return render_template("ninjas.html", ninjas = session['ninjas'])


app.run(debug=True)
