import time
import board
import busio
import digitalio
import adafruit_mpr121

# onboard LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# I2C bus + MPR121 setup
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

# record last touch states
last_touched = [False] * 12

while True:
    for i in range(12):
        touched = mpr121[i].value

        # just touched
        if touched and not last_touched[i]:
            print("touch", i)
            if i == 0:
                led.value = True
            elif i == 1:
                pass  # another action here if needed

        # just released
        if not touched and last_touched[i]:
            print("release", i)
            led.value = False

        last_touched[i] = touched

    time.sleep(0.05)