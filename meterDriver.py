from ftp import speedTest
from Speedtest_Python_API_Approach.hello_speedtest import ooklaInit, ooklaTest 
from rpi_hardware_pwm import HardwarePWM
import RPi.GPIO as GPIO
import time
import sys
import math

ON_LED=3
TESTING_LED=5
UPPER_PWM=6.2
LOWER_PWM=1.5
TEST_TYPE = 0 #0 for ftp, 1 for ookla speedtest

def init():
     
    #initialise LED pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ON_LED,GPIO.OUT)
    GPIO.setup(TESTING_LED,GPIO.OUT)
    GPIO.output(ON_LED,1)
    GPIO.output(TESTING_LED,0)
    #initialise PWM
    pwm=HardwarePWM(pwm_channel=0,hz=25)
    pwm.start(50)
    #initlialise OOKLA Speedtest
    if TEST_TYPE==1:
        ooklaInit()
    print("finished init")
    return pwm


def updateLoop(pwm):
    t=1.5
    dire=True
    while(True):
        #this linearly rotates the servo
        GPIO.output(TESTING_LED,1)
        if (TEST_TYPE==0):
            speed=speedTest()
        else:
            speed=ooklaTest()
        print(speed)
        GPIO.output(TESTING_LED,0)
        updateDisplay(pwm,speed)
        pass
    
def updateDisplay(pwm,speed):
    #map speed to pwm (1.5-6.2)
    dc=(speed/40)*(UPPER_PWM-LOWER_PWM)+LOWER_PWM
    #update PWM duty cycle
    pwm.change_duty_cycle(dc)
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
