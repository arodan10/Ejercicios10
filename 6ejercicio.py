def estCondicional01():
  #Definir variable
  montoP=0
  #Datos de entrada
  precioX=int(input("Ingrese el monto:"))
  #Proceso
  if precioX>=200:
    montoP=precioX-(precioX*0.15)
  elif precioX>=100 and precioX<=200:
    montoP=precioX-(precioX*0.12)         
  else:
    montoP=precioX-(precioX*0.10)
  #Datos de salida
  print("Total a pagar:",montoP,"soles" )
estCondicional01()