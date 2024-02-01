import RPi.GPIO as GPIO
import time

button_pin1 = 22
button_pin2 = 23
button_pin3 = 24
button_pin4 = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin1, GPIO.IN)
GPIO.setup(button_pin2, GPIO.IN)
GPIO.setup(button_pin3, GPIO.IN)
GPIO.setup(button_pin4, GPIO.IN)

while(1):
	if GPIO.input(button_pin1) == GPIO.LOW:
		print("Button 1 pushed!!")
	time.sleep(0.1)
	if GPIO.input(button_pin2) == GPIO.LOW:
		print("Button 2 pushed!!")
	time.sleep(0.1)
	if GPIO.input(button_pin3) == GPIO.LOW:
		print("Button 3 pushed!!")
	time.sleep(0.1)
	if GPIO.input(button_pin4) == GPIO.LOW:
		print("Button 4 pushed!!")
	time.sleep(0.1)

GPIO.cleanup()
