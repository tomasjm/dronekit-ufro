""" 
dronekit-sitl copter --home=-38.7460967,-72.6154299,0,180
mavproxy.py --master tcp:127.0.0.1:5760 --out udp:127.0.0.1:14550 --out udp:127.0.0.1:14551
mission planner en puerto udp:14550
dronekit en puerto udp:14551


https://github.com/ArduPilot/MAVProxy/issues/543

"""

#from pymavlink import mavutil

""" 
------------------------------
    IMPORTS E INICIALIZACION
------------------------------
"""
from dronekit import connect, VehicleMode
import mavutil
from time import sleep
from vuelo import despegarVehiculo, moverAlPunto, aterrizarVehiculo
from utils import agregarDistanciaMetros
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='udp:192.168.8.120:14550')
args = parser.parse_args()
print('Conectando al vehiculo en: %s' % args.connect)
vehicle = connect(args.connect, baud=57600, wait_ready=True)


def goto(dNorth, dEast, gotoFunction=vehicle.simple_goto):
    """
    Moves the vehicle to a position dNorth metres North and dEast metres East of the current position.
    The method takes a function pointer argument with a single `dronekit.lib.LocationGlobal` parameter for 
    the target position. This allows it to be called with different position-setting commands. 
    By default it uses the standard method: dronekit.lib.Vehicle.simple_goto().
    The method reports the distance to target every two seconds.
    """
    
    currentLocation = vehicle.location.global_relative_frame
    targetLocation = get_location_metres(currentLocation, dNorth, dEast)
    targetDistance = get_distance_metres(currentLocation, targetLocation)
    gotoFunction(targetLocation)
    
    #print "DEBUG: targetLocation: %s" % targetLocation
    #print "DEBUG: targetLocation: %s" % targetDistance

    while vehicle.mode.name=="GUIDED": #Stop action if we are no longer in guided mode.
        #print "DEBUG: mode: %s" % vehicle.mode.name
        remainingDistance=get_distance_metres(vehicle.location.global_relative_frame, targetLocation)
        print("Distance to target: ", remainingDistance)
        if remainingDistance<=targetDistance*0.01: #Just below target, in case of undershoot.
            print("Reached target")
            break;
        time.sleep(2)

""" 
------------------------------
        CODIGO PRINCIPAL
------------------------------
"""

print("Global Location: ", vehicle.location.global_frame)
despegarVehiculo(vehicle, 50)
goto()
# nuevoPunto = agregarDistanciaMetros(-38.7460967, -72.6154299, 20)
# #nuevoPuntoEste = agregarDistanciaMetros(-38.7460967, -72.6154299, 20, "ESTE")
# moverAlPunto(vehicle, nuevoPunto.lat, nuevoPunto.lon, 20, 20)
# sleep(3)
# # moverAlPunto(vehicle, -38.7460967, -72.6154299, 20, 20)
# # sleep(3)
# # moverAlPunto(vehicle, nuevoPuntoEste.lat, nuevoPuntoEste.lon, 20, 20)
# aterrizarVehiculo(vehicle)
# print("Cerrando inicialización de vehiculo.")
# vehicle.close()
# print("Completado")
