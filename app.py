from flask import Flask, request, render_template
app = Flask(__name__)
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
