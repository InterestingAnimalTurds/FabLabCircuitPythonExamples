import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize the keyboard device
keyboard = Keyboard(usb_hid.devices)

# Define button pins (change if needed)
button1 = digitalio.DigitalInOut(board.D10)
button2 = digitalio.DigitalInOut(board.D11)
button3 = digitalio.DigitalInOut(board.D12)

# Configure pins as inputs with pullups
for btn in (button1, button2, button3):
    btn.switch_to_input(pull=digitalio.Pull.UP)

# Store last states
last_button1 = True
last_button2 = True
last_button3 = True

while True:
    val1 = button1.value
    val2 = button2.value
    val3 = button3.value

    # Button pressed → send text
    if val1 != last_button1 and not val1:
        # Type “omg” and press Enter
        for c in "omg":
            keyboard.send(getattr(Keycode, c.upper()))
        keyboard.send(Keycode.ENTER)
        time.sleep(0.1)

    if val2 != last_button2 and not val2:
        for c in "wtf":
            keyboard.send(getattr(Keycode, c.upper()))
        keyboard.send(Keycode.ENTER)
        time.sleep(0.1)

    if val3 != last_button3 and not val3:
        for c in "lol":
            keyboard.send(getattr(Keycode, c.upper()))
        keyboard.send(Keycode.ENTER)
        time.sleep(0.1)

    # Update last states
    last_button1 = val1
    last_button2 = val2
    last_button3 = val3

    time.sleep(0.01)