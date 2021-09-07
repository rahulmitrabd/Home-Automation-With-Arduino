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
    indata=int(input("Please enter command= "))

    if(indata==1):
	    board.digital[13].write(1)
    if(indata==0):
	    board.digital[13].write(0)
data=board.get_pin('a:0:1')
