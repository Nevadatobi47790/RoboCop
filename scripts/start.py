#run on pi startup, include Wifi Setup and start main controll class
import os
import time
import RPi.GPIO as GPIO

os.system('sudo systemctl start NetworkManager')
time.sleep(2)
os.system('sudo nmcli device wifi hotspot ssid robocopWifi password Enes_ist_hot ifname wlan0')

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(3, GPIO.OUT)
#GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#GPIO.output(3, False)
#time.sleep(0.25)
#if GPIO.input(2):
#    GPIO.output(3, True)
#    GPIO.cleanup()
#    print('start')
#else:
#    GPIO.output(3, True)
#    GPIO.cleanup()
#    print('not start')
