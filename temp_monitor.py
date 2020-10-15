from boltiot import Bolt
import requests                 # for making HTTP requests
import json                     # library for handling JSON data
import time
import conf


def get_sensor_value_from_pin(pin):
    """Returns the sensor value. Returns -999 if request fails"""
   
    mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
    try:
        response = mybolt.analogRead(pin)
        data = json.loads(response)
        if data["success"] != 1:
            print("Request not successfull")
            print("This is the response->", data)
            return -999
        sensor_value = int(data["value"])
        return sensor_value
    except Exception as e:
        print("Something went wrong when returning the sensor value")
        print(e)
        return -999




mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
while True:
    sensor_value=get_sensor_value_from_pin("A0")
    Temperature=(100*sensor_value)/1024
    threshold=800
    print(Temperature)
    if Temperature > threshold:
        response = mybolt.digitalWrite('1', 'HIGH')
        print (response)
        c=input('notice the temperature')
        response = mybolt.digitalWrite('1', 'LOW')
        print(response)
    time.sleep(10)
