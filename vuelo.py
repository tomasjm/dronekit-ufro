import math
import time
from dronekit import VehicleMode, LocationGlobalRelative
from utils import obtenerDistanciaMetros

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
        if distanciaFaltante <= distanciaObjetivo*0.01:
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
