import RPi.GPIO as GPIO
import random
import time

led = [4, 5, 6]
sw = [23, 24, 25, 22]
buzzer = 18

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)
GPIO.setup(sw, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

GPIO.output(led, GPIO.LOW)

def bgm():
	pwm = GPIO.PWM(buzzer, 1.0)
	scale = [261.63, 293.66, 329.63, 349.23, 392, 440, 493.89, 523.25, 622.25]

	pwm.start(10.0)
	song = [3,2,3,2,3,5,3,3,2,3,2,3,5,3,3,2,3,4,5,3,2,3,4,5,3,2,3,4,5,7,5]

	for i in range(0, len(foxrain)):
		pwm.ChangeFrequency(scale[song[i]])
		if i==3 or i==10:
			time.sleep(0.4)
		elif i==6 or i==13 or i==18 or i==23:
			time.sleep(0.8)
		else:
			time.sleep(0.3)

	pwm.stop()

randColor = [led[0], led[1], led[2]]

cnt = 0

try:
	print("순발력 게임\n게임을 시작하려면 SW1을 눌러주세요")
	while 1:
		if GPIO.input(sw[3]) == GPIO.LOW:
			for j in range(3, 0, -1):
				print(j)
				time.sleep(1)
			print("Start!!")
			time.sleep(0.5)
			for i in range(10):
				color = randColor[random.randint(0,2)]
				duration = random.uniform(0.5, 1.0)

				judgement1 = 0	#올바르게 눌렀는가(맞으면 0, 틀리면 1)
				judgement2 = 0	#제 시간에 눌렀는가(맞으면 1, 틀리면 0)

				GPIO.output(color, GPIO.HIGH)

				start = time.time()
				while 1:
					if GPIO.input(sw[0]) == GPIO.LOW:
						judgement2 = 1
						if color != led[0]:
							judgement1 = 1

					if GPIO.input(sw[1]) == GPIO.LOW:
						judgement2 = 1
						if color != led[1]:
							judgement1 = 1

					if GPIO.input(sw[2]) == GPIO.LOW:
						judgement2 = 1
						if color != led[2]:
							judgement1 = 1

					current = time.time()
					if current - start >= duration:
						break

				if judgement1 == 1:
					print("bad")
				elif judgement2 == 0:
					print("miss")
				else:
					cnt += 1
					print("perfect")

				GPIO.output(color, GPIO.LOW)
				time.sleep(0.5)

			print("총 점수는", cnt, "점 입니다.")
			if cnt >= 7:
				bgm()
			break

except KeyboardInterrupt:
	pass

GPIO.cleanup()
