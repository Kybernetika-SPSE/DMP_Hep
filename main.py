from time import sleep_ms
from machine import Pin, PWM

pulse_in = Pin(2, Pin.IN)
speaker = Pin(6, Pin.OUT)
output = PWM(Pin(8, Pin.OUT))
output.freq()
count = 0
pulse_length = 0.2

def pulse_count():
    global count
    count = count + 1

    speaker.value(1)
    sleep_ms(pulse_length)
    speaker.value(0)

pulse_in.irq(trigger=Pin.IRQ_FALLING, handler=pulse_count())

while True:
    