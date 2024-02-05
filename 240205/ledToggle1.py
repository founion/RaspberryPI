from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pins = [14, 15, 18]
GPIO.setup(pins, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def hello():
  return "LED 제어를 위해 주소창을 변경하세요"

@app.route('/red_on')
def red_on():
  GPIO.output(pins[0], GPIO.HIGH)
  return "red LED on"

@app.route('/green_on')
def green_on():
  GPIO.output(pins[1], GPIO.HIGH)
  return "green LED on"

@app.route('/blue_on')
def blue_on():
  GPIO.output(pins[2], GPIO.HIGH)
  return "blue LED on"

@app.route('/off')
def off():
  GPIO.output(pins, GPIO.LOW)
  return "all LED off"

@app.route('/clean_up')
def clean_up():
  GPIO.cleanup()
  return "clean up"

if __name__ == "__main__":
  app.run(host = "192.168.0.143", port = "8080")
