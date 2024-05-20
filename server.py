from flask import Flask,render_template,url_for,redirect,request,send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler
#from flask_sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
##############from flask_mysqldb import MySQL
import pymysql
import sshtunnel 
#from flaskext.mysql import MySQL

import csv
# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#     username="asemah",
#     password="Newburg822!",
#     hostname="asemah.mysql.pythonanywhere-services.com",
#     databasename="asemah$miscdb",
# )
'''
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="asemah",
    password="Newburg822!",
    hostname="asemah.mysql.pythonanywhere-services.com",
    databasename="asemah$miscdb",
)
'''
#app=Flask(__name__,static_url_path='', static_folder='frontend\public')
app=Flask(__name__)
print(__name__+"xyz")
CORS(app) #comment this on deployment
api = Api(app)
#app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
#app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
sshtunnel.SSH_TIMEOUT = 15.0 
sshtunnel.TUNNEL_TIMEOUT = 15.0
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['MYSQL_HOST'] = 'asemah.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'asemah'
app.config['MYSQL_PASSWORD'] = 'Newburg822!'
app.config['MYSQL_DB'] ='asemah$miscdb'
app.config['MYSQL_PORT'] =3306

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Best4all'
# app.config['MYSQL_DB'] ='world'

#app.config['MYSQL_PORT']=3306
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Best4all@localhost/world'
#db = SQLAlchemy(app)


'''
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
'''
#db = SQLAlchemy(app)
'''
class State(db.Model):

    __tablename__ = "States"

    order_id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(255))
    abr = db.Column(db.String(255))
    year_est = db.Column(db.Integer)
    size = db.Column(db.Integer)
    pop = db.Column(db.Integer)
'''
'''
@app.route('/states.html')
def index():
	#return 'Hello, World'
	#url=url_for('my_home')
	#return redirect(url)
	states=State.query.all()
	#return "lenght of states is " + str(len(states))
	return  render_template('states.html',states=states)
'''
# mysql = pymysql.connect(
#     user=app.config["MYSQL_USER"],
#     password=app.config["MYSQL_PASSWORD"],
#     host=app.config["MYSQL_HOST"],
#     database=app.config["MYSQL_DB"]
# )
with sshtunnel.SSHTunnelForwarder( ('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"], ssh_password=app.config["MYSQL_PASSWORD"], remote_bind_address=(app.config["MYSQL_HOST"], 3306) ) as tunnel:
	 connection = pymysql.connect( user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"], host='127.0.0.1', port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])

#mysql = MySQL(app)
# print(f'my sql is: {mysql}')
# print(f'my sql is conenction: {mysql.connection}')
class City():

    __tablename__ = "city"
    a=5
    #order_id = db.Column(db.Integer, primary_key=True)
    # state = db.Column(db.String(255))
    # abr = db.Column(db.String(255))
    # year_est = db.Column(db.Integer)
    # size = db.Column(db.Integer)
    # pop = db.Column(db.Integer)

	#ID =db.Column(db.Integer, primary_key=True)
	#Name=db.Column(db.String(35))
	#CountryCode = db.Column(db.Char(3))
	#District = db.Column(db.Char(20))
	#Population = db.Column(db.Integer)
@app.route('/returnDBStaff/<string:city>')
def returnDBStaff(city):
    try:
    # if not mysql.open:
    #     mysql.ping(reconnect=True)
    #cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder( ('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"], ssh_password=app.config["MYSQL_PASSWORD"], remote_bind_address=(app.config["MYSQL_HOST"], 3306) ) as tunnel:
            connection = pymysql.connect( user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"], host='127.0.0.1', port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            # sqltext="select * from City where name='"+ city+ "'"
            sqltext="select * from States"
            cursor.execute(sqltext)
            #cursor.execute('''select * from City''')
            data = cursor.fetchall()
            return ({"city":city,"data": data,"count":len(data)})
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return ({"error": str(e)})

@app.route('/returnDBStaff2')
def returnDBStaff2():
	# MySQL(app)
	# print(f'my sql is: {mysql}')
	# print(f'my sql is conenction: {mysql.connection}')
	db=_mysql.connect("localhost","joebob","moonpie","thangs");

	cursor = mysql.connection.cursor()


	sql = "SELECT * FROM city"
	cursor.execute(sql)
	results = cursor.fetchall()
	cursor.close()

	return  {'states':results}


@app.route('/returnStates')
def returnAllStates():
	#return 'Hello, World'
	#url=url_for('my_home')
	#return redirect(url)
	alist=['apples','banans']
	#return "lenght of states is " + str(len(states))
	dict={'name':'avi semah','country':'usa','favorites':alist}
	return  dict

@app.route('/react.html')
def index():
	#return 'Hello, World'
	url="http://localhost:3000/"#url_for('my_home')
	return redirect(url)
	#states=State.query.all()
	#return "lenght of states is " + str(len(states))
	#return  render_template('states.html',states=states)

print("app.static_folder" +app.static_folder)
'''
@app.route("/xyz", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')
'''
api.add_resource(HelloApiHandler, '/flask/hello')

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
	print("page_name:" + page_name)
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