from flask import Flask, render_template
import RPi.GPIO as GPIO

sw_pin = [14, 15, 18]
GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

GPIO.setup(sw_pin[0], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(sw_pin[1], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(sw_pin[2], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

sw_state = [0, 0, 0]

@app.route('/')
def home():
  for ii in range(3):
    sw_state[ii] = GPIO.input(sw_pin[ii])

  return render_template('buttonState.html', sw_state = sw_state)

if __name__ == "__main__":
  app.run(host = "192.168.0.143", port = "8080")
