from modules import system

import RPi.GPIO as GPIO
from termcolor import colored, cprint
import time

# Set up the GPIO pin
PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)


activate_fan = False
try:
    while True:
        temperature = system.get_temperature()

        if temperature <= 30:
            # Cool
            temp_color = "blue"
        elif temperature <= 50:
            # Warm
            temp_color = "yellow"
        elif temperature <= 70:
            # Hot
            temp_color = "red"
        else:
            # Very Hot
            temp_color = "magenta"

        print(colored("[!] Temperature is", "cyan"), colored(
            f"{temperature}°C", temp_color))

        if temperature > 50:
            if activate_fan:
                print(f"Fan run.")
            else:
                activate_fan = True
                GPIO.output(PIN, GPIO.HIGH)  # Activate the pin
                cprint(f"Pin {PIN} activated. Fan turned on.", "green")
        else:
            if activate_fan:
                activate_fan = False
                GPIO.output(PIN, GPIO.LOW)  # Deactivate the pin
                cprint(f"Pin {PIN} deactivated. Fan turned off.", "blue")
            else:
                print(f"Fan off.")
        time.sleep(10)  # Wait for 1 second before checking again
finally:
    GPIO.cleanup()  # Clean up all GPIO settings
