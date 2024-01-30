import RPi.GPIO as GPIO
import time

led_pin = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 100)

try:
	while True:
		print("1. LED 켜기\n2. LED 끄기\n3. LED 3초간 점점 밝기\n4. LED 3초간 점점 어둡기\n5. LED 3초간 점점 밝다가 3초간 점점 어둡기\n6.원하는 초 입력\n다른 숫자를 입력하면 종료합니다.\n원하는 기능 : ")

		num = input()

		if num == '1':
			print("LED 켜기!!")
			GPIO.output(led_pin, True)
		elif num == '2':
			print("LED 끄기!!")
			GPIO.output(led_pin, False)
		elif num == '3':
			print("LED 3초간 점점 밝기!!")
			pwm_led.start(0)
			for duty_cycle in range(101):
				pwm_led.ChangeDutyCycle(duty_cycle)
				time.sleep(0.03)
			pwm_led.stop()
		elif num == '4':
			print("LED 3초간 점점 어둡기!!")
			pwm_led.start(100)
			for duty_cycle in range(100, -1, -1):
				pwm_led.ChangeDutyCycle(duty_cycle)
				time.sleep(0.03)
			pwm_led.stop()
		elif num == '5':
			print("LED 3초간 점점 밝다가 3초간 점점 어둡기!!")
			pwm_led.start(0)
			for duty_cycle in range(101):
				pwm_led.ChangeDutyCycle(duty_cycle)
				time.sleep(0.03)
			pwm_led.stop()
			pwm_led.start(100)
			for duty_cycle in range(100, -1, -1):
				pwm_led.ChangeDutyCycle(duty_cycle)
				time.sleep(0.03)
			pwm_led.stop()
		elif num == '6':
			want_time = float(input("원하는 시간을 입력하세요: "))
			print("총", want_time*2, "초 동안 점점 밝아지다가 어두워집니다!!")
			pwm_led.start(0)
			for duty_cycle in range(101):
				pwm_led.ChangeDutyCycle(duty_cycle)
				time.sleep(want_time/100.0)
			pwm_led.stop()
			pwm_led.start(100)
			for duty_cycle in range(100, -1, -1):
				pwm_led.ChangeDutyCycle(duty_cycle)
				time.sleep(want_time/100.0)
			pwm_led.stop()
		else:
			print("프로그램을 종료합니다!!")
			break

except KeyboardInterrupt:
	pass

GPIO.cleanup()
