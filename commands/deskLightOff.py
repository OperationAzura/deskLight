import RPi.GPIO as GPIO

pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.LOW)


