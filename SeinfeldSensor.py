import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            time.sleep(0.5)
            print("Motion Detected...")
            os.system("aplay -D bluealsa:HCI=hci0,DEV=00:21:3C:79:02:5C,PROFILE=a2dp /home/pi/Music/SeinfeldTheme.wav")
            time.sleep(2) #to avoid multiple detection
        time.sleep(.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()
