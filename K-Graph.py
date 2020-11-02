from math import pi
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


# CALCULANDO LOS VÉRTICES  [Coord. X, Coord. Y, Nombre, Grado]
def CalcularVertices(num_vertices):

    Vertices=[]

    for i in range(num_vertices):

        Vertice_valido = False
        num_intentos = 0

        while Vertice_valido == False:

            num_intentos += 1
            if num_intentos < 50:

                try:
                    Vertice_temp = [random.randint(-300, 300), random.randint(-250, 250)]

                    for Vertice in Vertices:

                        distancia = math.sqrt(
                            (Vertice[0]-Vertice_temp[0])**2+(Vertice[1]-Vertice_temp[1])**2)

                        if distancia < 80:
                            print("[/] Vertice "+str(Vertice_temp) +
                                " no válido. Está a una distancia "+str(distancia)+" de "+str(Vertice))
                            break

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

    return Vertices

# DIBUJANDO LOS VÉRTICES
def DibujarVertices(Vertices):

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
def CalcularAristas(Vertices,Grado_vertices):


    Aristas_creadas,salir=False,False
    while Aristas_creadas==False:
          
        Aristas=[]

        for Vertice in Vertices:

            Grado_vertice = Vertice[3]

            for _ in range(Grado_vertices-Grado_vertice):

                Arista_valida = False
                acc=0

                while Arista_valida == False:

                    if acc==50:
                        print("=================================\nDemasiados intentos. Reintentando\n=================================")
                        salir=True
                        break

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


                if salir==True:
                    salir=False
                    break

        count=0
        for Vertice in Vertices:
            if Vertice[3]!=Grado_vertices:
                count+=1
        
        if count==0:
            Aristas_creadas=True
        else:
            for Vertice in Vertices:
                Vertice[3]=0
            

    return Aristas

# DIBUJANDO LAS ARISTAS
def DibujarAristas(Aristas):

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

# RESOLVER EL JUEGO
def Resolver(t_juego,Aristas,Vertice_inicial):

    t_juego.clear()
    t_juego.penup()

    t_juego.goto(Vertice_inicial[0],Vertice_inicial[1])
    Vertice_actual=Vertice_inicial
    t_juego.speed(2)
    t_juego.pendown()

    salir_temp=False
    while salir_temp==False:

        Vertice_sig, Arista_temp="",""
        
        max=0

        for Arista in Aristas:

            if Vertice_actual in Arista[0]:
                
                if Arista[0][0]==Vertice_actual:

                    Vertice_temp=Arista[0][1]

                    if Vertice_temp[3]>max:

                        Vertice_sig=Vertice_temp
                        Arista_temp=Arista


                else:
                    
                    Vertice_temp=Arista[0][0]

                    if Vertice_temp[3]>max:

                        Vertice_sig=Vertice_temp
                        Arista_temp=Arista


        Aristas.remove(Arista_temp)
             

        if Vertice_sig[0]>t_juego.xcor():
            t_juego.settiltangle(math.atan((Vertice_sig[1]-t_juego.ycor())/(Vertice_sig[0]-t_juego.xcor())))        
        else:
            t_juego.settiltangle(math.pi+math.atan((Vertice_sig[1]-t_juego.ycor())/(Vertice_sig[0]-t_juego.xcor())))  

        t_juego.goto(Vertice_sig[0], Vertice_sig[1])
        Vertice_actual=Vertice_sig

        if not Aristas:
            salir_temp=True


    t_juego.penup()
    t_juego.circle(20)
    t_juego.fillcolor()


# JUEGO
def Graph():
    # PIDIENDO DATOS
    try:

        num_vertices = int(input(
            "\n>> Ingrese el número de vértices deseados. No se recomiendan más de 30 vértices\n"))

        if num_vertices <= 2:
            num_vertices = 3
            print("Se necesitan un mínimo de 3 vértices. Se dibujarán 3 vértices")

    except:
        
        num_vertices = 3
        print("Número ingresado no válido. Se dibujarán 3 vértices")


    try:

        Grado_vertices = int(input(
            "\n>> Ingrese el grado (par) de los vértices. El máximo grado posible es "+str(num_vertices-1)+".\n"))

        if Grado_vertices >= num_vertices:
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


    Vertices=CalcularVertices(num_vertices)
    DibujarVertices(Vertices)
    Aristas=CalcularAristas(Vertices, Grado_vertices)
    DibujarAristas(Aristas)    

    print("~~~~~~~~> VERTICES <~~~~~~~~~")
    print(Vertices)
    print("\n~~~~~~~~> ARISTAS <~~~~~~~~~")
    print(Aristas)

    Aristas_old=Aristas.copy()
    

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
        print(Vertices)
        for Vertice in Vertices:
            print(Vertice[2])
            if Vertice_inicial == Vertice[2]:
                Vertice_inicial = Vertice
                Vertice_valido = True

    t_juego.goto(Vertice_inicial[0], Vertice_inicial[1])
    t_juego.pen(pencolor="green", pensize=2, speed=3)
    t_juego.pendown()


    # MOVIMIENTO ENTRE VÉRTICES
    Vertice_actual, Juego_terminado, Intentos = Vertice_inicial, False, 3

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
                    t_juego.penup()
                    t_juego.circle(20)
                    t_juego.fillcolor()

                else:
                    print("[/] El recorrido encontrado no es un circuito Euleriano")
                    
                    print("\n==> RESOLVIENDO EL GRAFO "+str(Grado_vertices)+"-Regular")
                    Resolver(t_juego,Aristas_old,Vertice_inicial)     


                Juego_terminado=True

        else:

            Intentos -= 1

            if Intentos>0:
                print("[/] No es un movimiento válido. Te quedan "+str(Intentos)+" intentos.")
            else:
                print(">> ¡Se te agotaron los intentos!")            

                print("\n==> RESOLVIENDO EL GRAFO "+str(Grado_vertices)+"-Regular")
                Resolver(t_juego,Aristas_old,Vertice_inicial)   

                Juego_terminado=True


    print("Haz click en la ventana de juego para cerrarlo")

    ventana.exitonclick()


#=====> E J E C U C I Ó N <======

Graph()