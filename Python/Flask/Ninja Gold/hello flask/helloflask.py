from flask import Flask, render_template, request, redirect, session
import random, datetime  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
app.secret_key = 'bcxjnmkbnhbfrvsghfn'

@app.route('/')
def index():

    if session.get('count') is None:
        session['count'] = 0

    if session.get('history') is None:
        session['history'] = []


    # try:
    #     session[ 'count' ] += 0
    # except KeyError:
    #     session[ 'count' ] = 0
    return render_template("index.html", count = session['count'], history = session['history'])  # Return 'Hello World!' to the response.


# @app.route('/reset', methods=['POST'])
# def reset():
#     # global name
#     session[ 'count' ] = 0
#     return redirect('/')

@app.route('/process_money', methods=['POST'])
def result():
    currenttime = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
    newVal = 0
    message = ""
    if request.form['action'] == "farm":
        newVal = random.randint(10,20)
        message = "Earned " + str(newVal) + " from the farm! "
    elif request.form['action'] == "cave":
        newVal = random.randint(5,10)
        message = "Earned " + str(newVal) + " from the cave! "
    elif request.form['action'] == "house":
        newVal = random.randint(2,5)
        message = "Earned " + str(newVal) + " from the house! "
    elif request.form['action'] == "casino":
        newVal = random.randint(-50,50)
        if newVal < 0:
            message = "Entered a casino and lost " + str(abs(newVal)) + " gold... Ouch.. "
        else:
            message = "Entered a casino and won " + str(newVal) + " gold... Woo! "

    elif request.form['action'] == "reset":
        session['count'] = 0

    # set result to count
# get time
    # add history line
    session['count'] += newVal
    session['history'].append({'message': message + "("+currenttime +")", 'value': newVal})

    return redirect('/')


app.run(debug=True)      # Run the app in debug mode.
