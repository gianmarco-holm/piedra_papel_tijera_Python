import random

opciones = ['Piedra', 'Papel', 'Tijera']

def respuestaUsuario(opciones):
    while True:
        print('Elija una opción:')
        for i, item in enumerate(opciones, start=1):
            print(f'{i}. {item}')
        try:
            respuesta = int(input("Ingrese un número: "))
            if 1 <= respuesta <= len(opciones):
                return opciones[respuesta-1]
            else:
                print("Ingrese un número válido")
        except ValueError:
            print("Por favor, ingrese un número válido")

def respuestaComputadora(opciones):
    return random.choice(opciones)

def determinarGanador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (
        (usuario == 'Piedra' and computadora == 'Tijera') or
        (usuario == 'Papel' and computadora == 'Piedra') or
        (usuario == 'Tijera' and computadora == 'Papel')
    ):
        return "¡Ganaste!"
    else:
        return "¡La computadora ganó!"

while True:
    print("********************************")
    print("PIEDRA, PAPEL O TIJERA")
    print("********************************")

    usuario = respuestaUsuario(opciones)
    computadora = respuestaComputadora(opciones)
    ganador = determinarGanador(usuario, computadora)

    print(f'Tu elección: {usuario}')
    print(f'Elección de la computadora: {computadora}\n')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(ganador)
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

    print("¿Deseas seguir jugando?")
    print("1. Sí")
    print("2. No")

    try:
        respuesta = int(input("Ingrese una opción: "))
        if respuesta != 1:
            break
    except ValueError:
        print("Por favor, ingrese un número válido")

# Mensaje de despedida
print("Gracias por jugar. ¡Hasta luego!")
