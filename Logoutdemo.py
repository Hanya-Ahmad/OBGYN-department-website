import mysql.connector 
from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret key'


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="obgyn2"
)


mycursor = mydb.cursor(buffered = True)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/patient')
def indexpatient():
    return render_template("indexpatient.html")

@app.route('/admin')
def indexadmin():
    return render_template("indexadmin.html")

@app.route('/doctor')
def indexdoctor():
    return render_template("indexdoctor.html")



@app.route('/signup')
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




@app.route('/ourservices')
def ser():
    return render_template('services.html')



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
        username = request.form['username'].lower()
        password = request.form['pass']
        first_name = request.form['fname'].capitalize()
        last_name= request.form['lname'].capitalize()
        phone_number= request.form['phone']
        age= request.form['age']
        e_mail= request.form['email']
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
        elif age.isnumeric() == False:
            error_statement = "Please enter a valid age."
            return render_template("signup.html", error_stat=error_statement)
        elif int(age) >120:
            error_statement = "Please enter your correct age in years."
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
                    session['id']=patient_id
                    mycursor.execute('INSERT INTO patient (patient_id,patient_password,patient_first_name,patient_last_name,patient_email_address,patient_age,patient_phone_no) VALUES( %s, %s,%s, %s, %s, %s,%s)', (patient_id, password,first_name, last_name, e_mail, age, phone_number,))
                    mydb.commit()
                    
                    return render_template('indexpatient.html', user_name=username, pass_word=password)

        return render_template('signup.html')

@app.route('/login', methods=["GET", "POST"])
def signin():
    print("0")
    if request.method == 'POST' :
        username = request.form['username'].lower()
        password = request.form['pass']
        role= request.form['access']
        mycursor.execute('SELECT * FROM user WHERE username = %s AND pass = %s AND access = %s', (username,password,role))
        account = mycursor.fetchall()
        print("17")
        if account :
                mycursor.execute('SELECT userid from user WHERE username=%s AND pass =%s',(username,password,))
                result = mycursor.fetchone()
                session["id"]=result
                mycursor.execute('SELECT access from user WHERE username=%s AND pass =%s',(username,password,))
                result =mycursor.fetchone()
                session["role"]=result[0]
                if role == ("patient"):
                    return render_template("indexpatient.html",username=username)
                    print("2")
                elif role ==("doctor"):        
                    return render_template("indexdoctor.html",username=username)
                    print("3")

                else :
                            return render_template('indexadmin.html',username=username)     
                            print("4")
                   
        else:
                error_statement = " There's no such account. Please make sure you enter your correct information."
                return render_template('login.html', username=username, error=error_statement)
                print("5")
@app.route('/contactus',methods=['POST','GET'])
def contact():
    
    return render_template('contact.html')

@app.route("/logout",methods=['POST','GET'])
def logout():
    session["id"] = None
    session["role"]= None
    return redirect("/")

@app.route('/doctor/myappointments',methods=['GET','POST'])
def my_appointments():
    mycursor.execute('SELECT patient_id, booked_appointment_date, booked_appointment_time, doctor_comment FROM booked_appointment WHERE doctor_id = %s',(session["id"]))
    result=tuple(mycursor.fetchall())
    return render_template("myappointments.html", data= result)


@app.route('/admin/doctorsappointment', methods=['GET','POST'])
def admin_doctors_appointments():
    if session['role'] != "admin":
        return redirect('/')
    else:
        mycursor.execute('SELECT patient_id, doctor_id, booked_appointment_date, booked_appointment_time, doctor_comment FROM booked_appointment WHERE past_or_upcoming = "past"')
        past=tuple(mycursor.fetchall())
        mycursor.execute('SELECT patient_id, doctor_id, booked_appointment_date, booked_appointment_time, doctor_comment FROM booked_appointment WHERE past_or_upcoming = "upcoming"')
        upcoming=tuple(mycursor.fetchall())
        header= ("Patient ID","Doctor ID", "Appointment Date", "Appointment Time", "Doctor's Comment")
        return render_template("allappointments.html",past_appointments=past, upcoming_appointments=upcoming, head= header)

@app.route('/patient/availableappointments')
def avaialable_appointments():
    
    if session['role']== "patient":
        mycursor.execute('SELECT doctor_name, available_appointment_date, available_appointment_time FROM doctor INNER JOIN available_appointment USING (doctor_id)')
        data=tuple(mycursor.fetchall())
        mycursor.execute('SELECT doctor_name FROM doctor INNER JOIN available_appointment USING (doctor_id)')
        doctors_list=mycursor.fetchall()
        doctors=[]
        for dr in doctors_list:
            doctors.append(dr[0])
        doctors=tuple(doctors)
        mycursor.execute('SELECT available_appointment_date FROM available_appointment INNER JOIN doctor USING (doctor_id)')
        dates=mycursor.fetchall()
        strings_of_dates=[]
        for date in dates:
            extract_date=date[0]
            strings_of_dates.append(extract_date.strftime("%Y-%m-%d"))
        times=tuple(mycursor.fetchall())
        new_dates=tuple(strings_of_dates)
        mycursor.execute('SELECT available_appointment_time FROM available_appointment INNER JOIN doctor USING (doctor_id)')
        times_list=mycursor.fetchall()
        times=[]
        for dr in times_list:
            times.append(dr[0])
        times=tuple(times)
        print(date, type(date))
        header= ("Doctor Name", "Appointment Date","Appointment Time")
        return render_template("availableappointments.html",doctors=doctors,availableappointments=data, head= header, dates=new_dates,times=times)
    elif session['role']=='doctor':
        return render_template("indexdoctor.html")
    elif session['role']=='admin':
        return render_template("indexadmin.html")
    return redirect('/')
    
    
    
    

        


@app.route('/patient/availableappointments', methods= ["GET","POST"])    
def patient_booking():
    if session['role']== 'patient':
        if request.method == 'POST':
            booked_date= request.form['date']
            booked_time= request.form['time']
            dr= request.form['doctor']
            mycursor.execute('SELECT doctor_id FROM doctor WHERE doctor_name = %s', (dr,))
            doctorid = mycursor.fetchone()[0]
            mycursor.execute('INSERT INTO booked_appointment (doctor_id, patient_id, booked_appointment_date, booked_appointment_time, past_or_upcoming) VALUES(%s, %s, %s, %s, "upcoming")',(doctorid,session['id'][0],booked_date,booked_time,))
            mydb.commit()
            mycursor.execute('DELETE FROM available_appointment WHERE doctor_id= %s AND available_appointment_date =%s AND available_appointment_time=%s',(doctorid,booked_date,booked_time,))
            mydb.commit()
            mycursor.execute('SELECT booked_appointment_id FROM booked_appointment WHERE doctor_id=%s AND patient_id=%s AND booked_appointment_date=%s AND booked_appointment_time=%s AND past_or_upcoming = "upcoming"',(doctorid,session['id'][0],booked_date,booked_time))
            app_id= mycursor.fetchone()[0]
            return render_template("bookingsuccess.html",dname=dr, appdate= booked_date, apptime=booked_time, appid=app_id)
    elif session['role']=='doctor': 
        return render_template('indexdoctor.html')
    elif session['role']=='admin':
        return render_template("indexadmin.html")
    return redirect('/')
if __name__ == '_main_':
    app.run(debug=True)