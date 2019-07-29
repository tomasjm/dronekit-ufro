import math

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
