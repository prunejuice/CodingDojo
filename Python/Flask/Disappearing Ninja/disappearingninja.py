from flask import Flask, render_template, request, redirect, session
import random, datetime
app = Flask(__name__)

ninja_dict = {
    'purple': 'images/donatello.jpg',
    'blue': 'images/leonardo.jpg',
    'red': 'images/raphael.jpg',
    'orange': 'images/michelangelo.jpg'
}
app.secret_key = 'bcxjnmkbnhbfrvsghfn'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas/')
def ninjas():
    return render_template("ninjas.html", ninjas = ninja_dict)

@app.route('/ninjas/<vararg>')
def handler_function(vararg):
    url = ninja_dict.get(vararg, 'images/notapril.jpg')

    return render_template("ninjas.html", ninjas = {'chosen': url})

app.run(debug=True)
