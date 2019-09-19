import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# joystick
GPIO.setup([2, 3, 4], GPIO.IN)
print("joystick2 "+str(GPIO.input(2)))
print("joystick3 "+str(GPIO.input(3)))
print("joystick4 "+str(GPIO.input(4)))

# button
GPIO.setup(24, GPIO.IN)
print("button "+str(GPIO.input(24)))

# switch
GPIO.setup(25, GPIO.IN)
print("switch "+str(GPIO.input(25)))
