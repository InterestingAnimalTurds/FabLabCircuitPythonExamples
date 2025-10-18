from machine import Pin
import time

# Define pins
BUTTON_PIN = 0
LED_PIN = 13

# LED setup
led = Pin(LED_PIN, Pin.OUT)

# Button setup (pull-up enabled)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Shared state variable (will change inside interrupt)
state = 1

# Interrupt handler
def on_press(pin):
    global state
    state += 1
    if state > 3:
        state = 0

# Attach interrupt to button pin
# Trigger when button goes from HIGH → LOW (falling edge)
button.irq(trigger=Pin.IRQ_FALLING, handler=on_press)

# Blink function
def blink(delay_ms):
    led.value(1)
    time.sleep_ms(delay_ms)
    led.value(0)
    time.sleep_ms(delay_ms)

# Main loop
while True:
    if state == 1:
        blink(1000)
    elif state == 2:
        blink(500)
    elif state == 3:
        blink(100)
    else:
        led.value(0)
        time.sleep_ms(50)