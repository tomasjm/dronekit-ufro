import requests
from time import sleep
import gpiozero as gpio

node_ip = '192.168.8.150'


def Control_Box(node_ip, foco_state, camara_state):
    R1 = str(foco_state)
    R2 = '1'
    R3 = str(camara_state)
    R4 = '1'
    response = requests.get(
        str('http://'+node_ip+'/relay?R1='+R1+'&R2='+R2+'&R3='+R3+'&R4='+R4+'/'))
    print(response)
    sleep(1)
    response = request.get(str('http://192.168.8.120:3000/start_stream_drone'))
    print(response)
    sleep(1)
    response =request.get(str('http://192.168.8.120:3000/start_mission'))
    print(response)
    sleep(60)
    response = request.get(str('http://192.168.120:3000/start_stream_central'))
    print(response)


b = gpio.Button(6, pull_up=True)
Control_Box(node_ip, 1, 1)
while True:
        sleep(0.1)
        if b.is_pressed:
                print("PRESIONADO")
                Control_Box(node_ip, 0, 0)
                sleep(5)
                while True:
                        if b.is_pressed:
                                Control_Box(node_ip, 1, 1)
                                sleep(5)
                                break
        else:
                print("NO")

