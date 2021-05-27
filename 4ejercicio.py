def cajaregistradora():
  #Definir variables y otros
  print("Ingrese las cantidades de las monedas y billetes:")
  #Datos de entrada
  e1=int(input("Ingrese la cantidad de monedas de 10 céntimos:"))
  e2=int(input("Ingrese la cantidad de monedas de 20 céntimos:"))
  e3=int(input("Ingrese la cantidad de monedas de 50 céntimos:"))
  e4=int(input("Ingrese la cantidad de monedas de 1 sol:"))
  e5=int(input("Ingrese la cantidad de monedas de 2 soles:"))
  e6=int(input("Ingrese la cantidad de monedas de 5 soles:"))
  e7=int(input("Ingrese la cantidad de billetes de 10 soles:"))
  e8=int(input("Ingrese la cantidad de billetes de 20 soles:"))
  e9=int(input("Ingrese la cantidad de billetes de 50 soles:"))
  e10=int(input("Ingrese la cantidad de billetes de 100 soles:"))
  e11=int(input("Ingrese la cantidad de billetes de 200 soles:"))
  #Proceso
  Resultados=(e1*0.10+e2*0.20+e3*0.50+e4*1+e5*2+e6*5+e7*10+e8*20+e9*50+e10*100+e11*200)
  #Datos de salida
  print("El total es:", Resultados)
cajaregistradora() 