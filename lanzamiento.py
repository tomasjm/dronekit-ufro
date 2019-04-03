from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time

import argparse  
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='127.0.0.1:14550')
args = parser.parse_args()

print 'Conectando al vehiculo en: %s' % args.connect
vehicle = connect(args.connect, baud=57600, wait_ready=True)

def takeOff(aTargetAltitude):
  print "Chequeando pre-arm"
  while not vehicle.is_armable:
    print " Esperando inicialización del vehiculo..."
    time.sleep(1)
        
  print "Armando motores"
  vehicle.mode    = VehicleMode("GUIDED")
  print "Vehiculo en modo GUIDED"
  vehicle.armed   = True


  while not vehicle.armed:
    print " Esperando preparación de vehiculo..."
    time.sleep(1)

  print "Despegando!"
  vehicle.simple_takeoff(aTargetAltitude) 

  while True:
    print " Altitud: ", vehicle.location.global_relative_frame.alt      
    if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
      print "Se ha llegado a la altitud objetivo"
      break
    time.sleep(1)

arm_and_takeoff(20)

print("Se ha completado el despegue")

time.sleep(10)

print("Vehiculo en modo LAND")
vehicle.mode = VehicleMode("LAND")
print("Aterrizando")

print "Cerrando inicialización de vehiculo."
vehicle.close()

print("Completado")
