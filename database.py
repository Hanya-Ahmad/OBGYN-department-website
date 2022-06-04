from ctypes.wintypes import INT
from enum import Enum
import string
from MySQLdb import STRING
import mysql.connector
from sqlalchemy import DATE, VARCHAR, String 




mydb= mysql.connector.connect(
   
   host= "localhost",
   user= "root",
   database= "obgyn"

)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE obgyn")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

# mycursor.execute (" CREATE TABLE admin ( admin_id INT AUTO_INCREMENT PRIMARY KEY , admin_email_address VARCHAR(200), admin_password VARCHAR(100), admin_name VARCHAR(200), hospital_name VARCHAR(200),hospital_address VARCHAR(200), hospital_contact_no varchar(30))")

#mycursor.execute ("CREATE TABLE appointment_table ( appointment_id INT AUTO_INCREMENT PRIMARY KEY, doctor_id INT , patient_id INT , doctor_schedule_id INT , appointment_number INT , appointment_time TIME , status VARCHAR(30) , doctor_comment VARCHAR(1000))")

#mycursor.execute ("CREATE TABLE doctor_schedule_table (schedule_id INT AUTO_INCREMENT PRIMARY KEY, doctor_id INT, schedule_date DATE, schedule_day ENUM('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'), schedule_start_time VARCHAR(20), schedule_end_time VARCHAR(20), schedule_status ENUM('Active','Inactive')) ")


#mycursor.execute (" CREATE TABLE doctor (doctor_id INT AUTO_INCREMENT PRIMARY KEY, doctor_email_address VARCHAR(200), doctor_password VARCHAR(100) , doctor_name VARCHAR(100) , doctor_phone_no VARCHAR(30) , doctor_address VARCHAR (500), doctor_date_of_birth DATE ,doctor_degree VARCHAR(200), doctor_status Enum('Active','Inactive'))")

#mycursor.execute ("CREATE TABLE patient ( patient_id INT AUTO_INCREMENT PRIMARY KEY, patient_email_address VARCHAR(200), patient_password VARCHAR(100), patient_first_name VARCHAR(100),patient_last_name VARCHAR(100), patient_date_of_birth DATE, patient_address VARCHAR(200), patient_phone_no VARCHAR(30))")


#mycursor.execute ("CREATE TABLE inventory ( device_id INT AUTO_INCREMENT PRIMARY KEY, device_name varchar(100),doctor_id INT, device_count INT, device_status ENUM('available','not available') )")


# sql = "INSERT INTO admin (admin_id, admin_email_address, admin_password, admin_name, hospital_name, hospital_address, hospital_contact_no) VALUES (%s, %s, %s, %s, %s, %s, %s)"

# val = ('1', 'gufranmohammed@gmail.com', 'password', 'Gufran Mohammed', 'Mount Hospital', '115, Last Lane, NYC', '741287410' )

# mycursor.execute(sql, val)


# sql1 = "INSERT INTO appointment_table (appointment_id, doctor_id, patient_id, doctor_schedule_id, appointment_number, appointment_time, status, doctor_comment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

# val1 = [('3', '1', '3', '2', '1000', '09:00:00', 'Cancel', ''),
#         ('4', '1', '3', '2', '1001', '09:00:00', 'Booked', ''),
#         ('5', '1', '4', '2', '1002', '09:30:00', 'Completed', 'She gave birth to boy baby.'),
#         ('6', '5', '3', '7', '1003', '18:00:00', 'In Process', ''),
#         ('7', '6', '5', '13','1004', '15:30:00', 'Completed','Acidity Problem.')]

# mycursor.executemany(sql1, val1)

# sql2 = "INSERT INTO doctor_schedule_table (schedule_id, doctor_id, schedule_date, schedule_day, schedule_start_time, schedule_end_time, schedule_status) VALUES (%s, %s, %s, %s, %s, %s, %s)"

