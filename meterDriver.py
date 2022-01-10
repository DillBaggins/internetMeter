#from ftp import speedTest
from rpi_hardware_pwm import HardwarePWM
import RPi.GPIO as GPIO
import time
import sys
import math


def init():
    ON_LED=3
    TESTING_LED=5
    #initialise LED pins
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ON_LED,GPIO.OUT)
    GPIO.setup(TESTING_LED,GPIO.OUT)
    GPIO.output(ON_LED,1)
    GPIO.output(TESTING_LED,0)
    #initialise PWM
    pwm=HardwarePWM(pwm_channel=0,hz=25)
    pwm.start(50)
    return pwm

def updateLoop(pwm):
    while(True):
        dt=round(abs(10*math.sin(0.1*time.time())))
        print(dt)
        pwm.change_duty_cycle(dt)
        #turn on testing LED
        #test speed
        #turn off testing LED
        #call update display
        time.sleep(0.01)
        pass
    
def updateDisplay():
    #update PWM duty cycle
    return

def main():
    p=init()
    try:
        updateLoop(p)
    except KeyboardInterrupt:
        print("interrupted")
        GPIO.cleanup()
        sys.exit(0)

if __name__ == "__main__":
    main()
