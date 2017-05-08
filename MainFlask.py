from flask import Flask
from flask import render_template
#from app import app
#from .forms import LoginForm
app = Flask(__name__)
app.debug=True

#Line to del
@app.route("/")
def pag_principal():
    return render_template("index.html")
"""
@app.route("/logged_in")    
def logged_in():
"""
"""@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
"""                           
if __name__ == "__main__":
    app.run()