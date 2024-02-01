import RPi.GPIO as GPIO
import time

buzzer = 18
PIR = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(PIR, GPIO.IN)

GPIO.output(buzzer, False)

try:
	while 1:
		if GPIO.input(27):
			print("Detected")
			GPIO.output(buzzer, True)
		else:
			print("Not Detected")
			GPIO.output(buzzer, False)
		time.sleep(0.5)

except KeyboardInterrupt:
	pass

GPIO.cleanup()
