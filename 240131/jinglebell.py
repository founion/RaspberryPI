import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)
pwm.start(5.0)

scale = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.89, 523.25, 622.25]
bell = [1,6,5,4,1,\
	1,6,5,4,2,\
	1,7,6,5,3,\
	8,8,7,5,6,4,\
	1,6,5,4,1,\
	1,6,5,4,2,\
	2,7,6,5,8,8,8,8,9,8,7,5,4,\
	6,6,6,6,6,6,6,8,4,5,6,\
	7,7,7,7,7,6,6,6,6,5,5,4,5,8,\
	6,6,6,6,6,6,6,8,4,5,6,\
	7,7,7,7,7,6,5,5,8,8,7,5,4
]

try:
	for i in range(0,93):
		index = bell[i] % len(scale)
		pwm.ChangeFrequency(scale[index])

		if i==4 or i==9 or i==14 or i==20 or i==25 or i==30 or i ==43 or i==54 or i==68 or i==79:
			time.sleep(1.0)
		else:
			time.sleep(0.5)

finally:
	GPIO.cleanup()
