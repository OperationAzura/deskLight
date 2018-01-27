import RPi.GPIO as GPIO
import time
import subprocess

echoPin = 16 #pin that receives signal from the ultra sonic sensor
triggerPin = 18 #pin to trigger the ultrasonic sensor
pulse_start = time.time() #variable for mesuring echo lenght
pulse_end = time.time() #variable for measuring the echo length
on = True #variable to keep trac if te light is on or off

GPIO.setmode(GPIO.BOARD) #Set the GPIO pin numbering scheme
GPIO.setup(echoPin,GPIO.IN) #setup the echo pin to receive
GPIO.setup(triggerPin,GPIO.OUT) #set up the trigger pin to send signals
subprocess.call("deskLightOn") #run the command to turn the desk light on by default

while True: #infinite loop
  GPIO.output(triggerPin, False) #set trigger pin low to get ready to send
  time.sleep(1) #sleep for a second

  GPIO.output(triggerPin, True) #send the trigger signal to the sensor
  time.sleep(0.00001) #wait for signal
  GPIO.output(triggerPin, False) #stop sending signal

  while GPIO.input(echoPin)==0: #while the echo pin reads low, as in no signal
    pulse_start = time.time() #Saves the last known time of LOW pulse

  while GPIO.input(echoPin)==1: #while the echo pin is receiving signal
    pulse_end = time.time() #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #saves the pulse duration
  distance = pulse_duration * 17150 #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2) #Round to two decimal points

  if distance > 2 and distance < 400: #Check whether the distance is within range
    if on: #if the light is on, turn it off
      on = False
      subprocess.call("deskLightOff")
    else: #if the light is off, turn it on
      on = True
      subprocess.call("deskLightOn")
