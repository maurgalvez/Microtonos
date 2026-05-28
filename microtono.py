import winsound # Librería que permite activar sonidos
import time
print("=== Simulador de microtonos ===")
maximo_microtonos = 25
microtonos_libres = 25
microtonos_activos = 0
ejecutando = True

while ejecutando:
    print("\n=== Panel de microtonos ===")
    print("1.- Ver cuántos microtonos quedan libres")
    print("2.- Ver microtonos (Avtivación de sonido)")
    print("3.- Apagar microtonos")
    print("4.- Monitorear el sonido actual")
    print("5.- Salir")
    opcion = int(input("Elige una opción(1-5): "))
    if opcion == 1:
        print(f"\n[INFO] Tienes {microtonos_libres} microtonos disponible para usar")
    elif opcion == 2:
        print(f"\n ACTIVAR MICROTONOS (Disponibles: {microtonos_libres})")
        if microtonos_libres == 0:
            print("Ya no se pueden emitir más microtonos, sonido al límite")
        else:
            try:
                cantidad = int(input("¿Cuántos microtonos quieres activar?: "))
                if cantidad <= 0:
                    print("Tienes que activar al menos 1 microtono")
                elif cantidad > microtonos_libres:
                    print(f"Solo puedes activar hasta {microtonos_libres} microtonos")
                else:
                    microtonos_libres -= cantidad
                    microtonos_activos += cantidad
                    print("Reproduciendo microtonos")
                    #for i in range(1, cantidad +1):
                    #    print(f"Microtono {i} activando...")
                    #   winsound.Beep(440,300) #440 HZ por 300 milesimas de segundo
                    #   time.sleep(0.05)
                    frecuencias = [261, 261, 261, 349, 440,261, 261, 261, 349, 440,349, 349, 329, 329, 293, 293, 261]
                    duraciones = [150, 150, 150, 400, 400, 150, 150, 150, 400, 400,300, 300, 300, 300, 300, 300, 600]
                    for i in range(1, cantidad + 1):
                        nota_actual = frecuencias[(i - 1) % len(frecuencias)]
                        duracion_actual = duraciones[(i - 1) % len(duraciones)]
                        winsound.Beep(nota_actual, duracion_actual)
            except ValueError:
                print("Error")
    else:
        print("Error")