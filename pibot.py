 

import RPi.GPIO as GPIO 
import time
 

#use board mode for the numbers
GPIO.setmode(GPIO.BOARD)
#set the gpio pins for the servos as output
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
#set set up pwm objects.  first param is the pin, second param is the power
rpwm = GPIO.PWM(12, 100)
lpwm = GPIO.PWM(16, 100)
#start the pwm at 0
rpwm.start(0)
lpwm.start(0)
 
#the continuous rotation servos will recognize 0 as signal to move forward and 180 to move backwards
####DO NOT ALTER THESE 4 FUNCTIONS#####
def forward(tm):
    print "moving servo forward"
    #right servo signal to move forward
    rdirect=0
    #because servo is flipped we need to make the left go opposite
    ldirect=180
    #because we set set the gpio as input to turn off the servos we will turn them back to outputs
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    #calculation for converting the degrees to the pwm frequency
    rduty = float(rdirect) / 10.0 + 2.5
    lduty = float(ldirect) / 10.0 + 2.5
    #these lines sends the frequencies to the servos
    rpwm.ChangeDutyCycle(rduty)
    lpwm.ChangeDutyCycle(lduty)
    time.sleep(tm)
 
def backward(tm):
    print "moving servo backward"
    rdirect=180
    #because servo is flipped we need to make the left go opposite
    ldirect=0
     #because we set set the gpio as input to turn off the servos we will turn them back to outputs
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    #calculation for converting the degrees to the pwm frequency
    rduty = float(rdirect) / 10.0 + 2.5
    lduty = float(ldirect) / 10.0 + 2.5
     #these lines sends the frequencies to the servos
    rpwm.ChangeDutyCycle(rduty)
    lpwm.ChangeDutyCycle(lduty)
    time.sleep(tm)
 
def left(tm):
    print "moving servo left"
    rdirect=0
    ldirect=0
     #because we set set the gpio as input to turn off the servos we will turn them back to outputs
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
     #calculation for converting the degrees to the pwm frequency
    rduty = float(rdirect) / 10.0 + 2.5
    lduty = float(ldirect) / 10.0 + 2.5
     #these lines sends the frequencies to the servos
    rpwm.ChangeDutyCycle(rduty)
    lpwm.ChangeDutyCycle(lduty)
    time.sleep(tm)
def right(tm):
    print "moving servo right"
    rdirect=180
    ldirect=180
     #because we set set the gpio as input to turn off the servos we will turn them back to outputs
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
     #calculation for converting the degrees to the pwm frequency
    rduty = float(rdirect) / 10.0 + 2.5
    lduty = float(ldirect) / 10.0 + 2.5
     #these lines sends the frequencies to the servos
    rpwm.ChangeDutyCycle(rduty)
    lpwm.ChangeDutyCycle(lduty)
    time.sleep(tm)
 
####END OF FUNCTIONS##################
 
 
#### customize path by changing function calls below#################
 
#these are examples
 
#goes forward for 90 seconds
forward(1)
#goes backwards for 200 seconds
backward(1)
#rotates left for 120 seconds
left(1)
#rotates right for 70 seconds
right(1)
#rotates left for half a second
left(1)
