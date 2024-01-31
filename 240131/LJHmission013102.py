import RPi.GPIO as GPIO
import random
import time

led_r = 4
led_g = 5
led_b = 6

pattern = []

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_r, GPIO.OUT)
GPIO.setup(led_g, GPIO.OUT)
GPIO.setup(led_b, GPIO.OUT)

GPIO.output(led_r, GPIO.LOW)
GPIO.output(led_g, GPIO.LOW)
GPIO.output(led_b, GPIO.LOW)

def genPattern(num):
	return [random.choice([led_r, led_g, led_b]) for i in range(num)]

def LEDPatternOn(pattern, duration):
	for led in pattern:
		GPIO.output(led, True)
		time.sleep(duration)
		GPIO.output(led, False)
		time.sleep(duration)

def Correct():
	for i in range(3):
		GPIO.output(led_g, True)
		time.sleep(0.5)
		GPIO.output(led_g, False)
		time.sleep(0.5)

def inCorrect():
	for i in range(3):
		GPIO.output(led_r, True)
		time.sleep(0.5)
		GPIO.output(led_r, False)
		time.sleep(0.5)

print("안녕하세요 Raspberry Pi LED 패턴 암기 게임입니다.")
time.sleep(1)
print("패턴이 랜덤하게 생성 되어 LED가 점등됩니다.")
time.sleep(1)
print("패턴을 기억한 후 패턴이 끝나면 정답을 입력해주세요.")
time.sleep(1)
print("패턴의 개수를 입력해주세요.: ")
num_pattern = int(input())
print("간격을 입력해주세요.: ")
interval = float(input())
print("아무 키나 누르면 시작합니다.")
input()
print("패턴 생성 중...")

pattern = genPattern(num_pattern)

LEDPatternOn(pattern, interval)

print("정답을 차례대로 입력해주세요. Red = 4, Green = 5, Blue = 6")
player_pattern = [0 for i in range(num_pattern)]
for i in range(num_pattern):
	player_pattern[i] = int(input())

if pattern == player_pattern:
	print("정답입니다!!")
	Correct()
else:
	print("오답입니다!!")
	print("정답은 ", pattern, "입니다.")
	inCorrect()

GPIO.cleanup()

