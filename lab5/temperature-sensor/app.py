from counterfit_connection import CounterFitConnection
import time
import json
import paho.mqtt.client as mqtt

from counterfit_shims_seeed_python_dht import DHT
CounterFitConnection.init('127.0.0.1', 5000)

sensor = DHT("11", 46)

id = 'c1967ba8-7aba-41c8-9bd0-6f06a001b33e'
client_name = id + 'temperature_sensor_client'
client_telemetry_topic = id + '/telemetry'

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_name)
mqtt_client.connect('test.mosquitto.org')
mqtt_client.loop_start()


while True:
   _, temp = sensor.read()
   telemetry = json.dumps({'temperature' : temp})
   print("Sending telemetry:", telemetry)
   mqtt_client.publish(client_telemetry_topic, telemetry)
   time.sleep(120)