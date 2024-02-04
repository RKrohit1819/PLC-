#sudo pip install mysql-connector-python==8.0.29
import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='mysql',
  database="db_machine"
)
mycursor = mydb.cursor()


def db_data(OK,NG,BY_PASS,MACHINE_ID, P_DATE, ACTUAL_CYCLE_TIME,DEVICE_TIME_STAMP,DEVICE_DATE):
    sql = "INSERT INTO production_data (ok, ng,by_pass, machine_id, p_date, actual_cycle_time, device_time_stamp,device_date) VALUES ("+str(OK)+","+str(NG)+","+str(BY_PASS)+",'"+str(MACHINE_ID)+"','"+ str(P_DATE)+"'," +str(ACTUAL_CYCLE_TIME)+",'"+str(DEVICE_TIME_STAMP)+"','"+str(DEVICE_DATE)+"') ON DUPLICATE KEY UPDATE ok="+str(OK)+",ng="+str(NG)+", by_pass="+str(BY_PASS)+", machine_id='"+str(MACHINE_ID)+"', actual_cycle_time="+str(ACTUAL_CYCLE_TIME)+", device_time_stamp='"+str(DEVICE_TIME_STAMP)+"', device_date='"+str(DEVICE_DATE)+"';"
    sql1= "INSERT INTO historian_data (ok, ng,by_pass, machine_id, p_date, actual_cycle_time, device_time_stamp,device_date) VALUES ("+str(OK)+","+str(NG)+","+str(BY_PASS)+",'"+str(MACHINE_ID)+"','"+ str(P_DATE)+"'," +str(ACTUAL_CYCLE_TIME)+",'"+str(DEVICE_TIME_STAMP)+"','"+str(DEVICE_DATE)+"')"
    #print(sql)
    mycursor.execute(sql)
    mydb.commit()
    #print(sql1)
    mycursor.execute(sql1)
    mydb.commit()
    
#db_data(0,0,0,'1234','2022-1-1',0,'2022-1-1 00;00:00','2022-1-1')

