""" 
dronekit-sitl copter --home=-38.7460967,-72.6154299,0,180
mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14550 --out udp:127.0.0.1:14551
mission planner en puerto udp:14550
dronekit en puerto udp:14551

"""

#from pymavlink import mavutil

""" 
------------------------------
    IMPORTS E INICIALIZACION
------------------------------
"""
from dronekit import connect
from vuelo import despegarVehiculo, moverAlPunto, aterrizarVehiculo
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='udp:127.0.0.1:14550')
args = parser.parse_args()
print('Conectando al vehiculo en: %s' % args.connect)
vehicle = connect(args.connect, baud=57600, wait_ready=True)


""" 
------------------------------
        CODIGO PRINCIPAL
------------------------------
"""
despegarVehiculo(vehicle, 20)
moverAlPunto(vehicle, -38.746759, -72.615816, 20, 20)
aterrizarVehiculo(vehicle)
print("Cerrando inicialización de vehiculo.")
vehicle.close()
print("Completado")
