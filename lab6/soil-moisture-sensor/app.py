from counterfit_connection import CounterFitConnection
import time
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay
import paho.mqtt.client as mqtt
import json
CounterFitConnection.init('127.0.0.1', 5000)

adc = ADC()
relay = GroveRelay(47)

id = '8e647539-debc-4bcf-9682-4b7ddbe2950d'
client_name = id + 'soil_moisture_sensor_client'
client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'

mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_name)
mqtt_client.connect('test.mosquitto.org')
mqtt_client.loop_start()
print("MQTT connected!")

def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    if payload['relay_on']:
        relay.on()
    else:
        relay.off()
        
mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command


while True:
    soil_moisture = adc.read(46)
    telemetry = json.dumps({'soil_moisture': soil_moisture})
    print("Sending telemetry:", telemetry)
    mqtt_client.publish(client_telemetry_topic, telemetry)
    time.sleep(10)