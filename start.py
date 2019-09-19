import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# joystick
GPIO.setup([2, 3, 4], GPIO.IN)

# button
GPIO.setup(24, GPIO.IN)
print(GPIO.input(24))

# switch
GPIO.setup(25, GPIO.IN)
