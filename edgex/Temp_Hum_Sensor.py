import sys, time, requests, json
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 2

edgexip = "blueshift.xslab.co.kr"
edgexfort ="9797"

try:

    while True :

        rawHum, rawTemp = Adafruit_DHT.read_retry(sensor, pin)

        if rawHum is not None and rawTemp is not None :

            urlTemp = 'http://%s:%s/api/v1/resource/Temp_and_Humidity_sensor_cluster_01/temperature' % (edgexip, edgexfort)
            urlHum  = 'http://%s:%s/api/v1/resource/Temp_and_Humidity_sensor_cluster_01/humidity' % (edgexip, edgexfort)

            humval = str(rawHum)
            tempval = str(rawTemp)

            headers = {'content-type': 'application/json'}
            response = requests.post(urlTemp, data=json.dumps(int(rawTemp)), headers=headers,verify=False)
            response = requests.post(urlHum, data=json.dumps(int(rawHum)), headers=headers,verify=False)

            print("Temp: %s\N{DEGREE SIGN}C, humidity: %s%%" % (tempval, humval))

        else :
            print('Read error')
            time.sleep(100)
except KeyboardInterrupt:
    print("Terminated by Keyboard")

finally:
    print("End of Program")
