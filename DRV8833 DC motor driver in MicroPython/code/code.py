import time
import board
import digitalio

# Define motor control pins
MOTOR_FORWARD_PIN = board.D11
MOTOR_REVERSE_PIN = board.D10

# Set up the pins as digital outputs
motor_forward = digitalio.DigitalInOut(MOTOR_FORWARD_PIN)
motor_forward.direction = digitalio.Direction.OUTPUT

motor_reverse = digitalio.DigitalInOut(MOTOR_REVERSE_PIN)
motor_reverse.direction = digitalio.Direction.OUTPUT

while True:
    # Drive motor forward
    motor_forward.value = True
    motor_reverse.value = False
    print("Motor: FORWARD")
    time.sleep(1.0)

    # Stop motor
    motor_forward.value = False
    motor_reverse.value = False
    print("Motor: STOP")
    time.sleep(1.0)

    # Drive motor backward
    motor_forward.value = False
    motor_reverse.value = True
    print("Motor: REVERSE")
    time.sleep(1.0)

    # Stop motor again
    motor_forward.value = False
    motor_reverse.value = False
    print("Motor: STOP")
    time.sleep(1.0)