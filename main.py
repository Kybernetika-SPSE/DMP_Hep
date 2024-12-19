import time
from machine import Pin

x = 0
def pulse_count(x):
    x = x + 1

pulse_in = Pin(2, Pin.IN)
pulse_in.irq(trigger=Pin.IRQ_RISING, handler=pulse_count(x))

while True:
    