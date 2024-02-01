import RPi.GPIO as GPIO
import time

button_pin = 22
led_pin = 18

led_state = GPIO.LOW;
led_state_changed = False;

def button_pressed(channel):
	global led_state
	global led_state_changed
	led_state = GPIO.HIGH if led_state == GPIO.LOW else GPIO.LOW
	led_state_changed = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

GPIO.add_event_detect(button_pin, GPIO.RISING, callback = button_pressed, bouncetime = 200)

try:
	while True:
		if led_state_changed:
			led_state_changed = False
			GPIO.output(led_pin, led_state)
		time.sleep(0.1)
except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()
