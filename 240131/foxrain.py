import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(10.0)

scale = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88, 523.25]
fox = [3,2,3,2,\
	3,5,3,\
	3,2,3,2,\
	3,5,3,\
	3,2,3,4,5,\
	3,2,3,4,5,\
	3,2,3,4,5,7,5
]

try:
	for i in range(0,31):
		pwm.ChangeFrequency(scale[fox[i]])
		if i==3 or i==10:
			time.sleep(0.4)
		elif i==6 or i==13 or i==18 or i==23:
			time.sleep(0.8)
		else:
			time.sleep(0.3)

finally:
	GPIO.cleanup()
