import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D9, echo_pin=board.D10)

while True:
    try:
        print("distance is {} cm \n".format(sonar.distance))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.5)