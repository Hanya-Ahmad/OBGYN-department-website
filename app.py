import mysql.connector 
from flask import Flask, render_template, url_for, request, session, redirect
from flask_session import Session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret key'


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="database_project"
)

mycursor = mydb.cursor(buffered = True)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/patient')
def patient():
    return render_template("indexpatient.html")

@app.route('/doctor')
def doctor():
    return render_template("indexdoctor.html")

@app.route('/admin')
def admin():
    return render_template("indexadmin.html")


@app.route('/patient/availableappointments/patientbooking')
def booking():
     return render_template("patientbooking.html")
    
    
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


@app.route('/contactus',methods=['POST','GET'])
def contact(): 
    return render_template('contactindex.html')


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
        emailExists=False
        usernameExists=False
        #database updates
        mycursor.execute('DELETE FROM inventory WHERE  CURRENT_DATE() >= expiry_date')
        mydb.commit()
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
        
        elif phone_number.isnumeric()==False or len(phone_number)!=11: #or str(phone_number)[:2] != "01":
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
            return render_template('signup.html', error_stat=error_statement, user_name=username, pass_word=password)
        else:   
            mycursor.execute(
                'SELECT * FROM user WHERE username =%s AND access=%s', (username,role))
            account = mycursor.fetchone()
            if account:
                usernameExists=True
            mycursor.execute(
                'SELECT patient_email_address FROM patient WHERE patient_email_address=%s',(e_mail,))
            account = mycursor.fetchone()
            if account:
                emailExists=True
            if usernameExists or emailExists:
                error_statement = "An account with this username already exists."
                return render_template("signup.html", error_stat=error_statement)

            else:
                if role == "patient":
                    mycursor.execute(
                        'INSERT INTO user (pass,username,access) VALUES( %s, %s,%s)', 
                        (password, username, role))
                    mydb.commit()

                    result = mycursor.execute('SELECT userid from user WHERE username=%s AND pass =%s',(username,password,))
                    result = mycursor.fetchone()
                    patient_id=result[0]
                    session['id']=patient_id
                    mycursor.execute('INSERT INTO patient (patient_id,patient_first_name,patient_last_name,patient_email_address,patient_age,patient_phone_no) VALUES( %s, %s,%s, %s, %s, %s)', (patient_id, first_name, last_name, e_mail, age, phone_number,))
                    mydb.commit()
                    
                    return render_template('indexpatient.html', user_name=username, pass_word=password)

        return render_template('signup.html')


@app.route('/login', methods=["GET", "POST"])
def signin():
    if request.method == 'POST' :
        username = request.form['username'].lower()
        password = request.form['pass']
        role= request.form['access']
        #database updates:
        mycursor.execute('DELETE FROM inventory WHERE  CURRENT_DATE() >= expiry_date')
        mydb.commit()
        if len(password) == 0 or len(username)==0 or len(role)==0:
            error_statement = 'Invalid input. Please re-enter your username, password and role correctly.'
            return render_template("signin.html",error_stat = error_statement, )
            
        else:
            
                mycursor.execute('SELECT * FROM user WHERE username = %s AND pass = %s AND access = %s', (username,password,role))
                account = mycursor.fetchall()
                
                if account :
                        mycursor.execute('SELECT userid from user WHERE username=%s AND pass =%s',(username,password,))
                        result = mycursor.fetchone()
            
                        session["id"]=result
                        mycursor.execute('SELECT access from user WHERE username=%s AND pass =%s',(username,password,))
                        result =mycursor.fetchone()
                        session["role"]=result[0]
                        if role == ("patient"):
                            return render_template("indexpatient.html")
                            
                        elif role ==("doctor"):        
                            return render_template("indexdoctor.html")
                            

                        else :
                            return render_template('indexadmin.html')     
                            
                   
                else:
                    error_statement = " There's no such account. Please make sure you enter your correct username, password and role. Or sign up if you don't have an existing account."
                    return render_template('login.html', username=username, error=error_statement)



