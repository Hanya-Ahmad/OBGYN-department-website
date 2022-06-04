import mysql.connector 
from email import message
from flask import Flask, render_template, request, session, url_for


app = Flask(__name__)
app.secret_key = 'secret key'


mydb = mysql.connector.connect(
    host="localhost",
   user="root",
 passwd="root",
 database="project"
) 



mycursor = mydb.cursor(buffered = True)

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


@app.route('/patient/doctorslist')
def doctors_list():
   return render_template("doctorslist.html")

@app.route('/doctor/doctorslist')
def doctorslist():
    return render_template("doctorslist.html")

@app.route('/admin/doctorslist')
def adminslist():
    return render_template('adminslist.html')


@app.route('/signup', methods=["Get", "POST"])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['firstName']
        last_name= request.form['lastName']
        phone_number= request.form['phoneNumber']
        age= request.form['age']
        e_mail= request.form['e-mail']
        role = "patient"
        isInt = True
        is_found=False
        for letter in e_mail:
            if letter == "@":
                is_found=True
                break
        try:
            int(username)
            
        except ValueError:
            isInt = False
        if isInt:
            error_statement = 'Your username should contain lettres.'
            return render_template("signup.html",error_stat = error_statement)
        elif not is_found:
            error_statement= "Please enter a valid e-mail in the format of abcdef@ghij.klm"
            return render_template("signup.html", error_stat= error_statement)
        elif phone_number.isnumeric()==False or len(phone_number)!=11:
            error_statement = "Pleae enter a valid phone number in the format of 01XXXXXXXXX"
            return render_template("signup.html", error_stat=error_statement)
        elif len(password) < 8 :
            error_statement = 'Your password must contain at least 8 characters'
            return render_template('signup.html', error=error_statement, user_name=username, pass_word=password)
        else:   
            mycursor.execute(
                'SELECT * FROM user WHERE username =%s AND access=%s', (username,role))
            account = mycursor.fetchone()
            if account:
                error_statement = "An account with this username already exists."
                return render_template("signup.html", error_stat=error_statement)

            else:
                #error_statement='no_error'
                if role == "patient":
                    mycursor.execute(
                        'INSERT INTO user (pass,username,access) VALUES( %s, %s,%s)', 
                        (password, username, role))
                    mydb.commit()

                    result = mycursor.execute('SELECT userid from user WHERE username=%s AND pass =%s',(username,password,))
                    result = mycursor.fetchone()
                    patient_id=result[0]

                    mycursor.execute(
                        'INSERT INTO patient (patientid,firstname,lastname,email,age,phone) VALUES( %s, %s,%s, %s, %s, %s)', (patient_id, first_name, last_name, e_mail, age, phone_number))
                    mydb.commit()
                    
                    return render_template('indexpatient.html', user_name=username, pass_word=password)

        return render_template('signup.html')
       # else:
        #if error_statement =='no_error':  
          # return render_template('signup.html', user_name=username, passwordd=password)

@app.route('/login', methods=["GET", "POST"])
def signin():
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['pass']
        role= request.form['access']
        print(username,role)
        
        if len(password) == 0 or len(username)==0 or len(role)==0:
            error_statement = 'Invalid input. Please re-enter your username, password and role correctly.'
            print("hena")
            return render_template("login.html",error_stat = error_statement)
        else:
                print("hena1")
                mycursor.execute('SELECT* FROM user WHERE username = %s AND pass = %s AND access = %s', (username,password,role))
                account = mycursor.fetchall()
                print("account",account)
                if account :
                        print("hena3")
                        if role == ("patient",):
                            print("hena4")
                            return render_template("indexpatient.html")
                        elif role ==("doctor"): 
                            print("hena5")       
                            return render_template("indexdoctor.html")

                        else :
                            print("hena6")
                            return render_template('indexadmin.html')     
                   
                else:
                    print("hena7")
                    error_statement = " There's no such account. Please make sure you enter your correct username, password and role. Or sign up if you don't have an existing account."
                    return render_template('login.html', error=error_statement)

if __name__ == '__main__':
    app.run(debug=True)
