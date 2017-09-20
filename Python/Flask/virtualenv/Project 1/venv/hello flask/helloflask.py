from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
app.secret_key = 'bcxjnmkbnhbfrvsghfn'

@app.route('/')
def index():
    session[ 'count' ] += 1
    return render_template("index.html", count = session [ 'count' ])  # Return 'Hello World!' to the response.


@app.route('/reset', methods=['POST'])
def reset():
    # global name
    session[ 'count' ] = 0
    return redirect('/')


@app.route('/result', methods=['POST'])
def result():
    session [ 'count'] += 1
    return redirect('/')


app.run(debug=True)      # Run the app in debug mode.
