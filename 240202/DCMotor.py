from gpiozero import Motor
from time import sleep

motorR = Motor(forward = 12, backward = 13)

motorR.forward(speed = 0.7)
sleep(3)

motorR.backward(speed = 0.7)
sleep(3)

motorR.forward(speed = 0.7)
sleep(3)

motorR.backward(speed = 0.7)
sleep(3)

motorR.stop()
