  #main controll class
import time
import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BCM)

class robo:
    def __init__(self, BEINVR, BEINHR, BEINHL, BEINVL):
        self.BeinVR = BEINVR
        self.BeinHR = BEINHR
        self.BeinHL = BEINHL
        self.BeinVL = BEINVL


class bein:
    def __init__(self, GELKO, GELHU, GELKN, GELFU):
        self.GelKo = GELKO
        self.GelHu = GELHU
        self.GelKn = GELKN
        self.GelFu = GELFU

    #x - Rechts Links koordinate, Positiv ist immer weg vom Koerper
    #y - Vorne Hinten koordinate, Positiv ist immmer weg vom Koerper
    #z - Oben unten Koordinate, Positiv ist immmer nach unten
    #d - Winkel des fusses auf dem Boden
    #Alle Variablen in Bruchteilen einer Bein-teil-laenge (~63mm)
    #Berechnung Check ich selber nicht
    def PosToRad(self, x, y, z, d):
        Koerper = math.tan(x / y)
        a = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        Ah = math.sqrt(math.pow(z-math.sin(d), 2) + math.pow(a-math.cos(d), 2))
        Alpha = math.acos(0.5 * Ah)
        Delta = math.tan((z-math.sin(d))/(a-math.cos(d)))
        Huefte = Alpha + Delta
        Knie = math.pi - 2 * Alpha
        Epsylon = math.tan(z/a)
        En = math.pi / 2 - Delta + Epsylon
        be = math.sqrt(pow(a, 2) + pow(z, 2))
        be1 = math.cos(Delta-Epsylon) * Ah
        Oh = math.asin(be - be1)
        Fuss = En + Alpha + Oh
        print([Koerper, Huefte, Knie, Fuss])
        return [Koerper, Huefte, Knie, Fuss]


class gelenk:
    def __init__(self, PINNUM, DEFAULT):
        self.PinNum = PINNUM
        self.Default = DEFAULT
        #initiiert den Servo
        GPIO.setup(self.PinNum, GPIO.OUT)
        self.Pin = GPIO.PWM(self.PinNum, 50)
        self.Pin.start(self.RadToPWM(self.Default))


    #Uebersetzt einen gegebenen Winkel von xPi zu einer PWM frequenz
    def RadToPWM(self, rad):
        if rad >= 0 and rad <= 1:
            return rad*10 + 2.5
        else:
            return self.Default*10 + 2.5

    def set(self, rad):
        self.Pin.ChangeDutyCycle(self.RadToPWM(rad))




#Körper Hüfte Knie Fuß
#GPIOpins = [2, 3, 17, 4, 14, 15, 18, 23, 12, 16, 20, 21, 6, 13, 19, 26]

default = 0.5
#KO = Koerper   HU = Huefte   KN = Knie   FU = Fuss   GEL = Gelenk

#BeinVR
GELKO = gelenk(2, default)
GELHU = gelenk(3, default)
GELKN = gelenk(17, default)
GELFU = gelenk(4, default)

BeinVR = bein(GELKO, GELHU, GELKN, GELFU)

#BeinHR
GELKO = gelenk(14, default)
GELHU = gelenk(15, default)
GELKN = gelenk(18, default)
GELFU = gelenk(23, default)

BeinHR = bein(GELKO, GELHU, GELKN, GELFU)

#BeinHL
GELKO = gelenk(12, default)
GELHU = gelenk(16, default)
GELKN = gelenk(20, default)
GELFU = gelenk(21, default)

BeinHL = bein(GELKO, GELHU, GELKN, GELFU)

#BeinVL
GELKO = gelenk(6, default)
GELHU = gelenk(13, default)
GELKN = gelenk(19, default)
GELFU = gelenk(26, default)

BeinVL = bein(GELKO, GELHU, GELKN, GELFU)

Guenther_in = robo(BeinVR, BeinHR, BeinHL, BeinVL)


v = 0.25
va = 0.75

while True:
    for i in range(4):
        Guenther_in.BeinVR.GelKo.set(v)
        Guenther_in.BeinHR.GelKo.set(va)
        Guenther_in.BeinHL.GelKo.set(v)
        Guenther_in.BeinVL.GelKo.set(va)
        time.sleep(1)
        if i == 0 or i == 2:
            va = 0.5
            v = 0.5
        elif i == 1:
            va = 0.25
            v = 0.75
        elif i == 3:
            va = 0.75
            v = 0.25

#pins = []
#posPins = []
#supposPins = []
#startVal = 7.5
#speed = 0.05

#def set(pin, pos):
#    posPins[pin] = pos
#    supposPins[pin] = pos
#    pins[pin].ChangeDutyCycle(pos)

#def move(pin, pos):
#    supposPins[pin] = pos
#    while True:
#        if posPins[pin] - supposPins[pin] > speed:
#            set(pin, posPins[pin] + speed)
#            time.sleep(0.01)
#        elif supposPins[pin] - posPins[pin] > speed:
#            set(pin, posPins[pin] - speed)
#            time.sleep(0.01)
#        else:
#            set(pin, supposPins[pin])
#            break

#GPIO.setmode(GPIO.BCM)
#for i in range(16):
#    GPIO.setup(GPIOpins[i], GPIO.OUT)
#    pins.append(GPIO.PWM(GPIOpins[i], 50))
#    posPins.append(startVal)
#    supposPins.append(startVal)
#    pins[i].start(startVal)

#for i in range(3):
#    pins[i*4].ChangeDutyCycle(7.5)
#    pins[i*4+1].ChangeDutyCycle(11)
#    pins[i*4+2].ChangeDutyCycle(7)
#    pins[i*4+3].ChangeDutyCycle(7)

#for i in range(11, 16):
#     pins[i].ChangeDutyCycle(7.5)

while True:
     time.sleep(100)
#    for i in range(16):
#        print("Servo " + str(i) + " auf klein")
#        pins[i].ChangeDutyCycle(6)
#        time.sleep(0.2)
#    time.sleep(1)
#    for i in range(16):
#        pins[i].ChangeDutyCycle(7.5)
#        time.sleep(0.2)
#    time.sleep(1)
#    for i in range(16):
#        print("Servo " + str(i) + " auf hoch")
#        pins[i].ChangeDutyCycle(9)
#        time.sleep(0.2)
#    time.sleep(1)

GPIO.cleanup()


