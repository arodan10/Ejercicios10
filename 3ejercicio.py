def edadpromedio():
  print("Salon A:")
  acumuladorA = int(0)
  for x in range(1,6):
    edad=int(input("Favor de ingresar la edad:" ));
    acumuladorA = acumuladorA + edad;
  print("el promedio de edad de todo el salon es de:", str(acumuladorA/5));
  print("---------------------------------")
  print("Salon B:")
  acumuladorB = int(0)
  for x in range(1,11):
    edad=int(input("Favor de ingresar la edad:" ));
    acumuladorB = acumuladorB + edad;
  print("el promedio de edad de todo el salon es de:", str(acumuladorB/10));
  print("el promedio general del la escuela es:",str((acumuladorA+acumuladorB)/15));
edadpromedio()