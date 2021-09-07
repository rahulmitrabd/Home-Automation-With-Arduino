import time
import sqlite3
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
devID=1
conn = sqlite3.connect('automation.db')
print ("Opened database successfully")
#conn.execute('''CREATE TABLE data
#         (deviceID INT PRIMARY KEY     NOT NULL,
#         type           TEXT    NOT NULL,
#         AGE            INT     NOT NULL,
#         ADDRESS        CHAR(50),
 #        SALARY         REAL);''')
#conn.execute('''CREATE TABLE device
#            (deviceID INT ,
#            type TEXT,
#            power INT);''')
#print ('Table created successfully')
conn.execute('''CREATE TABLE data
            (deviceID INT ,
            crndata INT,
            vltdata INT);''')
print ('Table created successfully')


iterator.start()
time.sleep(1.0)
while(True):
    print('Reading from Sensor')
    dev1crn = (data1.read() * 5000.0 - 500) / 10
    dev1vlt = (data2.read() * 5000.0 - 500) / 10
    dev2crn = (data3.read() * 5000.0 - 500) / 10
    dev2vlt = (data4.read() * 5000.0 - 500) / 10
    print(dev1crn)
    print(dev2vlt)
    conn.execute("INSERT INTO data (deviceID,crndata,vltdata) \
          VALUES (?,?,?)",(devID,dev1vlt,dev1crn))
    conn.commit()
    time.sleep(2)
