import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(10.0)

scale = [523.25, 587.33, 659.26, 698.46, 784, 880, 987.77]
airplane = [3,3,1,2,\
	3,3,3,\
	2,2,2,\
	3,5,5,\
	3,2,1,3,\
	3,3,3,\
	2,2,3,2,1
]

try:
	for i in range(0,25):
		index = airplane[i] % len(scale)
		pwm.ChangeFrequency(scale[index])
		if i==6 or i==9 or i==12 or i==16 or i==19:
			time.sleep(1.0)
		else:
			time.sleep(0.5)

finally:
	GPIO.cleanup()
