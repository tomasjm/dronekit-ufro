import math
import time
from dronekit import Vehicle, VehicleMode, LocationGlobalRelative
from utils import obtenerDistanciaMetros, get_location_metres

"""
    Funcion para realizar el despegue del vehiculo, recibe dos parametros:
    El primer parametro es la clase Vehicle inicializada de la clase "vehicle" de dronekit.
    El segundo parametro es un numero correspondiente a la altitud deseada de despegue.
"""


def despegarVehiculo(vehicle, altitudObjetivo):
    print("Confirmando inicializacion...")
    while not vehicle.is_armable:
        print("Esperando inicialización del vehiculo...")
        time.sleep(1)

    print("Preparando motores")
    vehicle.mode = VehicleMode("GUIDED")
    print("Vehiculo en modo GUIDED")
    vehicle.armed = True
    while not vehicle.armed:
        print("Esperando preparación de vehiculo...")
        time.sleep(1)

    print("Despegando!")
    vehicle.simple_takeoff(altitudObjetivo)

    while True:
        print("Altitud: ", vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= altitudObjetivo*0.95:
            print("Se ha llegado a la altitud objetivo")
            break
        time.sleep(1)


"""
    Funcion para moverse hacia un punto, requiere de 5 parametros.
    - Clase instanciada de la clase Vehiculo de dronekit.
    - Latitud objetivo
    - Longitud objetivo
    - Altitud objetivo
    - Velocidad deseada
"""


def moverAlPunto(vehicle, lat, lon, alt, vel):
    puntoInicial = vehicle.location.global_relative_frame
    if vehicle.location.global_relative_frame.alt <= alt*0.8:
        print("Cuidado con la altura, no se encuentra dentro del rango")
    puntoObjetivo = LocationGlobalRelative(lat, lon, vel)
    vehicle.simple_goto(puntoObjetivo)
    while True:
        distanciaObjetivo = obtenerDistanciaMetros(
            puntoInicial, puntoObjetivo)
        distanciaFaltante = obtenerDistanciaMetros(
            vehicle.location.global_frame, puntoObjetivo)
        print("Distancia al punto: ", distanciaObjetivo)
        print("Distancia faltante: ", distanciaFaltante)
        print("-----------------------------")
        if distanciaFaltante <= distanciaObjetivo*0.035 or distanciaFaltante <= 1:
            print("Se ha llegado al punto")
            break
        time.sleep(2)


"""
    Funcion para aterrizar.
    Requiere de parametro la instancia inicializada de la clase Vehiculo

"""


def aterrizarVehiculo(vehicle):
    initAlt = vehicle.location.global_relative_frame.alt
    print("Preparando el aterrizaje del vehiculo...")
    while not vehicle.mode == VehicleMode("LAND"):
        vehicle.mode = VehicleMode("LAND")
        time.sleep(1)
    print("Comenzando el aterrizaje!")
    while not vehicle.location.global_relative_frame.alt <= initAlt*0.035:
        print("Altura actual: ", vehicle.location.global_relative_frame.alt)
        time.sleep(1)
    print("Aterrizaje completado!")


def goto(vehicle, dNorth, dEast):
    """
    Moves the vehicle to a position dNorth metres North and dEast metres East of the current position.
    The method takes a function pointer argument with a single `dronekit.lib.LocationGlobal` parameter for 
    the target position. This allows it to be called with different position-setting commands. 
    By default it uses the standard method: dronekit.lib.Vehicle.simple_goto().
    The method reports the distance to target every two seconds.
    """

    currentLocation = vehicle.location.global_relative_frame
    targetLocation = get_location_metres(currentLocation, dNorth, dEast)
    targetDistance = obtenerDistanciaMetros(currentLocation, targetLocation)
    vehicle.simple_goto(targetLocation)

    # print "DEBUG: targetLocation: %s" % targetLocation
    # print "DEBUG: targetLocation: %s" % targetDistance

    # Stop action if we are no longer in guided mode.
    while vehicle.mode.name == "GUIDED":
        # print "DEBUG: mode: %s" % vehicle.mode.name
        remainingDistance = obtenerDistanciaMetros(
            vehicle.location.global_relative_frame, targetLocation)
        print("Distance to target: ", remainingDistance)
        # Just below target, in case of undershoot.
        if remainingDistance <= targetDistance*0.035 or remainingDistance <= 0.85:
            print("Reached target")
            break
        time.sleep(2)
