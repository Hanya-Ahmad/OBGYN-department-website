from flask import Flask, request, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import login_required , logout_user , login_user, login_manager , LoginManager, current_user



#!connction to database 

local_server = True
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/obgyn'
db = SQLAlchemy(app)
app.secret_key="1234"




 #!craeating database models (tabels)

class Stafflogin (UserMixin,db.Model):
     staffID=db.Column(db.Integer,primary_key= True) 
     Did=db.Column(db.String(20))
     email=db.Column(db.String(100))
     password=db.Column(db.String(1000))

class User (UserMixin,db.Model):
     Uid=db.Column(db.Integer,primary_key= True) 
     SRFid=db.Column(db.String(20))
     email=db.Column(db.String(20))
     birthdate=db.Column(db.String(20))     

class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))

class Appointment (db.Model):
     appointment_id=db.Column(db.Integer,primary_key= True) 
     SRFid=db.Column(db.Integer)
     patient_name=db.Column(db.String(50))
     patient_phone=db.Column(db.String(20))
     Did=db.Column(db.Integer)
     schedule_id=db.Column(db.Integer)
     appointment_time=db.Column(db.Time)
     appointment_number=db.Column(db.Integer)
     appointment_status=db.Column(db.String(30))
     doctor_comment=db.Column(db.String(1000))

class Doctor (db.Model):
     Did=db.Column(db.Integer,primary_key= True) 
     Dname=db.Column(db.String(100))
     Demail=db.Column(db.String(100))
     Daddress=db.Column(db.String(100))
     Dphone=db.Column(db.String(30))
     Ddatebirth=db.Column(db.Date)
     Ddegree=db.Column(db.String(200))
     Dstatus=db.Column(db.Enum('Active','Inactive'))

class Doctor_schedule (db.Model):
     schedule_id=db.Column(db.Integer,primary_key= True)
     Did=db.Column(db.Integer) 
     schedule_date=db.Column(db.Date)
     schedule_day=db.Column(db.Enum('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'))
     start_time=db.Column(db.String(20))
     end_time=db.Column(db.String(20))
     schedule_status=db.Column(db.Enum('Availabe','not availabe'))

class Inventory (db.Model):
     device_id=db.Column(db.Integer,primary_key= True) 
     device_name=db.Column(db.String(50))
     Did=db.Column(db.Integer)
     device_count=db.Column(db.Integer)
     device_status=db.Column(db.Enum('available','not available'))
     

#! testing if the database is connected or not 

@app.route("/test.html")
def test():
     try:
          a = Test.query.all()
          print(a)
          return 'Database is connected'
     except Exception as e :
          print(e)
          return f'Database is not connected{e}'    


@app.route("/index.html", methods=['POST', 'GET'])
def index():
     return render_template('index.html')
@app.route("/login.html", methods=['POST','GET'])
def login():
     return render_template('login.html')

@app.route("/signup.html",methods=['POST','GET'])
def signup():
     return render_template('signup.html')

@app.route("/about.html", methods=['POST', 'GET'])
def about():
     return render_template('about.html')

@app.route("/contact.html", methods=['POST', 'GET'])
def contact():
     return render_template('contact.html')

@app.route("/gallery.html", methods=['POST', 'GET'])
def gallery():
     return render_template('gallery.html')

@app.route("/icons.html",methods=['POST','GET'])
def icons():
     return render_template('icons.html')

@app.route("/services.html", methods=['POST','GET'])
def services():
     return render_template('services.html')

@app.route("/typography.html",methods=['POST','GET'])
def typography():
     return render_template('typography.html')
if __name__ == '__main__':        

    app.run(debug=True)
