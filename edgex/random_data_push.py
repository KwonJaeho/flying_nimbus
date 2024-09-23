import time, sys, requests, json
#import board
#import adafruit_dht
import random

# 데이터 핀 3번을 사용면, GPIO2로 설정
#pin = board.D2
#dhtDevice = adafruit_dht.DHT11(pin)

# EdgeX server ip
edgexip = "edgex_ip"

while True:
    try:
        # 온도 및 습도 값을 읽어옴

        #온도
        #temperature_c = dhtDevice.temperature
        temperature_c = random.uniform(35, 40)
        temperature_f = temperature_c * (9 / 5) + 32
        
        #습도
        #humidity = dhtDevice.humidity
        humidity = random.uniform(20, 80)
        
        print(
                "온도: {:.1f} F / {:.1f} C    습도: {:.1f} % ".format(
                temperature_f, temperature_c, humidity
            )
        )

        if temperature_c is not None and humidity is not None :
            urlTemp = 'http://%s:59986/api/v3/resource/Temp_and_Humidity_sensor_cluster_01/temperature' % edgexip
            urlHum  = 'http://%s:59986/api/v3/resource/Temp_and_Humidity_sensor_cluster_01/humidity' % edgexip

            headers = {'content-type': 'application/json'}
            response = requests.post(urlTemp, data=json.dumps(int(temperature_c)), headers=headers,verify=False)
            response = requests.post(urlHum, data=json.dumps(int(humidity)), headers=headers,verify=False)




        else:
            print('Read error')
            time.sleep(100)


    except RuntimeError as error:
        # 오류 발생 시 계속 진행
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        # 예기치 않은 오류 시 종료
        # dhtDevice.exit()
        print("Unexpected error:", error)
        sys.exit()
        raise error

    time.sleep(2.0)
