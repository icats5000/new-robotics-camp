 #!/usr/bin/python
import RPi.GPIO as GPIO
import time

#set up the
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 100)

pwm.start(0)

def forward():
    print "moving servo forward"
    direct=180
    GPIO.setup(12, GPIO.OUT)
    duty = float(direct) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)

def backward():
    print "moving servo forward"
    direct=0
    GPIO.setup(12, GPIO.OUT)
    duty = float(direct) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)



forward()
time.sleep(3)
backward()
time.sleep(3)


