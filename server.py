import os.path
import mysql.connector 
from email import message
from flask import Flask, render_template, request, session, url_for


app = Flask(__name__)

mydb= mysql.connector.connect(
   
   host= "localhost",
   user= "root",
   database= "obgyn"

)

mycursor = mydb.cursor()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/createaccount')
def create_account():
    return render_template("signup.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/aboutus')
def info():
    return render_template("about.html")


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contactus')
def contact():
    return render_template('contact.html')


@app.route('/ourservices')
def ser():
    return render_template('services.html')


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/viewdoctor')
def viewdoctor(doctor_id):
   mycursor.execute('SELECT * FROM doctor WHERE id = %s', (doctor_id)) 
   myresult = mycursor.fetchall()
   print(myresult)
   return (myresult)


@app.route('/signup', methods=["Get", "POST"])
def signup():
    if request.method == 'POST' and 'name' in request.form and 'id' in request.form:
        username = request.form['username']
        password = request.form['id']
        role = "patient"
        isInt = True
        try:
            int(username)
        except ValueError:
            isInt = False 
        if isInt:
                 error_statment = 'Your username should contain lettres.'
                 return render_template("signup.html",error_stat = error_statment)
             
        elif len(password) < 8 :
            error_statement = 'Your passwordord must contain at least 8 characters'
            return render_template('signup.html', error=error_statement, user_name=username, pass_word=password)
        else:
            mycursor.execute(
                'SELECT * FROM user WHERE name =%s', (username,))
            account = mycursor.fetchone()
            if account:
                error_statement = "An account with this username already exists."

            else:
                error_statement='no_error'
                if role == "patient":
                    mycursor.execute(
                        'INSERT INTO user (password,name,role) VALUES( %s, %s,%s)', 
                        (password, username, role))
                    mydb.commit()

                    result = mycursor.execute('SELECT id from user WHERE name=%s AND password =%s',(username,password,))
                    result = mycursor.fetchone()
                    patient_id=result[0]

                    mycursor.execute(
                        'INSERT INTO patient (id,name,password) VALUES( %s, %s,%s)', (patient_id, username, password))
                    mydb.commit()
                    
            return render_template('signup.html')
       # else:
        if error_statement =='no_error':  
           return render_template('signup.html', user_name=username, passwordd=password)

@app.route('/login', methods=["GET", "POST"])
def signin():
    if request.method == 'POST' :
        username = request.form['username']
        passwordord = request.form['passwordord']
        
        if len(passwordord) == 0 or len(username)==0:
            error_statement = 'Invalid passwordord or username. Please re-enter your username and passwordord.'
            return render_template("signin.html",error_stat = error_statement)
        else:
            mycursor.execute('SELECT flag FROM user WHERE password =%s',(passwordord,))
            flag = mycursor.fetchone()
            if flag == ("false"):
                error_statement ="Access denied. Please contact the Admin to resolve the issue."
                return render_template('signin.html', error_stat=error_statement)
            else:
                mycursor.execute('SELECT * FROM user WHERE name = %s AND password = %s ', (username,passwordord,))
                account = mycursor.fetchall()
                if account :
                    mycursor.execute('SELECT role from user WHERE name=%s AND password =%s',(username,passwordord,))
                    roles= mycursor.fetchone()
                    if roles == ("patient",):
                        return render_template("signin.html")
                    elif roles ==("doctor",):
                        
                        result = mycursor.execute('SELECT id from user WHERE name=%s AND password =%s',(username,passwordord,))
                        result = mycursor.fetchone()
                        doc_id=result[0]
                        data = viewdoctor(doc_id)
                        return render_template("doctortemplatepending.html", data=data )

                    else :
                        return render_template('admintemplatepending.html')     
                else:
                    msg = " There's no such account. Please make sure you enter your correct username and passwordord, or sign up if you don't have an account."
                    return render_template('signin.html', error=msg)

if __name__ == '__main__':
    app.run(debug=True)
