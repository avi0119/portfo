from flask import Flask,render_template,url_for,redirect,request
import csv
app=Flask(__name__)
print(__name__)

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