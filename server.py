import mysql.connector
from email import message
from flask import Flask, render_template, request, session, url_for
# from numpy import empty

app = Flask(__name__)
app.secret_key = 'secret key'


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sara2001",
    database="hemodialysis"
)

mycursor = mydb.cursor(buffered = True)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login&reg')
def log_reg():
    return render_template("signup.html")


@app.route('/log')
def log():
    return render_template("signin.html")


@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/doctor')
def doctor():
    return render_template("doctor.html")


@app.route('/dash')
def dash():
    return render_template("dashboard.html")


@app.route('/doctors')
def doctors():
    return render_template("doctors.html")


@app.route('/opendoctor')
def opendoctor(id):
   mycursor.execute('SELECT * FROM doctor WHERE id = %s', ( id,)) 
   myresult = mycursor.fetchall()
   print(myresult)
   return (myresult)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST' :
        #and 'name' in request.form and 'id' in request.form
        username = request.form['name']
        password = request.form['id']
        isInt = True
        
        try:
            int(username)
        except ValueError:
            isInt = False
        if isInt:
                 error_statment = 'You should enter a text not numbers'
                 return render_template("signin.html",error_statement = error_statment)
        elif len(password) == 0 or len(username)==0:
            error_statement = 'Wrong Password or username.'
            return render_template("signin.html",error_stat = error_statement)
        else:
            mycursor.execute('SELECT flag FROM user WHERE passw =%s',(password,))
            flag = mycursor.fetchone()
            if flag == ("false",):
                msg ="You Can't Login. Call Admin for Response"
                return render_template('signin.html', error=msg)
            else:
                mycursor.execute('SELECT * FROM user WHERE name = %s AND passw = %s ', (username,password,))
                account = mycursor.fetchall()
                if account :
                    mycursor.execute('SELECT role from user WHERE name=%s AND passw =%s',(username,password,))
                    roles= mycursor.fetchone()
                    if roles == ("patient",):
                        msg = "You're a patient"
                        return render_template("signin.html",msg=msg)
                    # session['loggedIn'] = True
                    # session['user'] = username   
                    elif roles ==("doctor",):
                        
                        result = mycursor.execute('SELECT id from user WHERE name=%s AND passw =%s',(username,password,))
                        result = mycursor.fetchone()
                        data = opendoctor(result[0])
                        return render_template("opendoctor.html", data=data )

                        # return render_template('doctor.html', name='Welcome {}'.format(username))
                    # session['loggedIn'] = True
                    # session['user'] = username
                    else :
                        return render_template('admin.html', name='Welcome {}'.format(username))     
                else:
                    msg = " You don't have an account."
                    return render_template('signin.html', error=msg)
                # session['loggedIn'] = True
                # session['user'] = username
                
                


@app.route('/SignUp', methods=["Get", "POST"])
def SignUp():
    if request.method == 'POST' and 'name' in request.form and 'id' in request.form:
        user = request.form['name']
        passw = request.form['id']
        role = request.form['role']
        isInt = True
        try:
            int(user)
        except ValueError:
            isInt = False
        if isInt:
                 error_statment = 'You should enter a text not numbers'
                 return render_template("signup.html",error_statement = error_statment)
             
        elif len(passw) < 8:
            error_statement = 'Password must be 8 characters'
            return render_template('signup.html', error=error_statement, username=user, passwd=passw)
        else:
            error_statement = ''

        if error_statement == '':
            mycursor.execute(
                'SELECT * FROM user WHERE name =%s AND passw =%s AND role=%s', (user, passw, role))
            account = mycursor.fetchone()
            if account:
                error_statement = "You already have an account."

            else:
                if role == "patient":
                    mycursor.execute(
                        'INSERT INTO user (passw,name,role) VALUES( %s, %s,%s)', (passw, user, role))
                    mydb.commit()

                    result = mycursor.execute('SELECT id from user WHERE name=%s AND passw =%s',(user,passw,))
                    result = mycursor.fetchone()

                    mycursor.execute(
                        'INSERT INTO patient (id,name,passw) VALUES( %s, %s,%s)', (result[0], user, passw))
                    mydb.commit()

                    msg = "signup"
                else:
                    s = "false"
                    mycursor.execute(
                        'INSERT INTO user (passw,name,role,flag) VALUES( %s, %s,%s,%s)', (passw, user, role, s))
                    mydb.commit()
                    msg = "signup "

        if error_statement == '':
            return render_template('signup.html', message=msg)
        else:
            return render_template('signup.html', error=error_statement, username=user, passwd=passw)


if __name__ == '__main__':
    app.run(debug=True)
