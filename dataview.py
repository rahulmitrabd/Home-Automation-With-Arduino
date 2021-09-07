import sqlite3
import time as t
conn = sqlite3.connect('automation.db')
print ("Opened database successfully")
while(True):
   # cursor = conn.execute("SELECT * from data")

    #for row in cursor:
    #   print ("ID = ", row[0])
     #  print ("Voltage = ", row[1])
     #  print ("Current = ", row[2])

    #print ("Operation done successfully")
    acceptedvoltdev1=[]
    grabdatadev1= conn.execute("SELECT SUM(vltdata) FROM data WHERE deviceID=1001 AND status=1")

    for row in grabdatadev1:
       acceptedvoltdev1.append(row[0])
       print("total= ", row[0])
       datadev1=int(acceptedvoltdev1[0])/25
       print(datadev1)
       t.sleep(2)
conn.close()