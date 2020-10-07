import turtle
import random
import math

Letra = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
         "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# turtle.shapesize(1,5,10)  para todas las tortugas
# t.shape("turtle")
# t.circle(60)
# t.dot(20)
# t.pensize(10)
# t.shapesize(1,5,10)
# t.pencolor("red")
# t.fillcolor("blue")
# t.begin_fill()
# t.end_fill()  rellenar formas cerradas
# t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)  forma abreviada
# t.penup()  deja de pintar
# t.pendown()    buelve a pintar
# t.undo() deshace el último comando
# t.clear() limpiar la pantalla
# c=t.clone()  clona una tortuga

# X (-300, 300)
# Y (-250, 250)

# <~~ GENERACIÓN DE VÉRTICES ~~>
try:
    Num_vertices = int(input(
        "\n>> Ingrese el número de vértices deseados. No se recomiendan más de 30 vértices\n"))

    if Num_vertices <= 2:
        Num_vertices = 3
        print("Se necesitan un mínimo de 3 vértices. Se dibujarán 3 vértices")

except:
    Num_vertices = 3
    print("Número ingresado no válido. Se dibujarán 3 vértices")

try:
    Grado_vertices = int(input(
        "\n>> Ingrese el grado (par) de los vértices. El máximo grado posible es "+str(Num_vertices-1)+".\n"))

    if Grado_vertices >= (Num_vertices):
        Grado_vertices = 2
        print("Se excedió el número máximo. Los vértices serán de grado 2")

    elif Grado_vertices < 2:
        Grado_vertices=2
        print("Se necesitan al menos un grafo 2-Regular. Los vértices serán de grado 2")

    elif Grado_vertices % 2 == 1:
        Grado_vertices -= 1
        print("Se debe tener un número par. Los vértices serán de grado "+str(Grado_vertices))

except:
    Grado_vertices = 2
    print("Número ingresado no válido. Los vértices serán de grado 2")


# VENTANA CANVAS
ventana = turtle.getscreen()
turtle.title("Grafo "+str(Grado_vertices)+"-Regular")
rootwindow = ventana.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

ventana.clear()


# CALCULANDO LOS VÉRTICES  [Coord. X, Coord. Y, Nombre, Grado]
Vertices = []
for i in range(Num_vertices):
    Vertice_valido = False
    Num_intentos = 0

    while Vertice_valido == False:

        Num_intentos += 1
        if Num_intentos < 50:

            try:
                Vertice_temp = [
                    random.randint(-300, 300), random.randint(-250, 250)]

                for Vertice in Vertices:

                    distancia = math.sqrt(
                        (Vertice[0]-Vertice_temp[0])**2+(Vertice[1]-Vertice_temp[1])**2)

                    if distancia < 80:
                        print("[/] Vertice "+str(Vertice_temp) +
                              " no válido. Está a una distancia "+str(distancia)+" de "+str(Vertice))
                        err += 1

                print("Vertice "+str(Vertice_temp)+" válido.")

                try:
                    Vertice_temp.append(Letra[i])  # Nombre
                except:
                    Vertice_temp.append(Letra[i-27]+"1")

                Vertice_temp.append(0)  # Grado
                Vertices.append(Vertice_temp)
                Vertice_valido = True

            except:
                pass

        else:
            print("[/] Se intentó demasiadas veces.")
            Vertice_valido = True

# DIBUJANDO LOS VÉRTICES
t_vertices = turtle.Turtle()
t_vertices.pencolor("red")
t_vertices.left(90)
t_vertices.penup()
t_vertices.hideturtle()
t_vertices.speed(50)

for Vertice in Vertices:
    t_vertices.goto(Vertice[0], Vertice[1])
    t_vertices.dot(15, "black")
    t_vertices.forward(15)
    t_vertices.write(Vertice[2])


# CALCULANDO LAS ARISTAS
Aristas_creadas=False

