import uuid
import pandas as pd
#import pyjokes
from datetime import datetime
from flask import Flask,render_template,url_for,redirect,request,send_from_directory,jsonify, send_file,send_from_directory
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
import sys
import smtplib
from email.mime.text import MIMEText
from urllib.parse import urlparse

HOST12701='127.0.0.1'
DOMAIN_HTTP_ADDRESS='http://127.0.0.1:5000'
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
	 connection = pymysql.connect( user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"], host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])

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
            connection = pymysql.connect( user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"], host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
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

@app.route('/getdomain')
def getdomain():
	#return 'Hello, World'
	o = urlparse(request.base_url)
	return o.hostname
def obtaindomain():
	#return 'Hello, World'
	o = urlparse(request.base_url)
	return DOMAIN_HTTP_ADDRESS#"http://"+  o.hostname

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
@app.route('/submit_login_form', methods=['POST','GET'])
def submit_login_form():
	print ('inside submit_login_form')
	#uname= request.form['uname']
	#psw=request.form['psw']

	return 'success'
@app.route('/submit_login_form2', methods=['POST','GET'])
def submit_login_form2():
    print ('inside submit_login_form')
    #uname= request.form['uname']
    #psw=request.form['psw']
    today_date = datetime.date.today()
    #new_today_date = today_date.strftime("%Y-%m-%d")
    content = request.get_json(silent=True)
    print(content['uname'])
    uname=content['uname']
    email=content['email']
    psw=content['psw']
    first_name='some first nane'
    last_name='some last name'
    password=psw
    last_updated=today_date
    created=last_updated
    
    res=recordNewUserName(uname,first_name, last_name, password,  last_updated, created,email)
    return {"content":res}

@app.route('/recordsingledaytimehours', methods=['POST','GET'])
def RecodSingleDayTimeHours():
    print ('inside RecodSingleDayTimeHours')
    if IsThereSecurityCookie()==False:
    	return {'success':False,'msg':'RelogginNeeded'}    
    #uname= request.form['uname']  
    #psw=request.form['psw']
    today_date = datetime.now()
    new_today_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
    content = request.get_json(silent=True)
    #print(content['uname'])
    uname=content['uname']
    starttime=content['starttime']
    endtime=content['endtime']
    workingday=content['workingday']
    # return {
    # 	'starttime':starttime,
    # 	'endtime':endtime,
    # 	'workingday':workingday,
    # 	'uname':uname
    # } 
    
    last_updated=new_today_date
    created=last_updated
    numberOfusersOfSameUname=int(returnCountOfRecordsOfGivenUserName(uname))
    # typeogf=str(type(numberOfusersOfSameUname))
    # return {'ret':typeogf}
    if numberOfusersOfSameUname==0:
    	return {'success':False,'msg':f'username {uname} does not exist'}
    numberOfusersOfSameUname=int(returnCountOfRecordsOfGivenUserNameAndTimeEntryDate(uname,workingday))
    if numberOfusersOfSameUname==1:
    	return {'success':False,'msg':f'username {uname} already recorded time for {workingday}.\nPleaase go to history and update the time for that date'}		
    res=recordTimeInAndOut(uname,workingday,starttime,endtime,  last_updated, created)
    success=res[0]
    return {'success':success,'msg':res[1]}	#{"content":res}

def returnCountOfRecordsOfGivenUserNameAndTimeEntryDate(uname,workingday):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            #sqltext="select * from City where name='"+ city+ "'"
            #sqltext="select * from users" #where uname='{uname}'""
            sqltext = f"SELECT count(*) as count FROM  timeentry where  start_date  ='{workingday}' and uname='{uname}'"
            cursor.execute(sqltext)
            # cursor.execute('''select * from City''')
            rows = cursor.fetchall()
            # data_array=data['content']
            # firstrecord=data_array[0]
            # count=firstrecord[0]
            main_list = []
            
            for row in rows:
                current_list = []
                for i in row:
                    current_list.append(i)
                main_list.append(current_list)
            count=main_list[0][0]
            return count# int([data[0]]['count'])
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return ({"error": str(e)})



def recordTimeInAndOut(uname, workingday, starttime, endtime, last_updated, created):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        startdate_converted_to_date = datetime.strptime(workingday, '%Y-%m-%d')
        startdate_no_time = startdate_converted_to_date.strftime("%Y-%m-%d %H:%M:%S")
        sqltext = f"INSERT INTO timeentry ( uname,start_date,start_time,end_time,  last_updated, created) VALUES ('{uname}', '{startdate_no_time}', '{starttime}', '{endtime}', '{last_updated}','{created}');"
        # return (False,sqltext)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
            ssh_password=app.config["MYSQL_PASSWORD"],
            remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext = "select * from States"
            cursor.execute(sqltext)
            # cursor.execute('''select * from States''')
            connection.commit()
            # data = cursor.fetchall()
            return (True, '11')
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (False, {"error": f'{e}'})	
@app.route('/crate_new_user', methods=['POST','GET'])
def crate_new_user():
    print ('inside submit_login_form')
    if IsThereSecurityCookie()==False:
    	return {'success':False,'msg':'RelogginNeeded'}
    #uname= request.form['uname']  
    #psw=request.form['psw']
    today_date = datetime.now()
    new_today_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
    content = request.get_json(silent=True)
    #print(content['uname'])
    uname=content['uname']
    email=content['email']
    psw=content['psw']
    first_name=content['firstname']
    last_name=content['lastname']
    password=psw
    last_updated=new_today_date
    created=last_updated
    numberOfusersOfSameUname=int(returnCountOfRecordsOfGivenUserName(uname))
    # typeogf=str(type(numberOfusersOfSameUname))
    # return {'ret':typeogf}
    if numberOfusersOfSameUname>0:
    	return {'success':False,'msg':'this user name is already taken'}	
    res=recordNewUserName(uname,first_name, last_name, password,  last_updated, created,email)
    success=res[0]
    return {'success':success,'msg':res[1]}	#{"content":res}
@app.route('/updateuser', methods=['POST','GET'])
def updateUserDeatils():
    print ('inside updateUserDeatils')
    if IsThereSecurityCookie()==False:
    	return {'success':False,'msg':'RelogginNeeded'}
    #uname= request.form['uname']  
    #psw=request.form['psw']
    today_date = datetime.now()
    new_today_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
    content = request.get_json(silent=True)
    #print(content['uname'])
    uname=content['uname']
    email=content['email']
    psw=content['psw']
    first_name=content['firstname']
    last_name=content['lastname']
    password=psw
    last_updated=new_today_date
    # created=last_updated
    numberOfusersOfSameUname=int(returnCountOfRecordsOfGivenUserName(uname))
    # typeogf=str(type(numberOfusersOfSameUname))
    # return {'ret':typeogf}
    if numberOfusersOfSameUname==0:
    	return {'success':False,'msg':'this user does not exist in database'}
    res=updateUserName(uname,first_name, last_name,   last_updated,email)
    success=res[0]
    return {'success':success,'msg':res[1]}	#{"content":res}
def returnAllUserDetailsEmail(email):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext="select * from users" #where uname='{uname}'""
            sqltext = f"select * from users where email='{email}'"
            cursor.execute(sqltext)
            # cursor.execute('''select * from City''')
            rows = cursor.fetchall()
            # data_array=data['content']
            # firstrecord=data_array[0]
            # count=firstrecord[0]
            if True == False:
                main_list = []
                
                for row in rows:
                    current_list = []
                    for i in row:
                        current_list.append(i)
                    main_list.append(current_list)
                return main_list  # int([data[0]]['count'])
            else:
            	print('hiiiiiiiiiiiiiii',file=sys.stdout)
            	#ret={'type':str(type(rows))}
            	print(rows,file=sys.stdout)
            	return (True,evalluatListOfDictionaries(rows))


    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (False,({"error": str(e)}))

def returnAllUserDetailsForUserName(uname):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext="select * from users" #where uname='{uname}'""
            sqltext = f"select * from users where uname='{uname}'"
            cursor.execute(sqltext)
            # cursor.execute('''select * from City''')
            rows = cursor.fetchall()
            # data_array=data['content']
            # firstrecord=data_array[0]
            # count=firstrecord[0]
            if True == False:
                main_list = []
                
                for row in rows:
                    current_list = []
                    for i in row:
                        current_list.append(i)
                    main_list.append(current_list)
                return main_list  # int([data[0]]['count'])
            else:
            	print('hiiiiiiiiiiiiiii',file=sys.stdout)
            	#ret={'type':str(type(rows))}
            	print(rows,file=sys.stdout)
            	return (True,evalluatListOfDictionaries(rows))


    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (False,({"error": str(e)}))
def recordNewUserName(uname, first_name, last_name, password, last_updated, created, email):
    defaultrole = 1
    
    
    sqltext = f"INSERT INTO users ( role,email,uname,first_name, last_name, password, active, last_updated, created) VALUES ({defaultrole},'{email}','{uname}', '{first_name}', '{last_name}', '{password}', 1, '{last_updated}','{created}');"
    # return sqltext
    
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext = "select * from States"
            cursor.execute(sqltext)
            # cursor.execute('''select * from States''')
            connection.commit()
            # data = cursor.fetchall()
            return (True, '11')
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (False, {"error": f'{e}'})	
@app.route('/getuserdetails', methods=['GET', 'POST'])
def getUserDetails():
    print ('inside getUserDetails')
    #uname= request.form['uname'] 
    #psw=request.form['psw']
    # today_date = datetime.now()
    # new_today_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
    content = request.get_json(silent=True)
    print(content['uname'])
    uname=content['uname']
    # email=content['email']
    # psw=content['psw']
    # first_name=content['firstname']
    # last_name=content['lastname']
    # password=psw
    # last_updated=new_today_date
    # created=last_updated
    listOfresults=returnAllUserDetailsForUserName(uname)
    # typeogf=str(type(numberOfusersOfSameUname))
    # return {'ret':typeogf}
    # if len(listOfresults)==0:
    # 	return {'success':False,'msg':'this user name is already taken'}	
    # res=recordNewUserName(uname,first_name, last_name, password,  last_updated, created,email)
    # success=res[0]
    # data_as_dict={ 'line '+str(ind) :' '.join([str(i) for i in x]) for ind, x in enumerate(listOfresults) }
    

    data_as_dict=listOfresults[1]
    #data_as_dict=[{'line1':'xyz'},{'line1':'abc'}];
    if listOfresults[0]==True:
    	return {'success':listOfresults[0],'data':data_as_dict,'msg':'all is good'}	#{"content":res}
    else:
    	if str(data_as_dict)=="RelogginNeeded":
    		msg="RelogginNeeded"
    	else:
    		msg=data_as_dict
    	return {'success':listOfresults[0],'msg':msg}
def updateUserName( uname,first_name, last_name,   last_updated,email):
    defaultrole = 1
    defaultactive=1
    
    sqltext = f"UPDATE users SET first_name='{first_name}', last_name='{last_name}',active={defaultactive},last_updated='{last_updated}',email='{email}' where uname='{uname}';"
    # return (False,sqltext)
    
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext = "select * from States"
            cursor.execute(sqltext)
            # cursor.execute('''select * from States''')
            connection.commit()
            # data = cursor.fetchall()
            return (True, '11')
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (False, {"error": f'{e}'})	
@app.route('/login', methods=['GET', 'POST'])
def login():
    print('inside login')
    # uname= request.form['uname'] 
    # psw=request.form['psw']
    today_date = datetime.now()
    new_today_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
    content = request.get_json(silent=True)
    # print(content['uname'])
    uname = content['uname']
    # email=content['email']
    psw = content['psw']
    # first_name=content['firstname']
    # last_name=content['lastname']
    password = psw
    last_updated = new_today_date
    created = last_updated
    isAuthenticationSuccessful = isUserPasswordCombinationInDB(uname, psw)
    # typeogf=str(type(numberOfusersOfSameUname))
    # return {'ret':typeogf}
    if isAuthenticationSuccessful == False:
        return {'success': False, 'msg': 'username and/or password are incorrect'}
    # res=recordNewUserName(uname,first_name, last_name, password,  last_updated, created,email)
    user_details=returnAllUserDetailsForUserName(uname)
    dict=user_details[1][0]
    del dict['password']
    out = jsonify(success=True, msg='successful authentication!',user_details=dict)
    out.set_cookie('soapologyInSessionUserName', uname)
    return out
    # return {'success':True,'msg':'successful authentication!'}	#{"content":res}
def IsThereSecurityCookie():
	ret=False
	if 'soapologyInSessionUserName' in request.cookies:
		ret=True
	return ret
def isUserPasswordCombinationInDB(uname,psw):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            #sqltext="select * from City where name='"+ city+ "'"
            #sqltext="select * from users" #where uname='{uname}'""
            sqltext = f"select count(*) as count from users where uname='{uname}' and password='{psw}'"
            cursor.execute(sqltext)
            # cursor.execute('''select * from City''')
            rows = cursor.fetchall()
            # data_array=data['content']
            # firstrecord=data_array[0]
            # count=firstrecord[0]
            main_list = []
            
            for row in rows:
                current_list = []
                for i in row:
                    current_list.append(i)
                main_list.append(current_list)
            count=main_list[0][0]
            return count>0# int([data[0]]['count'])
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return ({"error": str(e)})
def returnCountOfRecordsOfGivenUserName(uname):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            #sqltext="select * from City where name='"+ city+ "'"
            #sqltext="select * from users" #where uname='{uname}'""
            sqltext = f"select count(*) as count from users where uname='{uname}'"
            cursor.execute(sqltext)
            # cursor.execute('''select * from City''')
            rows = cursor.fetchall()
            # data_array=data['content']
            # firstrecord=data_array[0]
            # count=firstrecord[0]
            main_list = []
            
            for row in rows:
                current_list = []
                for i in row:
                    current_list.append(i)
                main_list.append(current_list)
            count=main_list[0][0]
            return count# int([data[0]]['count'])
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return ({"error": str(e)})
@app.route('/gethistoricaltimeentry', methods=['GET', 'POST'])
def getHistoricalTimeEntry():
    print ('inside getHistoricalTimeEntry')
    #uname= request.form['uname'] 
    #psw=request.form['psw']
    # today_date = datetime.now()
    # new_today_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
    content = request.get_json(silent=True)
    #print(content['uname'])
    # uname=content['uname']
    uname=content.get('uname',None)
    fromdate=content.get('fromdate',None)
    todate=content.get('todate',None)
    # email=content['email']
    # psw=content['psw']
    # first_name=content['firstname']
    # last_name=content['lastname']
    # password=psw
    # last_updated=new_today_date
    # created=last_updated
    listOfresults=returnAllRecordTimeEntryHistoryForUserName(uname=uname,fromdate=fromdate,todate=todate)
    # typeogf=str(type(numberOfusersOfSameUname))
    # return {'ret':typeogf}
    # if len(listOfresults)==0:
    # 	return {'success':False,'msg':'this user name is already taken'}	
    # res=recordNewUserName(uname,first_name, last_name, password,  last_updated, created,email)
    # success=res[0]
    # data_as_dict={ 'line '+str(ind) :' '.join([str(i) for i in x]) for ind, x in enumerate(listOfresults) }
    

    data_as_dict=listOfresults[1]
    #data_as_dict=[{'line1':'xyz'},{'line1':'abc'}];
    if listOfresults[0]==True:
    	return {'success':listOfresults[0],'data':data_as_dict,'msg':'all is good'}	#{"content":res}
    else:
    	if str(data_as_dict)=="RelogginNeeded":
    		msg="RelogginNeeded"
    	else:
    		msg=data_as_dict
    	return {'success':listOfresults[0],'msg':msg}	#{"content":res}
def returnNoneIfEmpty(arg):
	if arg!=None and len(arg)==0:
		return None
	return arg
@app.route('/downloadtimeentryfile', methods=['GET', 'POST'])
def downloadtimeentryfile():
    print ('inside downloadtimeentryfile')
    if IsThereSecurityCookie()==False:
    	return {'success':False,'msg':'RelogginNeeded'}
    #uname= request.form['uname'] 
    #psw=request.form['psw']
    # today_date = datetime.now()
    # new_today_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
	# if True==False:
	# 	content = request.get_json(silent=True)
	# 	uname=content.get('uname',None)
	# 	fromdate=content.get('fromdate',None)
	# 	todate=content.get('todate',None)
	# else:
    # uname=None
    # fromdate=None
    # todate=None	
    uname = returnNoneIfEmpty(request.args.get('uname'))
    fromdate = returnNoneIfEmpty(request.args.get('fromdate'))
    todate = returnNoneIfEmpty(request.args.get('todate'))
    # temp=str(uname) + " "+ str(fromdate)+ " "+ str(todate)
    # return {'final':temp}
    # email=content['email']
    # psw=content['psw']
    # first_name=content['firstname']
    # last_name=content['lastname']
    # password=psw
    # last_updated=new_today_date
    # created=last_updated
    listOfresults=returnAllRecordTimeEntryHistoryForUserName(uname=uname,fromdate=fromdate,todate=todate)
    #print(content['uname'])
    filename="timeentrydownload.xlsx"
    uploads="D:\\PythonWS\\portfo"
    df = pd.DataFrame(listOfresults[1])
    print(df)
    df.to_excel('timeentrydownload.xlsx', index=False)
    return send_file( filename,as_attachment=True)
    # return send_from_directory(uploads, filename)
    # typeogf=str(type(numberOfusersOfSameUname))
    # return {'ret':typeogf}
    # if len(listOfresults)==0:
    # 	return {'success':False,'msg':'this user name is already taken'}	
    # res=recordNewUserName(uname,first_name, last_name, password,  last_updated, created,email)
    # success=res[0]
    # data_as_dict={ 'line '+str(ind) :' '.join([str(i) for i in x]) for ind, x in enumerate(listOfresults) }
    

    data_as_dict=listOfresults[1]
    #data_as_dict=[{'line1':'xyz'},{'line1':'abc'}];
    if listOfresults[0]==True:
    	return {'success':listOfresults[0],'data':data_as_dict,'msg':'all is good'}	#{"content":res}
    else:
    	if str(data_as_dict)=="RelogginNeeded":
    		msg="RelogginNeeded"
    	else:
    		msg=data_as_dict
    	return {'success':listOfresults[0],'msg':msg}	#{"content":res}
def returnAllRecordTimeEntryHistoryForUserName(uname=None,fromdate=None,todate=None):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        
        if IsThereSecurityCookie()==False:
        	return (False,"RelogginNeeded")
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host='127.0.0.1', port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext="select * from users" #where uname='{uname}'""
            #return  (False,"xyzxyz")
            sqltext = f"select * from timeentry"
            criteria=''
            if (uname!=None):
            	criteria=f" where uname='{uname}'"
            if fromdate!=None or todate!=None:
            	criteria=criteria=criteria + (' and ' if len(criteria)>0 else ' where ') +f"(start_date>='{fromdate}' and start_date<='{todate}')"
            sqltext=sqltext+ criteria+ ' order by start_date'
            # if allrecordflag==True:
            # 	sqltext = f"select * from timeentry"
            # else:
            # 	sqltext = f"select * from timeentry where uname='{uname}' order by start_date"
            # return  (False,sqltext)
            cursor.execute(sqltext)
            # cursor.execute('''select * from City''')
            rows = cursor.fetchall()
            # data_array=data['content']
            # firstrecord=data_array[0]
            # count=firstrecord[0]
            if True == False:
                main_list = []
                
                for row in rows:
                    current_list = []
                    for i in row:
                        current_list.append(i)
                    main_list.append(current_list)
                return main_list  # int([data[0]]['count'])
            else:
            	print('hiiiiiiiiiiiiiii',file=sys.stdout)
            	#ret={'type':str(type(rows))}
            	print(rows,file=sys.stdout)
            	return (True,evalluatListOfDictionaries(rows))


    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (False,({"error": str(e)}))
def evalluatListOfDictionaries(rows):
	ret=[]
	for row in rows:
		new_dict={}
		for akey,avalue in row.items():
			new_dict[akey]=(str(avalue))
		ret.append(new_dict)
	return ret



@app.route('/sidebarmenu', methods=['POST','GET'])
def sidebarmenu():
	error=None
	return render_template('IntroWithSidebarMenu.html',error=error)
@app.route('/displayInitialLogin', methods=['POST','GET'])
def displayLogin():
	error=None
	return render_template('InitialLoginPageOnly.html',error=error)
#sendemployeeidsetupinvitation
@app.route('/sendemployeeinitializationemail', methods=['POST','GET'])
def testSendinEmail():
	if IsThereSecurityCookie()==False:
		return {'success':False,'msg':'RelogginNeeded'}#(False,"RelogginNeeded")
	content = request.get_json(silent=True)
	# print(content['uname'])
	# uname = content['uname']
	email_recipient=content['email']
	# psw = content['psw']
	first_name=content['firstname']
	last_name=content['lastname']
	today_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	url_to_create_account=f'{obtaindomain()}/CreateNewAcccount.html'
	email_text = f"""
	Dear Person,
	Welecome aboard.  Please click the link below in order to create new account

	{url_to_create_account}

	Thank you,

	Soapology Management
	"""

	EMAIL ="chuchutainc@gmail.com"# os.environ.get("EMAIL")
	PASSWORD = "wlwittwcpblgpsqt"#os.environ.get("PASSWORD")

	GMAIL_USERNAME = EMAIL
	GMAIL_APP_PASSWORD = PASSWORD

	recipients = [email_recipient]#["avisemah@gmail.com"]
	msg = MIMEText(email_text)
	msg["Subject"] = "Email report: a simple sum"
	msg["To"] = ", ".join(recipients)
	msg["From"] = EMAIL#f"{GMAIL_USERNAME}@gmail.com"


	smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
	smtp_server.sendmail(msg["From"], recipients, msg.as_string())
	smtp_server.quit()
	return {'success':True,'msg':'sent email!'}
@app.route('/resetpassword', methods=['POST','GET'])
def resetpassword():
    print ('inside resetpassword')
    # if IsThereSecurityCookie()==False:
    # 	return {'success':False,'msg':'RelogginNeeded'}
    #uname= request.form['uname']  
    #psw=request.form['psw']
    today_date = datetime.now()
    new_today_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
    content = request.get_json(silent=True)
    #print(content['uname'])
    token=content['token']
    listOfresults=retruntokenandunamerecordforgiventoken(token)
    data_as_dict=listOfresults[1]
    wasused=data_as_dict[0]['wasused']
    uname=data_as_dict[0]['uname']
    if int(wasused)==1:
    	return {'success':False,'msg':f'password reset token has been already used.  Please issue a new one wasused={wasused} uname={uname}'}
    
    ## find uname based on token
    # uname=content['uname']
    # email=content['email']
    psw=content['psw']
    #return {'success':True,'msg':f'password was reset token={token} and pswe={psw},uname is {uname}'}
    # first_name=content['firstname']
    # last_name=content['lastname']
    password=psw
    last_updated=new_today_date
    # created=last_updated
    numberOfusersOfSameUname=int(returnCountOfRecordsOfGivenUserName(uname))
    # typeogf=str(type(numberOfusersOfSameUname))
    # return {'ret':typeogf}
    if numberOfusersOfSameUname==0:
    	return {'success':False,'msg':'this user does not exist in database'}
    res=updatepasswordonlyforusername(uname,password  ,last_updated,token)
    success=res[0]
    return {'success':success,'msg':res[1]}	#{"content":res}
def updatepasswordonlyforusername( uname,password  ,last_updated,token):
    defaultrole = 1
    defaultactive=1
    
    sqltext = f"UPDATE users SET password='{password}', last_updated='{last_updated}' where uname='{uname}';"
    sqltext_updatetokenstatus = f"UPDATE usernameandtokes SET wasused=1, last_updated='{last_updated}' where token='{token}';"
    # return (False,sqltext)
    
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext = "select * from States"
            cursor.execute(sqltext)
            cursor.execute(sqltext_updatetokenstatus)
            # cursor.execute('''select * from States''')
            connection.commit()
            # data = cursor.fetchall()
            return (True, '11')
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (False, {"error": f'{e}'})	

@app.route('/sendemailtoresetpassword', methods=['POST','GET'])
def sendemailtoresetpassword():
	# if IsThereSecurityCookie()==False:
	# 	return {'success':False,'msg':'RelogginNeeded'}#(False,"RelogginNeeded")
	content = request.get_json(silent=True)
	# print(content['uname'])
	# uname = content['uname']  
	uname=content['uname']    
    # listOfresults= returnAllUserDetailsForUserName(uname)      
    # data_as_dict=listOfresults[1]  
	listOfresults= returnAllUserDetailsForUserName(uname)  
	data_as_dict=listOfresults[1] 
	if len(data_as_dict)==0:
		return {'success':False,'msg':'no reset password was sent:username you provided does not exist'}
	today_date = datetime.now()
	created = today_date.strftime("%Y-%m-%d %H:%M:%S")
	result = uuid.uuid4()
	token=result.hex
	res=recordusernameandtoken(uname,token, created)
	if res[0]==False:
		return {'msg':res[1]}
	# first_name=content['firstname']
	# last_name=content['lastname']
	## need to produce token for uname and record in db
	email_recipient=data_as_dict[0]['email']#"avisemah@gmail.com"
	
	url_to_create_account=f'{obtaindomain()}/ResetPassword.html?token={token}'
	email_text = f"""
	Dear Person,
	Please click n the link below in order to reset password

	{url_to_create_account}

	Thank you,

	Soapology Management
	"""

	EMAIL ="chuchutainc@gmail.com"# os.environ.get("EMAIL")
	PASSWORD = "wlwittwcpblgpsqt"#os.environ.get("PASSWORD")

	GMAIL_USERNAME = EMAIL
	GMAIL_APP_PASSWORD = PASSWORD

	recipients = [email_recipient]#["avisemah@gmail.com"]
	msg = MIMEText(email_text)
	msg["Subject"] = "Email report: a simple sum"
	msg["To"] = ", ".join(recipients)
	msg["From"] = EMAIL#f"{GMAIL_USERNAME}@gmail.com"


	smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
	smtp_server.sendmail(msg["From"], recipients, msg.as_string())
	smtp_server.quit()
	return {'success':True,'msg':'sent email!'}
@app.route('/sendemailtogetusername', methods=['POST','GET'])
def sendemailtogetusername():
	# if IsThereSecurityCookie()==False:
	# 	return {'success':False,'msg':'RelogginNeeded'}#(False,"RelogginNeeded")
	content = request.get_json(silent=True)
	# print(content['uname'])
	email = content['email']  
	#uname=content['uname']    
    # listOfresults= returnAllUserDetailsForUserName(uname)      
    # data_as_dict=listOfresults[1]  
	listOfresults= returnAllUserDetailsEmail(email)  
	data_as_dict=listOfresults[1] 
	if len(data_as_dict)==0:
		return {'success':False,'msg':'no reset password was sent:email you provided does not exist'}
	uname=data_as_dict[0]['uname']
	# last_name=content['lastname']
	## need to produce token for uname and record in dbs
	email_recipient=email#data_asfdomain_dict[0]['email']#"avisemah@gmail.com"
	

	email_text = f"""
	Dear Person,
	Your username is 

	{uname}

	Thank you,

	Soapology Management
	"""

	EMAIL ="chuchutainc@gmail.com"# os.environ.get("EMAIL")
	PASSWORD = "wlwittwcpblgpsqt"#os.environ.get("PASSWORD")

	GMAIL_USERNAME = EMAIL
	GMAIL_APP_PASSWORD = PASSWORD

	recipients = [email_recipient]#["avisemah@gmail.com"]
	msg = MIMEText(email_text)
	msg["Subject"] = "Email report: a simple sum"
	msg["To"] = ", ".join(recipients)
	msg["From"] = EMAIL#f"{GMAIL_USERNAME}@gmail.com"


	smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
	smtp_server.sendmail(msg["From"], recipients, msg.as_string())
	smtp_server.quit()
	return {'success':True,'msg':'sent email!'}

def recordusernameandtoken(uname,token, created):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        #startdate_converted_to_date = datetime.strptime(workingday, '%Y-%m-%d')
        #startdate_no_time = startdate_converted_to_date.strftime("%Y-%m-%d %H:%M:%S")
        sqltext = f"INSERT INTO usernameandtokes ( uname,token, created,wasused) VALUES ('{uname}', '{token}','{created}',0);"
        # return (False,sqltext)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
            ssh_password=app.config["MYSQL_PASSWORD"],
            remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext = "select * from States"
            cursor.execute(sqltext)
            # cursor.execute('''select * from States''')
            connection.commit()
            # data = cursor.fetchall()
            return (True, '11')
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (False, {"error": f'error for {sqltext}\n {e}'})
#SELECT * FROM asemah$miscdb.usernameandtokes where token='980b780309ad44479bd6102d536249dd'
def retruntokenandunamerecordforgiventoken(token):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext="select * from users" #where uname='{uname}'""
            sqltext = f"SELECT * FROM usernameandtokes where token='{token}'"
            cursor.execute(sqltext)
            # cursor.execute('''select * from City''')
            rows = cursor.fetchall()
            # data_array=data['content']
            # firstrecord=data_array[0]
            # count=firstrecord[0]
            if True == False:
                main_list = []
                
                for row in rows:
                    current_list = []
                    for i in row:
                        current_list.append(i)
                    main_list.append(current_list)
                return main_list  # int([data[0]]['count'])
            else:
            	print('hiiiiiiiiiiiiiii',file=sys.stdout)
            	#ret={'type':str(type(rows))}
            	print(rows,file=sys.stdout)
            	return (True,evalluatListOfDictionaries(rows))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return ({"error":"while executing {sqltext}"+ str(e)})

@app.route('/sendemployeeidsetupinvitation', methods=['POST','GET'])
def sendemployeeidsetupinvitation():
	if IsThereSecurityCookie()==False:
		return {'success':False,'msg':'RelogginNeeded'}#(False,"RelogginNeeded")
	content = request.get_json(silent=True)
	# print(content['uname'])
	# uname = content['uname']
	email_recipient=content['email']
	email=email_recipient
	rightnow = datetime.now()
    # created = rightnow.strftime("%Y-%m-%d %H:%M:%S")
	created = rightnow.strftime("%Y-%m-%d %H:%M:%S")  
	first_name=content['firstname']
	last_name=content['lastname']
	today_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	result = uuid.uuid4()
	token=result.hex
	res=recordnewemployeetoken(email,token, created)
	url_to_create_account=f'{obtaindomain()}/SetupNewemployeeID.html?token={token}'
	email_text = f"""
	Dear Person,
	Welecome aboard.  Please click the link below in order to create new employee account

	{url_to_create_account}

	Thank you,

	Soapology Management
	"""

	EMAIL ="chuchutainc@gmail.com"# os.environ.get("EMAIL")
	PASSWORD = "wlwittwcpblgpsqt"#os.environ.get("PASSWORD")

	GMAIL_USERNAME = EMAIL
	GMAIL_APP_PASSWORD = PASSWORD

	recipients = [email_recipient]#["avisemah@gmail.com"]
	msg = MIMEText(email_text)
	msg["Subject"] = "Email report: a simple sum"
	msg["To"] = ", ".join(recipients)
	msg["From"] = EMAIL#f"{GMAIL_USERNAME}@gmail.com"
	smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
	smtp_server.sendmail(msg["From"], recipients, msg.as_string())
	smtp_server.quit()
	return {'success':True,'msg':'sent email!'}
def recordnewemployeetoken(email, token, created):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        # startdate_converted_to_date = datetime.strptime(workingday, '%Y-%m-%d')
        # startdate_no_time = startdate_converted_to_date.strftime("%Y-%m-%d %H:%M:%S")
        sqltext = f"INSERT INTO employeesetuptokens ( email,token, created,wasused) VALUES ('{email}', '{token}','{created}',0);"
        # return (False,sqltext)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
                  ssh_password=app.config["MYSQL_PASSWORD"],
                  remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
                     host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext = "select * from States"
            cursor.execute(sqltext)
            # cursor.execute('''select * from States''')
            connection.commit()
            # data = cursor.fetchall()
            return (True, '11')
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (False, {"error": f'error for {sqltext}\n {e}'})


def sendemployeenewemployeeidbyemail(email,newemployeeid):
	content = request.get_json(silent=True)
	# print(content['uname'])
	# uname = content['uname']
	email_recipient=email

	# rightnow = datetime.now()
 #    # created = rightnow.strftime("%Y-%m-%d %H:%M:%S")
	# created = rightnow.strftime("%Y-%m-%d %H:%M:%S")  
	# first_name=content['firstname']
	# last_name=content['lastname']
	# today_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
	# result = uuid.uuid4()
	# token=result.hex
	# res=recordnewemployeetoken(email,token, created)
	# url_to_create_account=f'{obtaindomain()}/SetupNewemployeeID.html?token={token}'
	email_text = f"""
	Dear Person,
	Welecome aboard.  Your new employee id is: {newemployeeid}

	Please make sure to retain this number wheenver clocking in or clocking out

	Thank you,

	Soapology Management
	"""

	EMAIL ="chuchutainc@gmail.com"# os.environ.get("EMAIL")
	PASSWORD = "wlwittwcpblgpsqt"#os.environ.get("PASSWORD")

	GMAIL_USERNAME = EMAIL
	GMAIL_APP_PASSWORD = PASSWORD

	recipients = [email_recipient]#["avisemah@gmail.com"]
	msg = MIMEText(email_text)
	msg["Subject"] = "Email report: a simple sum"
	msg["To"] = ", ".join(recipients)
	msg["From"] = EMAIL#f"{GMAIL_USERNAME}@gmail.com"
	smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
	smtp_server.sendmail(msg["From"], recipients, msg.as_string())
	smtp_server.quit()
	return {'success':True,'msg':'sent email!'}
@app.route('/createnewemployee', methods=['POST','GET'])
def createNewEmployee():
    print ('inside submit_login_form')
    if IsThereSecurityCookie()==False:
    	return {'success':False,'msg':'RelogginNeeded'}
    #uname= request.form['uname']  
    #psw=request.form['psw']
    today_date = datetime.now()
    new_today_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
    content = request.get_json(silent=True)
    #print(content['uname'])
    #uname=content['uname']
    email=content['email']
    dob=content['dob']
    token=content['token']
    first_name=content['firstname']
    last_name=content['lastname']
    # password=psw
    last_updated=new_today_date
    created=last_updated

    listOfresults=retruntokenandemailofnewemployeesetup(token)
    data_as_dict=listOfresults[1]
    wasused=data_as_dict[0]['wasused']
    #return {'success':False,'wasused':wasused,'type':str(type(wasused))}
    #uname=data_as_dict[0]['uname']
    if str(wasused)=='None':
    	# do nothing
    	a=1
    else:
	    if int(wasused)==1:
	    	return {'success':False,'msg':f'expired token! please make a request to admin to issue new employee setup'}
    #numberOfusersOfSameUname=int(returnCountOfRecordsOfGivenUserName(uname))
    # typeogf=str(type(numberOfusersOfSameUname))
    # return {'ret':typeogf}
    # if numberOfusersOfSameUname>0:
    # 	return {'success':False,'msg':'this user name is already taken'}	
    res=recordNewEmployee(dob, first_name, last_name,  last_updated, created, email,token)
    success=res[0]
    new_employee_id=''
    if success:
    	new_employee_id=res[2]
    	sendemployeenewemployeeidbyemail(email,new_employee_id)
    return {'success':success,'msg':res[1],'employeeid':new_employee_id}	#{"content":res}
def retruntokenandemailofnewemployeesetup(token):
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext="select * from users" #where uname='{uname}'""
            sqltext = f"SELECT * FROM employeesetuptokens where token='{token}'"
            cursor.execute(sqltext)
            # cursor.execute('''select * from City''')
            rows = cursor.fetchall()
            # data_array=data['content']
            # firstrecord=data_array[0]
            # count=firstrecord[0]
            if True == False:
                main_list = []
                
                for row in rows:
                    current_list = []
                    for i in row:
                        current_list.append(i)
                    main_list.append(current_list)
                return main_list  # int([data[0]]['count'])
            else:
            	print('hiiiiiiiiiiiiiii',file=sys.stdout)
            	#ret={'type':str(type(rows))}
            	print(rows,file=sys.stdout)
            	return (True,evalluatListOfDictionaries(rows))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return ({"error":"while executing {sqltext}"+ str(e)})

def recordNewEmployee(dob, first_name, last_name,  last_updated, created, email,token):
    defaultrole = 1
    
    
    sqltext = f"INSERT INTO employees (dob, email,first_name, last_name,  active, last_updated, created) VALUES ('{dob}','{email}', '{first_name}', '{last_name}',  1, '{last_updated}','{created}');"
    sqltext_updatetokenstatus = f"UPDATE employeesetuptokens SET wasused=1, last_updated='{last_updated}' where token='{token}';"
    
    try:
        # if not mysql.open:
        #     mysql.ping(reconnect=True)
        # cursor = mysql.cursor(pymysql.cursors.DictCursor)
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'), ssh_username=app.config["MYSQL_USER"],
        ssh_password=app.config["MYSQL_PASSWORD"],
        remote_bind_address=(app.config["MYSQL_HOST"], 3306)) as tunnel:
            connection = pymysql.connect(user=app.config["MYSQL_USER"], password=app.config["MYSQL_PASSWORD"],
            host=HOST12701, port=tunnel.local_bind_port, db=app.config["MYSQL_DB"])
            
            cursor = connection.cursor()
            # sqltext="select * from City where name='"+ city+ "'"
            # sqltext = "select * from States"
            cursor.execute(sqltext_updatetokenstatus)
            cursor.execute(sqltext)
            cursor.execute('SELECT LAST_INSERT_ID()')
            cursor.lastrowid = cursor.fetchone()[0]  
            last_id=cursor.lastrowid
            # cursor.execute('''select * from States''')
            connection.commit()
            # data = cursor.fetchall()
            return (True, '11',last_id)
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return (False, {"error": f'{e}\nsql: {sqltext}'})	


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