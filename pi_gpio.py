#Traslation layer between pigpio and Rpi.GPIO to be imported as GPIO
#and maintain compatibility
from pigpio import *

class GPIO:
    def __call__(self):
        self.BCM = "BCM"
        self.LOW = 0
        self.HIGH = 1
    #GPIO no aplicable a pigpio pero se agregan para mantener compatibilidad

    def setmode(self, mode):
        self.raspi = pi()
        return self.BCM

    def setwarnings(self, bool):
        return bool
    
    def setup(self, pin, mode):
        self.raspi.set_mode(pin, mode)
    
    def output(self, pin, state):
        self.raspi.write(pin, state)
    
    class PWM:
        def __init__(self, pin, init_freq, freq_range = 10000):
            self.pin = pin
            self.pi = pi()
            self.pi.set_PWM_range(self.pin, freq_range)
            self.pi.set_PWM_frequency(self.pin, init_freq)
        
        def ChangeFrequency(self, freq):
            self.pi.set_PWM_frequency(self.pin, freq)
        
        def ChangeDutyCicle(self, duty_cicle):
            self.pi.set_PWM_dutycycle(self.pin, duty_cicle)
            
            
        def start(self, dc):
            self.pi.set_PWM_dutycycle(self.pin, dc)
        
        def stop(self):
            self.pi.set_PWM_dutycycle(self.pin, 0)
