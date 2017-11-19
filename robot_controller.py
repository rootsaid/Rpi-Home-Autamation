#This is a simple python script to move a raspberry pi robot using WiFi
#For Complete Tutorial, visit http://rootsaid.com/robot-control-over-wifi/

import RPi.GPIO as GPIO
import 
socket
import 
csv

GPIO.setwarnings(False)



GPIO.setmode(GPIO.BOARD)

GPIO.setup(33,GPIO.OUT)

GPIO.setup(11,GPIO.OUT)


GPIO.setup(13,GPIO.OUT)

GPIO.setup(15,GPIO.OUT)


GPIO.setup(29,GPIO.OUT)

GPIO.setup(31,GPIO.OUT)



GPIO.output(29,True)

GPIO.output(31,True)



UDP_IP = "0.0.0.0"
UDP_PORT = 5050

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

sock.bind((UDP_IP, UDP_PORT))


while True:
    
data, addr = sock.recvfrom(1024)
    
raw=data
    
print raw
   
 
if raw=="forward":
 	
GPIO.output(33,True)
GPIO.output(11,False)
GPIO.output(13,True)
GPIO.output(15,False)
print "Robot Move Forward"
  
  
elif raw=="stop":

GPIO.output(33,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)
print "Robot Stop"
    

elif raw=="backward":
	
GPIO.output(33,False)
GPIO.output(11,True)
GPIO.output(13,False)
GPIO.output(15,True)
print "Robot Move Backward"


elif raw=="left":

GPIO.output(33,False)
GPIO.output(11,True)
GPIO.output(13,True)
GPIO.output(15,False)	
print "Robot Move Left"

elif raw=="right":
GPIO.output(33,True)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,True)	
print "Robot Move Right"

else:
print "STOP"
GPIO.output(33,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)