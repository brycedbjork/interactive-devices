import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# joystick
# 2 is joystick button: 0 when pressed, 1 when not
GPIO.setup([2, 3, 4], GPIO.IN)
if (GPIO.input(2)):
    joystickButton = 0
else:
    joystickButton = 1

if (GPIO.input(3)):
    joystickUp = 0
else:
    joystickUp = 1

if (GPIO.input(4)):
    joystickLeft = 0
else:
    joystickLeft = 1

print("joystick button "+str(joystickButton))
print("joystick up "+str(joystickUp))
print("joystick left "+str(joystickLeft))

# button
GPIO.setup(24, GPIO.IN)
button = GPIO.input(24)
print("button "+str(button))

# switch
GPIO.setup(25, GPIO.IN)
switch = GPIO.input(25)
print("switch "+str(switch))
