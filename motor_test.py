#!/usr/bin/pyhton
#Imports the RPi.GPIO module to interact with the GPIO's
import RPi.GPIO as GPIO
#import time to use time.sleep(X)
import time
# import sys to use sys.ext
import sys

# ---------- Motor setup -------
# Right forward:
# 	7 False 
#	11 True
# Left forward:
# 	13 True
# 	15 False

# ------- Functions -------
def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)

def turn_off():
	GPIO.output(7, False)
	GPIO.output(11, False)
	GPIO.output(13, False)
	GPIO.output(15, False)

def left_motor_forward():
	GPIO.output(13, False)
	GPIO.output(15, True)

def left_motor_backward():
	GPIO.output(13, True)
	GPIO.output(15, False)

def right_motor_forward():
	GPIO.output(7, True)
	GPIO.output(11, False)

def right_motor_backward():
	GPIO.output(7, False)
	GPIO.output(11, True)

def forward():
	left_motor_forward()
	right_motor_forward()

def backward():
	left_motor_backward()
	right_motor_backward()

def turn_left():
	left_motor_backward()
	right_motor_forward()

def turn_right():
	left_motor_forward()
	right_motor_backward()

def command_entered(command):
	if (command == 'c'):
		forward()
		time.sleep(1)
	elif (command == 'h'):
		turn_left()
		time.sleep(0.3)
	elif (command == 't'):
		backward()
		time.sleep(1)
	elif (command == 'n'):
		turn_right()
		time.sleep(0.3)


# ------- END OF FUNCTIONS ---------
init()
print " C is forward \n H is right \n T is backward \n N is left \n 0 to quit)"
print "Enter command:"
try:
	while(True):
		command = raw_input(": ")
		if (command == '0'):
			print "Exit..."
			break
		command_entered(command)
		turn_off()
except KeyboardInterrupt:  
	print "\nExiting..."
	turn_off()
	GPIO.cleanup() # clean up on ctrl->C exit  
	sys.exit()
time.sleep(1)
turn_off()
GPIO.cleanup()
