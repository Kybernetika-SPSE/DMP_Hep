from time import sleep_ms
from machine import Pin, PWM, Timer

pulse_in = Pin(2, Pin.IN, Pin.PULL_DOWN)
speaker = Pin(6, Pin.OUT)
output = PWM(Pin(8, Pin.OUT))
output.freq(1000000)
count = 0
duty = 0
pulse_length = 2
timer = Timer()

def pulse_reset(useless_1):
    global count
    count = 0

def pulse_count(useless_2):
    pulse_in.irq(handler = None)
    global count
    count = count + 1
    #bacha jmenovatel je dan vzorokovaci frekvenci
    global duty
    duty = (count/1700)*55538
    #print("count="+str(count))

    speaker.value(1)
    sleep_ms(pulse_length)
    speaker.value(0)
    sleep_ms(pulse_length)

    pulse_in.irq(handler = pulse_count)

timer.init(period=500, mode=Timer.PERIODIC, callback=pulse_reset)
pulse_in.irq(trigger=Pin.IRQ_FALLING, handler=pulse_count)

while True:
    output.duty_u16(duty)