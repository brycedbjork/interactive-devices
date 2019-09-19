import RPi.GPIO as GPIO
import time

genre = 0
volume = 0
# 0 = pop, 1 = rock, 2 = electronic
genreString = ["pop", "rock", "electronic"]

GPIO.setmode(GPIO.BCM)

while True:

    # joystick
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

    # button
    GPIO.setup(24, GPIO.IN)
    button = GPIO.input(24)

    # switch
    GPIO.setup(25, GPIO.IN)
    switch = GPIO.input(25)

    if joystickUp:
        if volume < 10:
            volume = volume + 1
        print("volume: "+str(volume))
        time.sleep(1)

    if joystickLeft:
        if volume > 0:
            volume = volume - 1
        print("volume: "+str(volume))
        time.sleep(1)

    if joystickButton:
        genre = (genre + 1) % 3
        print("genre: "+genreString[genre])
        time.sleep(1)

    if button:
        if switch:
            print("play "+genreString[genre]+" @ volume:"+str(volume))
        else:
            print("yell!")
        time.sleep(1)
