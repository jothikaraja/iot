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




threshold=500

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
while True:
    sensor_value=get_sensor_value_from_pin("A0")
    if sensor_value < threshold:
        print("dark")
        response = mybolt.digitalWrite('0', 'HIGH')
        print (response)
    else:
        print("light")
        response = mybolt.digitalWrite('0', 'LOW')
        print(response)
    time.sleep(10)



    







