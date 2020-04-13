import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.cleanup()

# read data using Pin Board pins 
instance = dht11.DHT11(pin=8)

while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)

    time.sleep(1)
