from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)                     # Pin de salida para el LED
boton = Pin(16, Pin.IN, Pin.PULL_DOWN)     # Pin de entrada con pull-down interno

while True:
    if boton.value() == 1:  # Si el botón está presionado
        led.on()        # Enciende el LED
        sleep(0.1)
    else:
        led.off()       # Apaga el LED