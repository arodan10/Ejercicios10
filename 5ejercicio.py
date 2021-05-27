def valor():
  #definir Variables
  total=0
  #Datos de Endrada
  print("Categorías   1  ;  2  ;  3")
  categoría=float(input("Ingrese la categoría de su vehículo:"))
  #Proceso
  if categoría==1:
    total="paga el 10% del valor del vehículo"
  elif categoría==2:
   total="paga el 7% del valor del vehículo"    
  elif categoría==3:
   total="paga el 5% del valor del vehículo"  
  else:
   total="ERROR intentelo nuevamente"
 #Datos de salida
  print("Usted", total )

valor()