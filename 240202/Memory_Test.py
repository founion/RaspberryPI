import RPi.GPIO as GPIO
import time
import random

led = [4, 5, 6]
sw = [22, 23, 24, 25]
buzzer_pin = 18

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT)
GPIO.setup(sw, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)

GPIO.output(led, GPIO.LOW)

buzzer = GPIO.PWM(buzzer_pin, 100)

def color_Hz(color):
	if color == 4:
		return 262
	elif color == 5:
		return 294
	elif color == 6:
		return 330

def play_sequence(sequence, duration):
	for color in sequence:
		GPIO.output(color, GPIO.HIGH)
		for i in range(4, 7, 1):
			if color == i:
				buzzer.ChangeFrequency(color_Hz(color))
		buzzer.start(10)
		time.sleep(duration)
		buzzer.stop()
		GPIO.output(color, GPIO.LOW)
		time.sleep(0.3)

def get_user_input():
	while 1:
		for i in range(3):
			if GPIO.input(sw[i]) == GPIO.LOW:
				return i+4
		if GPIO.input(sw[3]) == GPIO.LOW:
			print("게임 종료")
			return 1

try:
	print("기억력 게임")
	for i in range(3, 0, -1):
		print(i)
		time.sleep(1)
	sequence = []
	while 1:
		time.sleep(0.5)
		sequence.append(random.choice(led))
		play_sequence(sequence, 0.3)

		user_input = []
		for _ in range(len(sequence)):
			button_pressed = get_user_input()
			user_input.append(button_pressed)
			for i in range(4, 7, 1):
				if button_pressed == i:
					buzzer.ChangeFrequency(color_Hz(button_pressed))
			if button_pressed == 1:
				print("게임 종료! 점수 : ", (len(sequence) - 1) * 10)
				exit(0)
			buzzer.start(10)
			time.sleep(0.3)
			buzzer.stop()

		if sequence != user_input:
			print("Game Over! 점수 : ", (len(sequence) - 1) * 10)
			for i in range(3):
				GPIO.output(led[0], GPIO.HIGH)
				time.sleep(0.5)
				GPIO.output(led[0], GPIO.LOW)
				time.sleep(0.5)
			break

	time.sleep(1)

except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
