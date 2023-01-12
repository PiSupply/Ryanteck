#RTK.GPIO implementation of PWM courtesy of C0deGyver
from time import sleep
try:
        import GPIO as GPIO
except:
        import RTk.GPIO as GPIO

class PWM_Mod:
        """
                fake PWM output using sleep
                included a position calulator function
                   this function should work with *most* PWM servos by default; but check your spec sheet
        """

        def __init__(self, initPWMPIN, initFREQUENCY):
                self.PWMPIN = initPWMPIN
                self.FREQUENCY = initFREQUENCY
                self.MILS = 0.01

        def start(self, startDutyCycle):
                startDutyCycle = round(startDutyCycle)
                for x in range(startDutyCycle):
                        GPIO.output(self.PWMPIN, GPIO.HIGH)
                        sleep(self.milS)
                        GPIO.output(self.PWMPIN, GPIO.LOW)
                        sleep(self.milS)

        def servoCalc(self, location, FREQUENCY = 50, minPW = 1, maxPW = 2):
                period = (1 / frequency) * 1000
                if (location <= 180):
                        pulseWidth = (((maxPW - minPW) / 180) * location) + minPW
                else:
                        pulseWidth = (((maxPW - minPW) / 360) * location) + minPW
                dutyCycle = pulseWidth / period

                return dutyCycle
