"""
dronekit-sitl copter --home=-38.7460967,-72.6154299,0,180
mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14550 --out udp:127.0.0.1:14551
mission planner en puerto udp:14550
dronekit en puerto udp:14551


https://github.com/ArduPilot/MAVProxy/issues/543

"""

# from pymavlink import mavutil

"""
------------------------------
    IMPORTS E INICIALIZACION
------------------------------
"""
from dronekit import connect, VehicleMode
from time import sleep
from vuelo import despegarVehiculo, moverAlPunto, aterrizarVehiculo, goto
from utils import agregarDistanciaMetros
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='udp:192.168.8.120:14551')
args = parser.parse_args()
print('Conectando al vehiculo en: %s' % args.connect)
vehicle = connect(args.connect, baud=57600, wait_ready=True)


"""
------------------------------
        CODIGO PRINCIPAL
------------------------------
"""


def prueba_default():
    print("------COMENZANDO LA PRIMERA PRUEBA ------")
    despegarVehiculo(vehicle, 3)
    sleep(8)
    aterrizarVehiculo(vehicle)
    sleep(1)
    vehicle.close()


def prueba_movimiento():
    print("------COMENZANDO LA SEGUNDA PRUEBA ------")
    despegarVehiculo(vehicle, 5)
    goto(vehicle, 2.5, 2.5)
    sleep(3)
    goto(vehicle, 2.5, 2.5)
    sleep(3)
    aterrizarVehiculo(vehicle)
    sleep(1)
    vehicle.close()


def prueba_final():
    print("------COMENZANDO LA TERCERA PRUEBA ------")
    despegarVehiculo(vehicle, 30)
    goto(vehicle, 5, 0)
    sleep(1)
    goto(vehicle, -1.5, 3.5)
    sleep(1)
    goto(vehicle, -3.5, 1.5)
    sleep(1)
    goto(vehicle, -3.5, -1.5)
    sleep(1)
    goto(vehicle, -1.5, -3.5)
    sleep(1)
    goto(vehicle, 1.5, -3.5)
    sleep(1)
    goto(vehicle, 3.5, -1.5)
    sleep(1)
    goto(vehicle, 3.5, 1.5)
    sleep(1)
    goto(vehicle, 1.5, 3.5)
    sleep(1)
    goto(vehicle, -5, 0)
    sleep(1)
    aterrizarVehiculo(vehicle)
    vehicle.close()


prueba_movimiento()

