import math
from enum import Enum
from dronekit import VehicleMode, LocationGlobal, LocationGlobalRelative


class NuevoPunto:
    lat = 0
    lon = 0

    def __init__(self, nlat, nlon):
        self.lat = nlat
        self.lon = nlon


""" 
    Funcion para obtener distancia en metros entre dos puntos de geolocalizacion
    de latitud y longitud.
    Es una aproximación para cortas distancias.
    Requiere de dos parametros que son los 2 puntos a comparar.
    Estos son de la clase "vehicle" propiedad "location": global_relative_frame
"""


def obtenerDistanciaMetros(punto1, punto2):
    dlat = punto2.lat - punto1.lat
    dlong = punto2.lon - punto1.lon
    return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5


"""
    Funcion para agregar distancia en metros a un punto de geolocalizacion de latitud y longitud.
    Aproximado.
    Requiere de 3 parametros: latitud, longitud y la cantidad de metros.
"""


def agregarDistanciaMetros(alat, alon, metros):
    dlat = alat
    dlon = alon
    coeficiente = 0.0000089
    nDist = metros*coeficiente
    nlat = dlat - nDist
    nlon = dlon - nDist/math.acos(dlat*math.pi/180)
    nuevoPunto = NuevoPunto(nlat, nlon)
    return nuevoPunto


def get_location_metres(original_location, dNorth, dEast):
    """
    Returns a LocationGlobal object containing the latitude/longitude `dNorth` and `dEast` metres from the 
    specified `original_location`. The returned LocationGlobal has the same `alt` value
    as `original_location`.
    The function is useful when you want to move the vehicle around specifying locations relative to 
    the current vehicle position.
    The algorithm is relatively accurate over small distances (10m within 1km) except close to the poles.
    For more information see:
    http://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-a-latitude-longitude-by-some-amount-of-meters
    """
    earth_radius = 6378137.0  # Radius of "spherical" earth
    # Coordinate offsets in radians
    dLat = dNorth/earth_radius
    dLon = dEast/(earth_radius*math.cos(math.pi*original_location.lat/180))

    # New position in decimal degrees
    newlat = original_location.lat + (dLat * 180/math.pi)
    newlon = original_location.lon + (dLon * 180/math.pi)
    if type(original_location) is LocationGlobal:
        targetlocation = LocationGlobal(newlat, newlon, original_location.alt)
    elif type(original_location) is LocationGlobalRelative:
        targetlocation = LocationGlobalRelative(
            newlat, newlon, original_location.alt)
    else:
        raise Exception("Invalid Location object passed")

    return targetlocation
