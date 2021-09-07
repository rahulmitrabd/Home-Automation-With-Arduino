import time as t
import sqlite3
from datetime import *
try:
	from pyfirmata import Arduino, util
except:
	from pip._internal import main
	main(['install','pyfirmata'])
	from pyfirmata import Arduino, util
board = Arduino('COM4')
iterator = util.Iterator(board)
data1 = board.get_pin('a:0:1')
data2 = board.get_pin('a:1:1')
data3 = board.get_pin('a:2:1')
data4 = board.get_pin('a:3:1')
devID=1001
stsdev1=1
conn = sqlite3.connect('automation.db')
print ("Opened database successfully")
#conn.execute('''CREATE TABLE data
#         (deviceID INT PRIMARY KEY     NOT NULL,
#         type           TEXT    NOT NULL,
#         AGE            INT     NOT NULL,
#         ADDRESS        CHAR(50),
 #        SALARY         REAL);''')
#conn.execute('''CREATE TABLE device
#            (deviceID INT PRIMARY KEY  NOT NULL,
#            type TEXT,
#            power INT);''')
#print ('Table created successfully')
#conn.execute('''CREATE TABLE data
#            (deviceID INT ,
#            crndata INT,
#            vltdata INT,
#            time [timestamp]);''')
#print ('Table created successfully')

iterator.start()
t.sleep(1.0)
while(True):
    print('Reading from Sensor')
    dev1crn = (data1.read() * 5000.0 - 500) / 10
    dev1vlt = (data2.read() * 5000.0 - 500) / 10
    dev2crn = (data3.read() * 5000.0 - 500) / 10
    dev2vlt = (data4.read() * 5000.0 - 500) / 10
    #print(dev1crn)
    #print(dev2vlt)
    acceptedvoltdev1 = []
    acceptedcrndev1 = []

    cursor1 = conn.execute("SELECT count(*) FROM data WHERE deviceID=1001 AND status=1")
    for row in cursor1:
        trainingdatafordev1=int(row[0])
        print(trainingdatafordev1)
#Grabbing voltage data for Device 1
        grabvoltdatadev1 = conn.execute("SELECT SUM(vltdata) FROM data WHERE deviceID=1001 AND status=1")
        for row in grabvoltdatadev1:
            acceptedvoltdev1.append(row[0])
            print("total= ", row[0])
            voltdatadev1 = int(acceptedvoltdev1[0]) / trainingdatafordev1
            thrsvoltdev1=voltdatadev1+5
            print(voltdatadev1)
#Grabbing current data for Device 1

        grabcrndatadev1 = conn.execute("SELECT SUM(crndata) FROM data WHERE deviceID=1001 AND status=1")
        for row in grabcrndatadev1:
            acceptedcrndev1.append(row[0])
            print("total= ", row[0])
            crndatadev1 = int(acceptedcrndev1[0]) / trainingdatafordev1
            print(crndatadev1)
            thrscurrentdev1=crndatadev1+5
            print("Real time current: ", dev1crn)
            print("Real time Voltage: ", dev1vlt)
            print("Threshold Voltage: ", thrsvoltdev1)
            print("Threshold Current: ", thrscurrentdev1)
        if(dev1crn<thrscurrentdev1):
            board.digital[13].write(1)
            print("Device No: 1, Working Normally")
            if (trainingdatafordev1 < 250):
                print('training data is lower than 250')
                # inputtime =datetime.time()
                curnttime = str(datetime.now().time())
                conn.execute("INSERT INTO data (deviceID,crndata,vltdata,time,status) \
                         VALUES (?,?,?,?,?)", (devID, dev1vlt, dev1crn, curnttime, stsdev1))
                conn.commit()
                print("data successfully saved to database")
                t.sleep(0)
            else:
                print('Breaking this operation')
                break

        else:
            print("Short Circuit Detected on Device 1")
            board.digital[13].write(0)


    print('Successfully returned to the next process')
    print("Device No 2 Not connected")
    print("Device No 3 Not connected")
    print("Device No 4 Not connected")
    print("Device No 5 Not connected")

    t.sleep(2)

        #    conn.execute("INSERT INTO data (deviceID,crndata,vltdata) \
        #          VALUES (?,?,?)",(devID,dev1vlt,dev1crn))
        #    conn.commit()
        #else:
          #  continue
# This part controls the microcontroller
