import turtle
import time
import random
from io import open
retrasar=0.1


#guardar score en un archivo de texto
Score=0
Savemejor_puntaje=open("Mejor_Score.txt","r")
contenido=Savemejor_puntaje.read()
Savemejor_puntaje.close()
HighScore=int(contenido)


#configuración de la pantalla
pantalla=turtle.Screen()
pantalla.title("Snake")
pantalla.bgcolor("black")
pantalla.setup(width=600,height=600)
pantalla.tracer(0)


#cabeza de la serpiente
cabeza=turtle.Turtle()
cabeza.speed(0)         #movimiento de la serpiente
cabeza.shape("square")  #forma de la serpiente
cabeza.color("green")
cabeza.penup()          #quitar rastros del objecto
cabeza.goto(0,0)
cabeza.direction="stop"


#Comida
Comida=turtle.Turtle()
Comida.speed(0)
Comida.shape("circle")
Comida.color("red")
Comida.penup()
Comida.goto(0,100)

#obstaculos
obstaculos=turtle.Turtle()
obstaculos.speed(0)
obstaculos.shape("square")
obstaculos.color("pink")
obstaculos.penup()
obstaculos.goto(100,100)

 



    


#cuerpo serpiente

cuerpo=[]


#texto#
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score:{}   High Score:{}" .format(Score,HighScore),align="center",font=("Courier",24,"normal"))


#funciones para actualizar el movimiento
def arriba():
    cabeza.direction="up"
def abajo():
    cabeza.direction="down"
def izquierda():
    cabeza.direction="left"
def derecha():
    cabeza.direction="right"


#configuración de movimiento, se obtienen las coordenadas de cuanto se debe mover en cada acción
def mov():
    if cabeza.direction=="up":
        y= cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction=="down":
        y= cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction=="left":
        x= cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction=="right":
        x= cabeza.xcor()
        cabeza.setx(x+20)


#configurar teclado
pantalla.listen()
pantalla.onkeypress(arriba,"Up")
pantalla.onkeypress(abajo,"Down")
pantalla.onkeypress(izquierda,"Left")
pantalla.onkeypress(derecha,"Right")


#el programa, bucle para queel programa se este actualizando siempre
while True:
    pantalla.update()
    #colisión obstaculo
    if cabeza.distance(obstaculos)<20:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction="stop"
        for cuerpo_nuevo in cuerpo:
            cuerpo_nuevo.goto(1000,1000)
        mejor_puntaje=open("Mejor_Score.txt","w")
        p=str(HighScore)
        mejor_puntaje.write(p)
        mejor_puntaje.close()
        cuerpo=[]
        Score=0
        texto.clear()
        texto.write("Score:{}   High Score:{}".format(Score,HighScore),align="center",font=("Courier",24,"normal"))
    #colisión borde
    if cabeza.xcor() > 280 or cabeza.xcor()<-280 or cabeza.ycor()>280 or cabeza.ycor()<-280:
        cabeza.goto(0,0) 
        cabeza.direction="stop"
        for cuerpo_nuevo in cuerpo:
            cuerpo_nuevo.goto(1000,1000)
        mejor_puntaje=open("Mejor_Score.txt","w")
        p=str(HighScore)
        mejor_puntaje.write(p)
        mejor_puntaje.close()
        cuerpo=[]
        Score=0
        texto.clear()
        texto.write("Score:{}   High Score:{}".format(Score,HighScore),align="center",font=("Courier",24,"normal"))
    






    #colisión comida
    if cabeza.distance(Comida)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        Comida.goto(x,y)


        #nuevos segmentos, aqui solo se crean los segmentos del cuerpos
        cuerpo_nuevo=turtle.Turtle()
        cuerpo_nuevo.speed(0)
        cuerpo_nuevo.shape("square")  
        cuerpo_nuevo.color("purple")
        cuerpo_nuevo.penup()


        #agregar nuevos segmentos al cuerpo, aqui se agrega el nuevo segmento a la lista del cuerpo
        cuerpo.append(cuerpo_nuevo)


        #puntuación
        Score+=1
        if Score>HighScore:
            HighScore=Score
        texto.clear()
        texto.write("Score:{}   High Score:{}".format(Score,HighScore),align="center",font=("Courier",24,"normal"))
    
    #mover el cuerpo de la serpiente, aqui lo que se hace es hacer que cada recuadro siga al siguiente
    #que el primero cambie de posición, y que los demas vayan ocupando el lugar del que le sigue
    totalseg=len(cuerpo)
    for index in range(totalseg-1,0,-1):   #desde el numero mayor, hasta el primero,decrecer el valor
        x=cuerpo[index-1].xcor()            #obtengo las coordenadas anteriores de cada recuadro
        y=cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)             #coge el indice actual y lo mueve por el metodo a las coordenadas
    if totalseg>0:                          #anteriormente obtenidas 
        x=cabeza.xcor()
        y=cabeza.ycor()
        cuerpo[0].goto(x,y)                 #que el primer elemento se mueva donde esta la cabeza


    mov()
    #colisciones con el cuerpo
    for cuerpo_nuevo in cuerpo:
        if cuerpo_nuevo.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction="stop"
            for cuerpo_nuevo in cuerpo:
                cuerpo_nuevo.goto(1000,1000)
            mejor_puntaje=open("Mejor_Score.txt","w")
            p=str(HighScore)
            mejor_puntaje.write(p)
            mejor_puntaje.close()
            cuerpo=[]
            Score=0
            texto.clear()
            texto.write("Score:{}   High Score:{}".format(Score,HighScore),align="center",font=("Courier",24,"normal"))
            




    time.sleep(retrasar) #esto es para retrasar el tiempo de corrida por pixel