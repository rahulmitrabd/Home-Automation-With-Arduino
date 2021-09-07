import time
try:
	from pyfirmata import Arduino, util
except:
	from pip._internal import main
	main(['install','pyfirmata'])
	from pyfirmata import Arduino, util
board = Arduino('COM4')
iterator = util.Iterator(board)
iterator.start()
Tv1 = board.get_pin('a:0:1')
led = board.get_pin('d:9:d')
time.sleep(1.0)
while(True):
	print((Tv1.read()*5000.0-500)/10)
	board.digital[13].write(1)
	time.sleep(5)
	board.digital[13].write(0)
	time.sleep(2)








	if (trainingdatafordev1 < 25):
		print('training data is lower than 40')
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