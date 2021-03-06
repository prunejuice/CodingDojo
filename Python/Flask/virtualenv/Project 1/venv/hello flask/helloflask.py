from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
app.secret_key = 'bcxjnmkbnhbfrvsghfn'

@app.route('/')
def index():
    return render_template("index.html")


app.run(debug=True)      # Run the app in debug mode.
