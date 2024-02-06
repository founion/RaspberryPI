import RPi.GPIO as GPIO
import time

button_sw = [22, 23, 24, 25]  # sw1은 22번, sw2는 23번, sw3은 24번, sw4는 25번에 연결
buzzer = 18  # buzzer는 18번에 연결

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(button_sw, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0)
scale = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.89, 523.25, 622.25]

def twinkle():
	print("재생 중인 곡 : Twinkle")
	pwm.start(10.0)
	twinkle = [1,1,5,5,6,6,5,4,4,3,3,2,2,1,\
		5,5,4,4,3,3,2,5,5,4,4,3,3,2,\
		1,1,5,5,6,6,5,4,4,3,3,2,2,1]

	for i in range(0, len(twinkle)):
		pwm.ChangeFrequency(scale[twinkle[i]])
		if GPIO.input(button_sw[1]) == GPIO.LOW:
			stop_song()
			foxrain()
			break
		if GPIO.input(button_sw[2]) == GPIO.LOW:
			stop_song()
			jinglebell()
			break
		if GPIO.input(button_sw[3]) == GPIO.LOW:
			stop_song()
			program_down()

		if i==6 or i==13 or i==20 or i==27 or i==34 or i==41:
			time.sleep(1.0)
		else:
			time.sleep(0.5)
	pwm.stop()

def foxrain():
	print("재생 중인 곡 : 여우비")
	pwm.start(10.0)
	foxrain = [3,2,3,2,\
		3,5,3,\
		3,2,3,2,\
		3,5,3,\
		3,2,3,4,5,\
		3,2,3,4,5,\
		3,2,3,4,5,7,5]

	for i in range(0, len(foxrain)):
		pwm.ChangeFrequency(scale[foxrain[i]])
		if GPIO.input(button_sw[0]) == GPIO.LOW:
			stop_song()
			twinkle()
			break
		if GPIO.input(button_sw[2]) == GPIO.LOW:
			stop_song()
			jinglebell()
			break
		if GPIO.input(button_sw[3]) == GPIO.LOW:
			stop_song()
			program_down()

		if i==3 or i==10:
			time.sleep(0.4)
		elif i==6 or i==13 or i==18 or i==23:
			time.sleep(0.8)
		else:
			time.sleep(0.3)
	pwm.stop()

def jinglebell():
	print("재생 중인 곡 : Jinglebell")
	pwm.start(10.0)
	bell = [0,5,4,3,0,\
		0,5,4,3,1,\
		0,6,5,4,2,\
		7,7,6,4,5,3,\
		0,5,4,3,0,\
		0,5,4,3,1,\
		1,6,5,4,7,7,7,7,8,7,6,4,3,\
		5,5,5,5,5,5,5,7,3,4,5,\
		6,6,6,6,6,5,5,5,5,4,4,3,4,7,\
		5,5,5,5,5,5,5,7,3,4,5,\
		6,6,6,6,6,5,4,4,7,7,6,4,3]

	for i in range(0, len(bell)):
		pwm.ChangeFrequency(scale[bell[i]])
		if GPIO.input(button_sw[0]) == GPIO.LOW:
			stop_song()
			twinkle()
			break
		if GPIO.input(button_sw[1]) == GPIO.LOW:
			stop_song()
			foxrain()
			break
		if GPIO.input(button_sw[3]) == GPIO.LOW:
			stop_song()
			program_down()

		if i==4 or i==9 or i==14 or i==20 or i==25 or i==30 or i==43 or i==54 or i==68 or i==79:
			time.sleep(1.0)
		else:
			time.sleep(0.5)
	pwm.stop()

def stop_song():
	pwm.stop()

def program_down():
	print("프로그램을 종료합니다.")
	exit(0)

try:
	print("SW1 : Twinkle\nSW2 : 여우비\nSW3 : Jinglebell\nSW4 : Exit")
	while True:
		if GPIO.input(button_sw[0]) == GPIO.LOW:
			twinkle()
		if GPIO.input(button_sw[1]) == GPIO.LOW:
			foxrain()
		if GPIO.input(button_sw[2]) == GPIO.LOW:
			jinglebell()
		if GPIO.input(button_sw[3]) == GPIO.LOW:
			program_down()

except KeyboardInterrupt:
	pass

GPIO.cleanup()