@app.route("/logout",methods=['POST','GET'])
def logout():
    session["id"] = None
    session["role"]= None
    return redirect("/")

@app.route('/doctor/myappointments',methods=['GET','POST'])
def my_appointments():
    if session["role"]== "patient":
        return render_template('indexpatient')
    elif session['role']=='admin':
        return render_template('indexadmin.html')
    elif session["role"]== "doctor":    
        doctor_id=session['id']
        mycursor.execute('SELECT patient_id, booked_appointment_time, booked_appointment_date, doctor_comment FROM booked_appointment WHERE doctor_id = %s AND past_or_upcoming = "past"',(doctor_id[0],))
        past=tuple(mycursor.fetchall())
        mycursor.execute('SELECT patient_id, booked_appointment_time, booked_appointment_date, doctor_comment FROM booked_appointment WHERE doctor_id = %s AND past_or_upcoming = "upcoming"',(doctor_id[0],))
        upcoming=tuple(mycursor.fetchall())
        return render_template("myappointments.html", past_appointments=past, upcoming_appointments=upcoming)
    return redirect('/')

@app.route('/admin/doctorsappointment', methods=['GET','POST'])
def admin_doctors_appointments():
      if session['role'] == None:
         return redirect('/')
      elif session['role']== 'patient':
          return render_template('indexpatient.html')
      elif session['role']=='doctor':
          return render_template('indexdoctor.html')
      elif session['role'] == "admin": 
        mycursor.execute('SELECT patient_id, doctor_id, booked_appointment_date, booked_appointment_time, doctor_comment FROM booked_appointment WHERE past_or_upcoming = "past"')
        past=tuple(mycursor.fetchall())
        mycursor.execute('SELECT patient_id, doctor_id, booked_appointment_date, booked_appointment_time, doctor_comment FROM booked_appointment WHERE past_or_upcoming = "upcoming"')
        upcoming=tuple(mycursor.fetchall())
        header= ("Patient ID","Doctor ID", "Appointment Date", "Appointment Time", "Doctor's Comment")
        return render_template("allappointments.html",past_appointments=past, upcoming_appointments=upcoming, head= header)
      return redirect('/')

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
        mycursor.execute('SELECT available_appointment_time FROM available_appointment INNER JOIN doctor USING (doctor_id)')
        times_list=tuple(mycursor.fetchall())
        new_dates=tuple(strings_of_dates)
        times=[]
        for t in times_list:
            times.append(t[0])
        times=tuple(times)
        header= ("Doctor Name", "Appointment Date","Appointment Time")
        return render_template("availableappointments.html",doctors=doctors,availableappointments=data, head= header, dates=new_dates,times=times)
    elif session['role']=='doctor':
        return render_template("indexdoctor.html")
    elif session['role']=='admin':
        return render_template("indexadmin.html")
    return redirect('/')
    
