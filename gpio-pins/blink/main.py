from machine import Pin
import time

led = Pin(5, Pin.OUT)
while True:
  led.value(1)    # Nivel alto (enciende LED)
  time.sleep(1)   # Espera 1 segundo
  led.value(0)    # Nivel bajo (apaga LED)
  time.sleep(1)   # Espera 1 segundo
