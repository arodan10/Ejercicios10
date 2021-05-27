def salario():
  #Definir variables y otros
  
  #Datos de entrada
  e1=int(input("Ingrese su salario inicial:"))
  #proceso
  e2=e1*0.10+e1
  e3=e2*0.10+e2
  e4=e3*0.10+e3
  e5=e4*0.10+e4
  e6=e5*0.10+e5
  #Datos de salida
  print("sueldo del segundo año es:" , e2)
  print("sueldo del tercer año es:" , e3)
  print("sueldo del cuarto año es:" , e4)
  print("sueldo del quinto año es:" , e5)
  print("sueldo del sexto año es:" , e6)
salario()