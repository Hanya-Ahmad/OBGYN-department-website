from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/", methods=['POST', 'GET'])
def indexpatient():
     return render_template('indexpatient.html')
@app.route("/doctor", methods=['POST', 'GET'])
def indexdoctor():
     return render_template('indexdoctor.html')
@app.route("/admin", methods=['POST', 'GET'])
def indexadmin():
     return render_template('indexadmin.html')
@app.route("/appointments", methods=['POST', 'GET'])
def appointments():
     return render_template('appointments.html')
     
@app.route("/login.html", methods=['POST','GET'])
def login():
     return render_template('login.html')

@app.route("/signup.html",methods=['POST','GET'])
def signup():
     return render_template('signup.html')

@app.route("/list", methods=['POST', 'GET'])
def list():
     return render_template('doctorslist.html')

@app.route("/adminlist", methods=['POST', 'GET'])
def listadmin():
     return render_template('adminlist.html')
@app.route("/inventory", methods=['POST','GET'])
def inventory():
     return render_template('inventory.html')

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
