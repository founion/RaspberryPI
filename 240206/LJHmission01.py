import RPi.GPIO as GPIO
import time

led_pins = [14, 15, 18]  #red는 14, green은 15, blue는 18에 연결

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pins, GPIO.OUT)

GPIO.output(led_pins, GPIO.LOW)

try:
	print("3 Color LED Control Start !!\n")
	for i in range(10):
		print("Red LED On!!\n")
		GPIO.output(led_pins[0], True)
		time.sleep(0.5)
		print("Red LED Off !!\nGreen LED On !!\n")
		GPIO.output(led_pins[0], False)
		GPIO.output(led_pins[1], True)
		time.sleep(0.5)
		print("Green LED Off !!\nBlue LED On !!\n")
		GPIO.output(led_pins[1], False)
		GPIO.output(led_pins[2], True)
		time.sleep(0.5)
		print("Blue LED Off")
		GPIO.output(led_pins[2], False)

except KeyboardInterrupt:
	pass

GPIO.cleanup()
