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
    session['ninjas'].append({'name': 'donatello.jpg'})
    session['ninjas'].append({'name':'michaelangelo.jpg'})
    session['ninjas'].append({'name':'leonardo.jpg'})
    session['ninjas'].append({'name':'michaelangelo.jpg'})
    return render_template("ninjas.html", ninjas = session['ninjas'])



@app.route('/ninja/<vararg>')
def handler_function(vararg):
    if vararg =

    return render_template


app.run(debug=True)
