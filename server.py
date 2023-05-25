from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy

import csv
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="asemah",
    password="Newburg822!",
    hostname="asemah.mysql.pythonanywhere-services.com",
    databasename="asemah$miscdb",
)
app=Flask(__name__)
print(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class State(db.Model):

    __tablename__ = "States"

    order_id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(255))
    abr = db.Column(db.String(255))
    year_est = db.Column(db.Integer)
    size = db.Column(db.Integer)
    pop = db.Column(db.Integer)


@app.route('/states.html')
def index():
	#return 'Hello, World'
	#url=url_for('my_home')
	#return redirect(url)
	states=State.query.all()
	#return "lenght of states is " + str(len(states))
	return  render_template('states.html',states=states)



@app.route('/')
def my_home():
	#return 'Hello, World'
	return render_template('index.html')
@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
	if request.method=='POST':
		data=request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong.  Try again!'



@app.route('/<string:page_name>')
def dynamicurl(page_name):
	#return 'Hello, World'
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email=data['email']
		subject=data['subject']
		message=data['message']
		file=database.write(f'\n{email},{subject},{message}')
def write_to_csv(data):
	with open('database.csv',mode='a') as database2:
		email=data['email']
		subject=data['subject']
		message=data['message']
		csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

'''
@app.route('/submit_form', methods=['POST','GET'])
def submit_form(page_name):
	error=None
	if request.method=='POST':
		if valid_login(request.form['username'],request.form['password']):
			return log_the_user_in(request.form['username'],request.form['password'])
		else:
			error='Invalid username/password'
	return render_template('login.html',error=error)


@app.route('/index.html')
def index():
	#return 'Hello, World'
	url=url_for('my_home')
	return redirect(url)
	#return render_template('index.html')

@app.route('/about.html')
def my_about():
	#return 'Hello, World'
	print('goinf to about html')
	return render_template('about.html')

@app.route('/works.html')
def my_works():
	#return 'Hello, World'
	return render_template('works.html')

@app.route('/contact.html')
def my_contact():
	#return 'Hello, World'
	return render_template('contact.html')
'''