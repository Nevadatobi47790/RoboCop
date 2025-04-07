#run on pi startup, include Wifi Setup and start main controll class
import os
import time
import RPi.GPIO as GPIO

#GPIO 2&3 setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(3, True)
time.sleep(0.25)
#ueberpruefung ob debug schalter on/off
if GPIO.input(2):
    GPIO.output(3, False)
    GPIO.cleanup()
    os.system('sudo systemctl start NetworkManager')
    time.sleep(2)
    os.system('sudo nmcli device wifi hotspot robocopWifi password Enes_ist_hot ifname wlan0')
    os.system('sudo python script.py')
    print('start')
else:
    GPIO.output(3, False)
    GPIO.cleanup()
    os.system('sudo apt update -y && sudo apt upgrade -y')
    os.system('cd home/Robocop/RoboCop/ && sudo git pull')
    print('not start')
