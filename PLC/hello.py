import datetime
#sudo pip install mysql-connector-python==8.0.29
import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='mysql',
  database="db_machine"
)
mycursor=""
mycursor= mydb.cursor()
DEVICE_DATE="2023-1-9"
sql="SELECT * FROM production_data WHERE p_date='"+DEVICE_DATE+"' ORDER BY serial DESC LIMIT 1"
DEVICE_DATE="2023-1-10"
mycurser.execute(sql)
myresult = mycursor.fetchall()
PREV_OK=0
PREV_NG=0
for data in myresult:
	PREV_OK=data[1]
	PREV_NG=data[2]
	PREV_BY_PASS=data[3]
	PREV_DATE=data[6]    
	print(PREV_OK, PREV_NG, PREV_BY_PASS, PREV_DATE)      
if PREV_DATE!=DEVICE_DATE:
	PREV_DATE=DEVICE_DATE
	#siemens.writeBool(35,8,2,1)
	#sleep(1)
	#siemens.writeBool(35,8,2,0)
	OK=OK-PREV_OK
	NG=NG-PREV_NG
	BY_PASS=BY_PASS-PREV_BY_PASS
	#call
	PREV_OK=OK
	PREV_NG=NG
	PREV_BY_PASS=BY_PASS
else:
	#call
	print("HELLO")
