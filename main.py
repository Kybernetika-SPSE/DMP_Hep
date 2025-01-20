from time import sleep_ms
from machine import Pin, PWM

count = 0
def pulse_count():
    global count
    count = count + 1


pulse_in = Pin(2, Pin.IN)
speaker = PWM(Pin(6, Pin.OUT))
pulse_in.irq(trigger=Pin.IRQ_RISING, handler=pulse_count(x))

while True:
    