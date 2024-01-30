import RPi.GPIO as GPIO
import time

led_red = 4
led_green = 5
led_blue = 6

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)

try:
	print("3 Color LED Control Start !!\n")
	for i in range(5):
		print("Red LED On!!\n")
		GPIO.output(led_red, True)
		time.sleep(0.5)
		print("Red LED Off !!\nGreen LED On !!\n")
		GPIO.output(led_red, False)
		GPIO.output(led_green, True)
		time.sleep(0.5)
		print("Green LED Off !!\nBlue LED On !!\n")
		GPIO.output(led_green, False)
		GPIO.output(led_blue, True)
		time.sleep(0.5)
		print("Blue LED Off")
		GPIO.output(led_blue, False)

except KeyboardInterrupt:
	pass

GPIO.cleanup()
