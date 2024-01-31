import RPi.GPIO as GPIO
import random
import time

led_pins = [4, 5, 6]

GPIO.setmode(GPIO.BCM)

for led_pin in led_pins:
	GPIO.setup(led_pin, GPIO.OUT)
for led_pin in led_pins:
	GPIO.output(led_pin, GPIO.LOW)

print("--------------------------------------------------------")
print("                  빛의 삼원색 게임\n")
print("  - 색을 확인하고 합쳐지면 어떤 색이 되는지 맞춰보자 -")
print("--------------------------------------------------------")
print("Red, Green, Blue 중 중복되지 않고 랜덤하게 2개의 색 출력")

selected_led1 = random.choice(led_pins)
selected_led2 = random.choice(led_pins)
while selected_led2 == selected_led1:
	selected_led2 = random.choice(led_pins)

while(1):
	GPIO.output(selected_led1, True)
	GPIO.output(selected_led2, True)

	time.sleep(1)

	GPIO.output(selected_led1, False)
	GPIO.output(selected_led2, False)

	print("--------------------------------------------------------")
	print("1. yellow\n2. magenta\n3. cyan")
	print("--------------------------------------------------------")
	print("정답은? ")


	answer = int(input())

	if answer == 1:
		if ((selected_led1 == 4) & (selected_led2 == 5)) | ((selected_led1 == 5) & (selected_led2 == 4)):
			print("정답입니다!!")
			for i in range(3):
				GPIO.output(led_pins[i], True)
				time.sleep(0.5)
			GPIO.output(led_pins, False)
			break
		else:
			print("오답입니다!!")
			for i in range(3):
				GPIO.output(led_pins[0], True)
				time.sleep(0.5)
				GPIO.output(led_pins[0], False)
				time.sleep(0.5)
	elif answer == 2:
		if ((selected_led1 == 4) & (selected_led2 == 6)) | ((selected_led1 == 6) & (selected_led2 == 4)):
			print("정답입니다!!")
			for i in range(3):
				GPIO.output(led_pins[i], True)
				time.sleep(0.5)
			GPIO.output(led_pins, False)
			break
		else:
			print("오답입니다!!")
			for i in range(3):
				GPIO.output(led_pins[0], True)
				time.sleep(0.5)
				GPIO.output(led_pins[0], False)
				time.sleep(0.5)
	elif answer == 3:
		if ((selected_led1 == 5) & (selected_led2 == 6)) | ((selected_led1 == 6) & (selected_led2 == 5)):
			print("정답입니다")
			for i in range(3):
				GPIO.output(led_pins[i], True)
				time.sleep(0.5)
			GPIO.output(led_pins, False)
			break
		else:
			print("오답입니다!!")
			for i in range(3):
				GPIO.output(led_pins[0], True)
				time.sleep(0.5)
				GPIO.output(led_pins[0], False)
				time.sleep(0.5)

GPIO.cleanup()
