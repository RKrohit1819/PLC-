import requests
import mysql.connector
import datetime

try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="db_machine"
        )
        mycursor = mydb.cursor()
        sql="SELECT * FROM historian_data WHERE sync=b'0' ORDER BY serial ASC"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for data in myresult:
                SERIAL=data[0]
                OK=data[1]
                NG=data[2]
                BY_PASS=data[3]
                CYCLE_TIME=data[7]
                DEVICE_TIME_STAMP=data[4]
                DEVICE_DATE=data[6]
                MACHINE_ID=data[5]
                DEVICE_TIME=DEVICE_TIME_STAMP.strftime("%H:%M:%S")
                URL="http://192.168.3.19/eol/module/autoprn/API/api/data.php?ok=" + str(OK) +"&ng=" + str(NG)+ "&by_pass=" + str(BY_PASS)+ "&mac_id=" +str(MACHINE_ID)+"&actual_cycle_time="+str(CYCLE_TIME)+"&device_date="+str(DEVICE_DATE)+"&device_time="+str(DEVICE_TIME);
                #print(str(SERIAL),str(OK),str(NG), str(BY_PASS),str(CYCLE_TIME),str(DEVICE_TIME_STAMP),str(DEVICE_DATE),str(MACHINE_ID))
                print(URL)
                r = requests.get(URL)
                if(r.status_code==200):
                        sql="UPDATE historian_data SET sync=b'1' WHERE serial="+str(SERIAL)
                        mycursor.execute(sql)
                        mydb.commit()
                        print(r.text)
except:
        print("Error!")
                
        

#print (r.status_code)
#print (r.headers)
#print (r.text)