while Aristas_creadas==False:

    try:
        Aristas = []
        for Vertice in Vertices:

            Grado_vertice = Vertice[3]

            for _ in range(Grado_vertices-Grado_vertice):

                Arista_valida = False
                acc=0

                while Arista_valida == False:

                    if acc==150:
                        print("=================================\nDemasiados intentos. Reintentando\n=================================")
                        err+=1

                    Vertice_temp = Vertices[random.randint(0, len(Vertices)-1)]

                    Arista_temp = [[Vertice, Vertice_temp],
                                [Vertice_temp, Vertice]]
                    Arista_alt = [[Vertice_temp, Vertice],
                                [Vertice, Vertice_temp]]

                    if Vertice_temp[3] < Grado_vertices and Vertice != Vertice_temp:

                        if (Arista_temp not in Aristas) and (Arista_alt not in Aristas):

                            Vertice[3] += 1
                            Vertice_temp[3] += 1

                            Aristas.append(Arista_temp)
                            Arista_valida = True

                    # SI HUBIERA LAZOS
                    # elif Vertice_temp[3] < (Grado_vertices-1) and Vertice == Vertice_temp:

                    #     if (Arista_temp not in Aristas) and (Arista_alt not in Aristas):

                    #         Vertice[3] += 2
                    #         Aristas.append(Arista_temp)
                    #         print("LAZO  ", Arista_temp)
                    #         Arista_valida = True

                    else:
                        acc+=1
                        print("[/] No se pudo meter ",Arista_temp)
                        print("Vertices:",Vertices)

        Aristas_creadas=True
        
    except: pass

print("~~~~~~~~> VERTICES <~~~~~~~~~")
print(Vertices)

# DIBUJANDO LAS ARISTAS
t_aristas = turtle.Turtle()
t_aristas.pencolor("blue")
t_aristas.penup()
t_aristas.hideturtle()

for Arista in Aristas:
    t_aristas.speed(0)
    t_aristas.goto(Arista[0][0][0], Arista[0][0][1])
    t_aristas.pendown()

    t_aristas.speed(3)
    t_aristas.goto(Arista[0][1][0], Arista[0][1][1])
    t_aristas.penup()


# JUEGO

def Resolver():
    print("hellou")

t_juego = turtle.Turtle()
t_juego.shape("turtle")
t_juego.radians()
t_juego.pencolor("green")
t_juego.penup()
t_juego.speed(0)

# VÉRTICE INICIAL
Vertice_valido, Vertice_inicial = False, []

while Vertice_valido == False:
    Vertice_inicial = input("Ingrese el vértice para comenzar:\n").upper()

    for Vertice in Vertices:
        if Vertice_inicial == Vertice[2]:
            Vertice_inicial = Vertice
            Vertice_valido = True

t_juego.goto(Vertice_inicial[0], Vertice_inicial[1])
t_juego.pen(pencolor="green", pensize=2, speed=5)
t_juego.pendown()

Vertice_actual, Juego_terminado, Intentos = Vertice_inicial, False, 3

# MOVIMIENTO ENTRE VÉRTICES
while Juego_terminado == False:
    Vertice_temp = input("Ingrese el vértice al cual desea moverse:\n").upper()

    for Vertice in Vertices:
        if Vertice_temp == Vertice[2]:
            Vertice_temp = Vertice

    Arista_temp = [[Vertice_actual, Vertice_temp],[Vertice_temp,Vertice_actual]]
    Arista_temp2 = [[Vertice_temp,Vertice_actual],[Vertice_actual, Vertice_temp]]

    if Arista_temp in Aristas or Arista_temp2 in Aristas:
        
        if Arista_temp in Aristas:
            Aristas.remove(Arista_temp)
        else:
            Aristas.remove(Arista_temp2)

        if Vertice_temp[0]>t_juego.xcor():
            t_juego.settiltangle(math.atan((Vertice_temp[1]-t_juego.ycor())/(Vertice_temp[0]-t_juego.xcor())))        
        else:
            t_juego.settiltangle(math.pi+math.atan((Vertice_temp[1]-t_juego.ycor())/(Vertice_temp[0]-t_juego.xcor())))  

        t_juego.goto(Vertice_temp[0], Vertice_temp[1])

        Vertice_actual = Vertice_temp
        if len(Aristas)==0:
            if Vertice_actual==Vertice_inicial:
                print(">> ¡Has encontrado un circuito de Euler! El juego ha finalizado")
            else:
                print(">> ¡El recorrido encontrado no es un circuito!")
                t_juego.goto(Vertice_inicial[0],Vertice_inicial[1])
                t_juego.clear()
                Resolver()

            Juego_terminado=True

    else:
        Intentos -= 1
        if Intentos>0:
            print("[/] No es un movimiento válido. Te quedan "+str(Intentos)+" intentos.")
        else:
            print(">> ¡Se te agotaron los intentos!")            
            t_juego.goto(Vertice_inicial[0],Vertice_inicial[1])
            t_juego.clear()
            Resolver()

            Juego_terminado=True

print("Haz click en la ventana de juego para cerrarlo")
ventana.exitonclick()
