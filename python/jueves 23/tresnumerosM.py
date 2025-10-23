#Ingrese 3 numeros e identifique el mayor de estos
num1= int(input("ingrese un numero:"))
num2= int(input("ingrese un numero:"))
num3= int(input("ingrese un numero:"))
if num1> num2 and num3 :
  print("n1 es el numero mayor", num1 )
elif num2> num1 and num3:
  print("n2 es el numero mayor:", num2)
elif num3> num2 and num3:
  print("n3 es el numero mayor:", num3)
else : print("los numeros son iguales")