@app.route('/patient/myappointments', methods=['GET','PUSH'])
def show_my_appointments():
    if session['role']== "patient":
        mycursor.execute('SELECT booked_appointment_id, doctor_name, booked_appointment_date, booked_appointment_time, doctor_comment FROM doctor INNER JOIN booked_appointment USING (doctor_id) WHERE patient_id= %s',((session['id'])[0],))
        my_apps= tuple(mycursor.fetchall())    
        header=("Appointment ID", "Doctor", "Appointment Date", "Appointment Time", "Doctor's Comment(s)")
        return render_template('patientappointments.html', appointments=my_apps, head=header)
        
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
    
    

    
@app.route("/doctor/inventory")
def dr_inventory_table():
    if session["role"]== "patient":
        return render_template('indexpatient')
    elif session['role']=='admin':
        return render_template('indexadmin.html')
    elif session["role"]== "doctor":
        mycursor.execute('SELECT device_sn FROM inventory WHERE device_state="available"')
        devices_sns= mycursor.fetchall()
        device_sn=[]
        for sn in devices_sns:
            device_sn.append(sn[0])
        device_sn=tuple(device_sn)
        mycursor.execute('SELECT device_name FROM inventory WHERE device_state="available"')
        devices_names=mycursor.fetchall()
        device_name=[]
        for name in devices_names:
            device_name.append(name[0])
        device_name=tuple(device_name)
        mycursor.execute('SELECT booking_date FROM inventory WHERE device_state="available"')
        booking_dates= mycursor.fetchall()
        booking_date=[]
        for bdate in booking_dates:
            booking_date.append(bdate[0])
        booking_date=tuple(booking_date)
        mycursor.execute('SELECT booking_hour FROM inventory WHERE device_state="available"')
        bhours= mycursor.fetchall()
        booking_hour=[]
        for bhour in bhours:
            booking_hour.append(bhour[0])
        booking_hour=tuple(booking_hour)
        mycursor.execute('SELECT device_sn, device_name, booking_date, booking_hour FROM inventory WHERE device_state="available"')
        all_data= tuple(mycursor.fetchall())
        header=("Device SN", "Device Type", "Available Date", "Booking Hour")
        return render_template("doctorinventory.html",rows_info=all_data, head=header, time=booking_hour, date=booking_date, dname=device_name, serial_number=device_sn)
    return redirect('/')


    
@app.route('/doctor/inventory',methods=['GET','POST'])
def dr_book_dev():
    if session["role"]== "patient":
        return render_template('indexpatient')
    elif session['role']=='admin':
        return render_template('indexadmin.html')
    elif session["role"]== "doctor":
        if request.method=='POST':
            sn= request.form['device_sn']
            dev_name=request.form['device_name']
            booking_date=request.form['date']
            booking_time=request.form['time']
            doctor_id=session['id']
            values=(doctor_id[0],sn,dev_name,booking_date,booking_time,)
            mycursor.execute('SELECT* FROM inventory WHERE device_sn=%s AND device_name=%s AND booking_date=%s AND booking_hour=%s AND device_state="available"',(sn,dev_name,booking_date,booking_time,))
            success=mycursor.fetchall()
            if success:
                mycursor.execute('UPDATE inventory SET doctor_id=%s WHERE device_sn=%s AND device_name=%s AND booking_date=%s AND booking_hour=%s',values)
                mydb.commit()
                mycursor.execute('UPDATE inventory SET device_state="not available" WHERE device_sn=%s AND device_name=%s AND booking_date=%s AND booking_hour=%s',(sn,dev_name,booking_date,booking_time,))
                mydb.commit()
                message='Booking completed successfully.You booked {} (SN: {}). You will be able to use the {} at {}, {}'.format(
                    dev_name,sn,dev_name,booking_date,booking_time)
            else:
                message='Please recheck the information table and choose existing values.'
            return render_template("inventorybooking.html",message=message)
    return redirect(url_for('dr_inventory_table'))
            
@app.route('/admin/inventory',methods=['GET','PUSH'])
def admin_inventory_table():
    if session["role"]== "patient":
        return render_template('indexpatient')
    elif session['role']=="doctor":
        return render_template('indexadmin.html')
    if session["role"]== 'admin':
        mycursor.execute('SELECT device_sn, device_name, date_imported, booking_date, booking_hour FROM inventory WHERE device_state="available"')
        avlbl= tuple(mycursor.fetchall())
        avheader=("Device SN", "Device Type", "Date Imported ", "Booking Date", "Booking Hour")
        mycursor.execute('SELECT device_sn, device_name, date_imported, booking_date, booking_hour, doctor_id FROM inventory WHERE device_state="not available"')
        booked=tuple(mycursor.fetchall()) 
        bookheader=("Device SN", "Device Type", "Date Imported ", "Booked Date", "Booked Hour", "Doctor ID")
        return  render_template("admininventory.html",available_rows=avlbl, available_head=avheader, booked_rows=booked, booked_head=bookheader)
    return redirect('/')
    
    
if __name__ == '__main__':
    app.run(debug=True)