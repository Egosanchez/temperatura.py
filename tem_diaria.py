import time

temperaturas = []
        

for dia in range(1, 8):
    temperatura = float(input(f"Por favor ingrese la temperatura del día {dia}: "))
    temperaturas.append(temperatura)


promedio = sum(temperaturas)/len(temperaturas)
maximo = max(temperaturas)
minimo = min(temperaturas)
temp_promedio = 25

print ("\nCargando...")
time.sleep(2)

print("\nEstas han sido las temperaturas que se han registrado esta semana:")
for i, temperatura in enumerate(temperaturas, start=1):
    print(f"Día {i}: {temperatura}°C")


print ("El promedio de temperatura de esta semana ha sido de:", promedio, "°C")
time.sleep(1)
print ("La temperatura mas alta que se ha registrado en esta semana son:", maximo, "°C")
time.sleep(1)
print ("La temperatura mas baja que se ha registrado en esta semana son:", minimo, "°C")
time.sleep(1)


for i, temperatura in enumerate(temperaturas, start=1):
    if temperatura > 40:
        time.sleep(1)
        print(f"Alerta! AL temperatura del dia {i} ha superado los 40°C")

        for i, temperatura in enumerate(temperaturas, start=1):
            if temperatura < 0:
                time.sleep(1)
                print(f"Cuidado! La temperatura del dia {i} ha sido por debajo de 0°C")

                for i, temperatura in enumerate(temperaturas, start=1):
                    if temperatura > promedio:
                        time.sleep(1)
                        print(f"La temperatura del dia {i} ha sido mayor al promedio")
                                
        




    
    
           
    
