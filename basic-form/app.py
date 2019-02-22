# importing the flask class
from flask import Flask
from flask import render_template
# for HTTP METHODS
from flask import request

# instantiating the Flask class
# the first argument is the name of the application's module or package
# if you using a single module, you should use __name__

app = Flask(__name__)

#uhh... where is this page... OH!
# http://localhost:5000/hello
# got it!
# THIS IS REALLY COOL!
# This together with hello_form.html creates an official submit form! woo!
@app.route('/hello', methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")
 
 # only run this script if python app.py is run in the command line
# serves the purpose of making this code snippet portable into
# other programs without opening up a server.
if __name__ == "__main__":
    app.run()
