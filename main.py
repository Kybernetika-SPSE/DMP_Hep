from time import sleep_ms
from machine import Pin, PWM, Timer

pulse_in = Pin(2, Pin.IN, Pin.PULL_DOWN)
speaker = Pin(6, Pin.OUT)
output = PWM(Pin(8, Pin.OUT))
output.freq(10)
count = 0
pulse_length = 5
timer = Timer()

def pulse_reset(useless_1):
    global count
    count = 0

def pulse_count(useless_2):
    pulse_in.irq(handler = None)
    global count
    count = count + 1
    print("count="+str(count))

    speaker.value(1)
    sleep_ms(pulse_length)
    speaker.value(0)
    sleep_ms(pulse_length)

    pulse_in.irq(handler = pulse_count)

timer.init(period=2000, mode=Timer.PERIODIC, callback=pulse_reset)
pulse_in.irq(trigger=Pin.IRQ_RISING, handler=pulse_count)
while True:
    output.duty_u16(1456)