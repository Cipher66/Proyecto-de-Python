from flask import Flask
from flask import render_template
import vehiculos_objetos as vobj
#from app import app
#from .forms import LoginForm
app = Flask(__name__)
app.debug=True

#Line to del
@app.route("/")
def pag_principal():
    return render_template("index.html")

@app.route("/vehiculos")
def pag_vehiculos():
    arm = "hola"
    lsv = vobj.vehicles 
    return render_template("vehiculos.html", vc = arm, lv = lsv)

"""def vehiculos():
    vehiculos = vobj.vehiculos_for()
    return str(vehiculos)
    #for i in vobj.vehicles:
        #return str(i)

        #print (i)
    #vehiculo = vobj.my_vehicleAAF_Fighter
    #return str(vehiculo)"""
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