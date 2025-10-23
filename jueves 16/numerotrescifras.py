entrada= int(input("ingrese un numero mayor a 3 cifras:"))
if entrada>=100:
    print("numero correcto")
elif entrada<10:
    print("nuemro de 2 digitos")
elif entrada<=0:
    print("numero de 1 digito")
elif entrada>1000:
    print("numero de 4 digitos")
else :