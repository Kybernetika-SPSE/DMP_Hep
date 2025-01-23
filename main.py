from time import sleep_ms
from machine import Pin, PWM
from rp2 import StateMachine

#import threading

pulse_in = Pin(2, Pin.IN)
speaker = Pin(6, Pin.OUT)
test = Pin("LED",Pin.OUT)
output = PWM(Pin(8, Pin.OUT))
output.freq(10)
count = 0
pulse_length = 0.2

#def pulse_reset():
    #threading.Timer(10, pulse_reset).start()
    #count = 0

def pulse_count(zbytecne_1):
    pulse_in.irq(handler = None)
    global count
    count = count + 1
    print("count="+str(count))

    test.toggle()
    sleep_ms(500)
    test.toggle()
    sleep_ms(500)

    pulse_in.irq(handler = pulse_count)

    #speaker.value(1)
    #sleep_ms(pulse_length)
    #speaker.value(0)
    #sleep_ms(pulse_length)

pulse_in.irq(trigger=Pin.IRQ_RISING, handler=pulse_count)
while True:
    output.duty_u16(32700)