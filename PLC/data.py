import siemens
import db
import datetime
from time import sleep
MACHINE_ID="Edge-Device-001"
siemens.plc.connect('192.168.1.34', 0, 1)  #IP address, rack, slot (from HW settings)

#GET PCL INFO
#plc_info=siemens.plc.get_cpu_info()
#print(plc_info.ModuleTypeName)
#print(plc_info.Copyright)
#print(siemens.plc.get_cpu_state())
OK=0
NG=0
BY_PASS=0
PROCESS_START_BIT=False
PROCESS_STOP_BIT=False
PROCESS_START_FLAG=False
PROCESS_STOP_FLAG=False
CYCLE_TIME=0
timeStamp=""
today_date=""
while(True):
    try:
        byte_ar=siemens.plc.db_read(35,8,1)
        PROCESS_START_BIT=siemens.get_bool(byte_ar,0,0)
        #print("PROCESS_START_BIT:"+str(PROCESS_START_BIT))
        if(PROCESS_START_BIT==True):
            PROCESS_START_FLAG=True
            PROCESS_STOP_FLAG=False
            while(True):
                byte_ar=siemens.plc.db_read(35,8,2)
                PROCESS_STOP_BIT=siemens.get_bool(byte_ar,0,1)
                #print("PROCESS_STOP_BIT:"+str(PROCESS_STOP_BIT))
                sleep(0.5)
                if(PROCESS_STOP_BIT==True):
                    try:
                        PROCESS_STOP_FLAG=True
                        PROCESS_START_FLAG=False
                        date_time_now=datetime.datetime.now()
                        time_stamp=date_time_now.strftime("%Y-%m-%d %H:%M:%S")
                        today_date=date_time_now.strftime("%Y-%m-%d")
                        byte_ar=siemens.plc.db_read(35,0,4)
                        OK=siemens.get_udint(byte_ar,0)
                        byte_ar=siemens.plc.db_read(35,4,4)
                        NG=siemens.get_udint(byte_ar,0)
                        byte_ar=siemens.plc.db_read(35,270,4)
                        CYCLE_TIME=siemens.get_udint(byte_ar,0)
                        P_DATE=today_date
                        DEVICE_DATE=today_date
                        DEVICE_TIME_STAMP=time_stamp
                        db.db_data(OK,NG,BY_PASS,MACHINE_ID, P_DATE,CYCLE_TIME,DEVICE_TIME_STAMP,DEVICE_DATE)
                        PROCESS_STOP_FLAG=False
                        sleep(2)
                        break
                    except:
                        print("PLC Read Error!")
        else:
            PROCESS_START_FLAG=False
    except:
        print("PLC Read Error!")
        
'''
while(True):
        byte_ar=siemens.plc.db_read(35,0,4)
        print(siemens.get_udint(byte_ar,0))
        byte_ar=siemens.plc.db_read(35,4,4)
        print(siemens.get_udint(byte_ar,0))
        #print(readBool(35,8,1))
        byte_ar=siemens.plc.db_read(35,8,1)
        #print(byte_ar)
        print(siemens.get_bool(byte_ar,0,1))
        byte_ar=siemens.plc.db_read(35,270,4)
        #print(byte_ar)
        print(siemens.get_udint(byte_ar,0))
'''
