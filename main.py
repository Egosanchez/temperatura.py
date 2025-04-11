import time

temperaturas = []

# Recolectar temperaturas durante 7 días
for dia in range(1, 8):
    temperatura = float(input(f"Por favor ingrese la temperatura del día {dia}: "))
    temperaturas.append(temperatura)

# Procesar resultados al final
promedio = sum(temperaturas) / len(temperaturas)
maximo = max(temperaturas)
minimo = min(temperaturas)

print("\nCargando...")
time.sleep(2)

print("\n📋 Estas han sido las temperaturas que se han registrado esta semana:")
for i, temperatura in enumerate(temperaturas, start=1):
    print(f"Día {i}: {temperatura}°C")

print("\n Resultados finales:")
time.sleep(1)
print(f" El promedio de temperatura de esta semana ha sido de: {promedio}°C")
time.sleep(1)
print(f" La temperatura más alta registrada fue de: {maximo}°C")
time.sleep(1)
print(f" La temperatura más baja registrada fue de: {minimo}°C")

# Verificar si alguna temperatura superó los 40°C
print("\n Revisión de alertas de calor extremo:")
alerta = False
for i, temperatura in enumerate(temperaturas, start=1):
    if temperatura > 40:
        print(f" ¡Alerta! El día {i} tuvo una temperatura de {temperatura}°C (mayor a 40°C).")
        alerta = True

if not alerta:
    print(" Ningún día superó los 40°C. No se detectaron alertas de calor extremo.")