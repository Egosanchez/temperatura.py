import time
#Determinar si la temperatura ingresada por el ususario es Celsius, Fahrenheir o Kelvin y a cual la desea cambiar

temperatura = float(input("Ingrese una temperatura por favor:"))
escala = input("Es Celsius (C) o Fahrenheit (F) o Kelvin (K)?").lower()
cambio = input("A que escala lo deseas cambiar, Celsius , Fahrenheir o Kelvin ").lower()
#Funcion para pasar temperatura a la deseado por el usuario

print("Cargando...")
time.sleep(2)

if escala == "f":
    celsius = (temperatura - 32) * 5/9
    kelvin = (temperatura - 32) / 1.8 + 273.15
    if cambio == "c":
        print ("La temperatura es de", celsius, "grados Celsius")
    elif cambio == "k":
        print ("La temperatura es de", kelvin, "grados Kelvin")
    else:
        print ("Ya esta en esa escala")

if escala == "c":
    fahrenheit = (temperatura * 1.8) + 32
    kelvin = temperatura + 273.15
    if cambio == "f":
        print ("La temperatura es de", fahrenheit, "grados Fahrenheit")
    elif cambio == "k":
        print ("La temperatura es de", kelvin, "grados Kelvin")
    else:
        print ("Ya esta en esa escala")

if escala == "k":
    celsius = temperatura - 273.15
    fahrenheit = 1.8 * (temperatura - 273.15) + 32
    if cambio == "c":
        print ("La temperatura es de", celsius, "grados Celsius")
    elif cambio == "f":
        print ("La temperatura es de", fahrenheit, "grados Fahrenheit")
    else:
        print ("Ya esta en esa escala")
        






