#This is a simple python script to run a home automation system using raspberry pi
#For Complete Tutorial, visit http://rootsaid.com/home-automation-raspberry-pi/

import RPi.GPIO as GPIO
import socket
import csv

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)

UDP_IP = "0.0.0.0"
UDP_PORT = 5050

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

while True:
 data, addr = sock.recvfrom(1024)
 raw=data
 #print raw
  if raw=="device1on":
   GPIO.output(11,True)
   print "Device One Turned On"
 
  elif raw=="device1off":
   GPIO.output(11,False)
   print "Device One Turned Off"

  elif raw=="device2on":
   GPIO.output(13,true)
   print "Device Two Turned On"
 
  elif raw=="device2off":
   GPIO.output(13,False)
   print "Device Two Turned Off"
   
  elif raw=="device3on":
   GPIO.output(15,True)
   print "Device Three Turned On"
 
  elif raw=="device3off":
   GPIO.output(15,False)
   print "Device Three Turned Off"

  elif raw=="device4on":
   GPIO.output(29,True)
   print "Device Four Turned On"
 
  elif raw=="device4off":
   GPIO.output(29,False)
   print "Device Four Turned Off"
