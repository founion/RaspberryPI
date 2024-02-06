import RPi.GPIO as GPIO
import time

sw_pin = [22, 23, 24, 25]     # sw1은 22번, sw2는 23번, sw3은 24번, sw4는 25번에 연결
motor_pin = [16, 17, 18, 19]  # STEP_OUTA는 16번, OUTB는 17번, OUT2A는 18번, OUT2B는 19번에 연결

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(sw_pin, GPIO.IN)
GPIO.setup(motor_pin, GPIO.OUT)

GPIO.output(motor_pin, GPIO.LOW)

def degree45():
	print("45도 회전합니다!!")
	for i in range(64):
		for j in motor_pin:
			GPIO.output(j, GPIO.HIGH)
			time.sleep(0.003)
			GPIO.output(j, GPIO.LOW)

def degree90():
	print("90도 회전합니다!!")
	for i in range(128):
		for j in motor_pin:
			GPIO.output(j, GPIO.HIGH)
			time.sleep(0.003)
			GPIO.output(j, GPIO.LOW)

def degree180():
	print("180도 회전합니다!!")
	for i in range(257):
		for j in motor_pin:
			GPIO.output(j, GPIO.HIGH)
			time.sleep(0.003)
			GPIO.output(j, GPIO.LOW)

def program_down():
	print("프로그램을 종료합니다.")
	exit(0)

print("Step Motor Control Start!!")
print("SW1 : 45도\nSW2 : 90도\nSW3 : 180도\nSW4 : Exit")

try:
	while True:
		if GPIO.input(sw_pin[0]) == GPIO.LOW:
			degree45()
		elif GPIO.input(sw_pin[1]) == GPIO.LOW:
			degree90()
		elif GPIO.input(sw_pin[2]) == GPIO.LOW:
			degree180()
		elif GPIO.input(sw_pin[3]) == GPIO.LOW:
			program_down()

except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
