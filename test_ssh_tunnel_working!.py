import pymysql
from sshtunnel import SSHTunnelForwarder

MYSQL_USER = 'asemah'
MYSQL_PASSWORD = 'Newburg822!'  # Replace with your actual MySQL password
MYSQL_HOST = 'asemah.mysql.pythonanywhere-services.com'
MYSQL_DB = 'asemah$miscdb'  # Replace with your actual database name
SSH_PASSWORD = MYSQL_PASSWORD#  # Replace with your actual SSH password

try:
    with SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username=MYSQL_USER,
        ssh_password=SSH_PASSWORD,
        remote_bind_address=(MYSQL_HOST, 3306)
    ) as tunnel:
        connection = pymysql.connect(
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            host='127.0.0.1',
            port=tunnel.local_bind_port,
            db=MYSQL_DB
        )
        cursor = connection.cursor()
        cursor.execute('SELECT 1')
        result = cursor.fetchone()
        if result:
            print("Connection successful!")
        else:
            print("Connection failed.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
