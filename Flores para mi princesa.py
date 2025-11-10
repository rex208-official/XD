import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.bgcolor("skyblue")

# Crear un turtle para el ramo
ramo = turtle.Turtle()
ramo.speed(10)

# Función para dibujar una flor
def dibujar_flor(x, y):
    ramo.penup()
    ramo.goto(x, y)
    ramo.pendown()
    ramo.color("white")
    ramo.begin_fill()
    for _ in range(6):
        ramo.circle(15, 180)  # Hacer un pétalo de flor
        ramo.left(60)
    ramo.end_fill()

# Dibujar las flores de nube (ramo)
flores_posiciones = [(-100, 0), (0, 100), (100, 0), (0, -100), (-100, -100), (100, 100)]
for pos in flores_posiciones:
    dibujar_flor(pos[0], pos[1])

# Crear un turtle para el mensaje
mensaje = turtle.Turtle()
mensaje.speed(1)
mensaje.penup()
mensaje.goto(-200, -200)
mensaje.pendown()
mensaje.color("black")
mensaje.write("Te amaré, por toda la eternidad,\n"
              "Te cuidaré, y te protegeré,\n"
              "Y te seré fiel, hasta que estas flores se marchiten", font=("Arial", 16, "normal"))

# Esconde el turtle
ramo.hideturtle()
mensaje.hideturtle()

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.done()
