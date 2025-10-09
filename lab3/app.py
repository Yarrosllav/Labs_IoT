import time
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed

CounterFitConnection.init('127.0.0.1', 5000)

light_sensor = GroveLightSensor(46)
led = GroveLed(47)

while True:
    light = light_sensor.light
    print('Light level:', light)
    if light < 460:
        led.on()
    else:
        led.off()
    time.sleep(1)

