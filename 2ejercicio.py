def tabla():
  #Datos de entrada
  numero=int(input("Digite un número entero:"))
  #Proceso
  for X in range(1, 11):
    print(f"{X} * {numero} = {X*numero}")
tabla()