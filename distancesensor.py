import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == False:
    start= time.time()

while GPIO.input(ECHO) == True:
    end = time.time()

sig_time = end_start()

#CM:
distance = sig_time / 0.000058

#inches:
#distance = sig_time / 0.000148
while True:
    print('Distance: {} centimeters'.format(distance))

