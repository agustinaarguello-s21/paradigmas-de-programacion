#Pedir 3 notas, calcular el promedio  mostrar los promocionados (>7), los regulares (>4) y los desaprobados 
nota1= float(input("nota 1="))
nota2= float(input("nota2 ="))
nota3= float(input("nota3="))
promedio= (nota1+nota2+nota3)/3
round(promedio,2)
print("su promedio es de:",promedio)
if promedio>=7: 
     print("promocionado")
elif promedio>=4: 
          print("regular")
else : promedio<4
print("desaprobado") 
 