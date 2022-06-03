from flask import Flask, request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import login_required , logout_user , login_user, login_manager , LoginManager, current_user 

app = Flask(__name__)
<<<<<<< HEAD
@app.route("/", methods=['POST', 'GET'])
def indexpatient():
     return render_template('indexpatient.html')
@app.route("/doctor", methods=['POST', 'GET'])
def indexdoctor():
     return render_template('indexdoctor.html')
@app.route("/admin", methods=['POST', 'GET'])
def indexadmin():
     return render_template('indexadmin.html')
@app.route("/doctor/myappointments", methods=['POST', 'GET'])
def myappointments():
     return render_template('myappointments.html')
@app.route("/admin/appointments",methods=['POST','GET'])
def allappointments():
     return render_template("myappointments.html")

     
=======

@app.route("/index.html", methods=['POST', 'GET'])
def index():
     return render_template('index.html')
>>>>>>> 497a4dc9c7d013c1cd7a0fd29958714d21054846
@app.route("/login.html", methods=['POST','GET'])
def login():
     if request.method =="POST" :
          access=str(request.form['access'])
          if access=='patient':
              return render_template('indexpatient.html') 
          if access=='doctor':
               return render_template('indexdoctor.html')
          if access=='admin':
               return render_template('indexadmin.html',access=access)
         
     else:
          return render_template('login.html')

@app.route("/signup.html",methods=['POST','GET'])
def signup():
      if request.method =="POST" :
          name=str(request.form['name'])
          return render_template('indexpatient.html', name=name)
         
      else:
          return render_template('signup.html')

@app.route("/patient/list", methods=['POST', 'GET'])
def list():
     return render_template('doctorslist.html')

@app.route("/admin/list", methods=['POST', 'GET'])
def listadmin():
     return render_template('adminlist.html')
@app.route("/doctor/inventory", methods=['POST','GET'])
def doctorinventory():
     return render_template('doctorinventory.html')
@app.route("/admin/inventory",methods=['POST','GET'])
def admininventory():
     return render_template("admininventory.html")
@app.route("/contact.html", methods=['POST', 'GET'])
def contact():
     return render_template('contact.html')



if __name__ == '__main__':        

    app.run(debug=True)
