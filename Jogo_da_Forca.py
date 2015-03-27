# -*- coding: utf-8 -*-

        # Usa a biblioteca de turtle graphics
import random
import time
import turtle  

m = 0

window = turtle.Screen()

#Escolhe uma palavra aleatória da lista importada para ser a palavra secreta
lista_de_palavras = ["São Paulo"]

palavra = random.choice(lista_de_palavras).upper()
contagem_de_letras = len(palavra)
  
#Cria uma janela
window.bgcolor("lightblue")
window.title("Jogo da forca")


#Define a cabeça
def cabeca():
    cabeca = turtle.Turtle()
    cabeca.color("black")
    cabeca.speed(5)
    cabeca.penup()       
    cabeca.setpos(-200,130)
    cabeca.pendown()
    cabeca.circle(20)
    cabeca.hideturtle()

#Define o corpo
def corpo():
    corpo = turtle.Turtle()
    corpo.color ("black")
    corpo.speed(5)
    corpo.penup()
    corpo.setpos(-200,130)
    corpo.pendown()
    corpo.right(90)
    corpo.forward(80)
    corpo.hideturtle()

#Define a perna esquerda
def perna_esquerda():
    perna_esquerda = turtle.Turtle()
    perna_esquerda.color ("black")
    perna_esquerda.speed(5)
    perna_esquerda.penup()
    perna_esquerda.setpos(-200,50)
    perna_esquerda.pendown()
    perna_esquerda.left(225)
    perna_esquerda.forward(60)
    perna_esquerda.hidturtle()
    
#Define o braço esquerdo
def braco_esquerdo():
    braco_esquerdo = turtle.Turtle()
    braco_esquerdo.color ("black")
    braco_esquerdo.speed(5)
    braco_esquerdo.penup()
    braco_esquerdo.setpos(-200,110)
    braco_esquerdo.pendown()
    braco_esquerdo.left(225)
    braco_esquerdo.forward(60)
    braco_esquerdo.hideturtle()
    
#Define a perna direita
def perna_direita():
    perna_direita = turtle.Turtle()
    perna_direita.color ("black")
    perna_direita.speed(5)
    perna_direita.penup()
    perna_direita.setpos(-200,50)
    perna_direita.pendown()
    perna_direita.right(45)
    perna_direita.forward(60)
    perna_direita.hideturtle()
    
#Define o braço direito
def braco_direito():
    braco_direito = turtle.Turtle()
    braco_direito.color ("black")
    braco_direito.speed(5)
    braco_direito.penup()
    braco_direito.setpos(-200,110)
    braco_direito.pendown()
    braco_direito.right(45)
    braco_direito.forward(60)
    braco_direito.hideturtle()

i = 0
c = 0
x = 0
    
#Define a base da forca
forca = turtle.Turtle()
forca.color("black")
forca.speed(5)
forca.penup()       
forca.setpos(-300,-200)
forca.pendown()
forca.left (90)
forca.forward (400)
forca.right(90)
forca.forward(100)
forca.right(90)
forca.forward (30)
forca.hideturtle
forca.penup()
forca.left(90)

#Define a quantidade de epsaços que serão a base para cada letra da palavra secreta
while i < contagem_de_letras:
    tracos = turtle.Turtle()
    tracos.penup()
    tracos.setpos(-150+c,-200)
    tracos.pendown()
    tracos.forward(20)
    i +=1
    c += 30
    tracos.hideturtle()
    
    for x in range (1,contagem_de_letras):
        if palavra[x] == " ":
            tracos.penup()
            tracos.setpos(-150+30*x,-200)
            tracos.pendown()
            tracos.write("  ")
            
    

todas_as_letras_usadas = []

erro = 0
acerto = 0
t = 0



while erro < 6 and acerto < contagem_de_letras:
    j = 0
    letra = window.textinput("Letra", "Chute uma letra").upper()
    
    if letra in todas_as_letras_usadas:
         todas_as_letras_usadas.append(letra)
         repetida = turtle.Turtle()
         repetida.write ("Essa letra já foi utilizada", font = ("Arial",20))
         repetida.hideturtle()
         time.sleep(1)
         repetida.clear()
         
    elif letra not in palavra:
        todas_as_letras_usadas.append(letra)
        erro += 1
            
        if erro == 1:
               cabeca()
    
        elif erro == 2:
               corpo()
        
        elif erro == 3:
               braco_direito()
        
        elif erro == 4:
               braco_esquerdo()
    
        elif erro == 5:
               perna_direita()
    
    else:
        while j < contagem_de_letras:
            if letra in palavra and letra == palavra[j]:
                   forca.penup()
                   forca.setpos(-150+30*j, -200)
                   forca.pendown()
                   forca.write(palavra[j], font = ("Arial",12))
                   forca.hideturtle()
                   j += 1
                   acerto += 1
                   todas_as_letras_usadas.append(letra)
                   
            elif letra in palavra:
                   j += 1
       
if erro == 6:
    perna_esquerda()
    erros = turtle.Turtle()
    erros.write ("Game over!", font = ("Arial",20))
    time.sleep(2)
    m = window.textinput("Jogo da forca", "Para jogar novamente digite 0")

if acerto == contagem_de_letras:
    acertos = turtle.Turtle()
    acertos.write ("Parabéns, você ganhou!",font = ("Arial",20))
    time.sleep(2)
    m = window.textinput("Jogo da forca", "Para jogar novamente digite 0")



window.exitonclick()
