import RPi.GPIO as GPIO
import time
import subprocess

echoPin = 16
triggerPin = 18
pulse_start = time.time()
pulse_end = time.time()
on = True

GPIO.setmode(GPIO.BOARD)

print "Distance measurement in progress"

GPIO.setup(echoPin,GPIO.IN)
GPIO.setup(triggerPin,GPIO.OUT)                  #Set pin as GPIO out
subprocess.call("deskLightOn")

while True:

  GPIO.output(triggerPin, False)                 #Set TRIG as LOW
  print "Waitng For Sensor To Settle"
  time.sleep(1)                            #Delay of 2 seconds

  GPIO.output(triggerPin, True)                  #Set TRIG as HIGH
  time.sleep(0.0001)                      #Delay of 0.00001 seconds
  GPIO.output(triggerPin, False)                 #Set TRIG as LOW
  if GPIO.input(echoPin)==0:
    print "signal is low"

  while GPIO.input(echoPin)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(echoPin)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 2 and distance < 400:      #Check whether the distance is within range
    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    if on:
      on = False
      subprocess.call("deskLightOff")
    else:
      on = True
      subprocess.call("deskLightOn")
  else:
    print "Out Of Range"        

