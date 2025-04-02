# RoboCop
 Roboter P-Seminar Project
 
# 3D Modelle
 Onshape: https://cad.onshape.com/documents/159247000d269ee7f0577bf6/w/6b491cff9ae05a1da4a0bc55/e/ab45725633aa7fd81a276f7c?renderMode=0&uiState=67ed80defe0feb51428fd5da
 1x Körper
 4x Huefte
 4x Oberschenkel
 4x Unterschenkel
 4x Fuß
 
# Material
 16x Servos: https://www.amazon.de/Miuzei-Hubschrauber-Helikopter-Fahrzeugmodelle-Steuerung/dp/B07KPS9845
 1x Raspberry Pi Zero (2) W
 1x SD Karte
 
# Software
 Add the following at the end of the file /home/<user>/.profile
 >>$ sudo python3 /path/to/start.py<<
 
 Enable Auto Login in raspi-config under 1/S5
 
 make sure the following python packages are installed:
  time
  RPi.GPIO
  os
  math
  
 Change the GPIOPin numbers in scripts.py and start.py according to your connections (a config file will follow)