# val2 = [('2', '1',  '2021-02-19', 'Friday',    '09:00', '14:00',  'Active'),
#         ('3', '2',  '2021-02-19', 'Friday',    '09:00', '12:00',  'Active'),
#         ('4', '5',  '2021-02-19', 'Friday',    '10:00', '14:00',  'Active'),
#         ('5', '3',  '2021-02-19', 'Friday',    '13:00', '17:00',  'Active'),
#         ('6', '4',  '2021-02-19', 'Friday',    '15:00', '18:00',  'Active'),
#         ('7', '5',  '2021-02-22', 'Monday',    '18:00', '20:00',  'Active'),
#         ('8', '2',  '2021-02-24', 'Wednesday', '09:30', '12:30',  'Active'),
#         ('9', '5',  '2021-02-24', 'Wednesday', '11:00', '15:00',  'Active'),
#         ('10', '1', '2021-02-24', 'Wednesday', '12:00', '15:00',  'Active'),
#         ('11', '3', '2021-02-24', 'Wednesday', '14:00', '17:00',  'Active'),
#         ('12', '4', '2021-02-24', 'Wednesday', '16:00', '20:00',  'Active'),
#         ('13', '6', '2021-02-24', 'Wednesday', '15:30', '18:30',  'Active'),
#         ('14', '6', '2021-02-25', 'Thursday',  '10:00', '13:30',  'Active')]

# mycursor.executemany(sql2, val2)        


# sql3 = "INSERT INTO doctor (doctor_id, doctor_email_address, doctor_password, doctor_name, doctor_phone_no, doctor_address, doctor_date_of_birth, doctor_degree, doctor_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

# val3 = [('1', 'peterparker@gmail.com', 'password', 'Dr. Peter Parker', '7539518520', '102, Sky View NYC', '1985-10-29', 'MBBS MS','Active'),
#         ('2', 'adambrodly@gmail.com', 'password', 'Dr. Adam Broudly','753852963', '105, Fort, NYC', '1982-08-10', 'MBBS MD(Cardiac)','Active'),
#         ('3', 'sophia.parker@gmail.com', 'password', 'Dr. Sophia Parker', '7417417410', '50, Best street CA', '1989-04-03', 'MBBS','Active'),
#         ('4', 'williampeterson@gmail.com', 'password', 'Dr. William Peterson', '8523698520', '32, Green City, NYC', '1984-06-11', 'MBBS MD', 'Active'),
#         ('5', 'emmalarsdattor@gmail.com', 'password', 'Dr. Emma Larsdattor', '9635852025', '25, Silver Arch', '1988-03-03', 'MBBS MD', 'Active'),
#         ('6', 'manuel.armstrong@gmail.com', 'password', 'Dr. Manuel Armstrong', '8523697410', '2378 Fire Access Road Asheboro, NC 27203', '1989-03-01', 'MBBS MD (Medicine)','Active',)]

# mycursor.executemany(sql3, val3)


# sql4 = "INSERT INTO patient (patient_id, patient_email_address, patient_password, patient_first_name, patient_last_name, patient_date_of_birth, patient_address, patient_phone_no) VALUES (%s, %s, %s, %s, %s,%s, %s, %s)"

# val4 = [('3', 'jacobmartin@gmail.com', 'password', 'Jacob', 'Martin', '2021-02-26', 'Green view, 1025,    NYC','85745635210'),
#         ('4', 'oliviabaker@gmail.com', 'password', 'Olivia', 'Baker', '2001-04-05', 'Diamond street, 115, NYC', '7539518520'),
#         ('5', 'amberanderson@gmail.com', 'password', 'Amber', 'Anderson', '1995-07-25','2083 Cameron Road Buffalo, NY 14202', '75394511442')]

# mycursor.executemany(sql4, val4)


# sql5 = "INSERT INTO inventory (device_id, device_name, doctor_id, device_count, device_status) VALUES (%s, %s, %s, %s, %s)"

# val5 = [('1', 'colposcopes',               '1', '5',        'available'),
#         ('2', 'ultrasound system',         '2', '2',        'not available'),
#         ('3', 'Liquid Based Cytology set', '3', '4',        'available')]

# mycursor.executemany(sql5, val5)

mydb.commit()

print(mycursor.rowcount, "record inserted.")