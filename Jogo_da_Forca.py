# -*- coding: utf-8 -*-

        # Usa a biblioteca de turtle graphics
import random
import time
import turtle 
from unicodedata import normalize 

m = 1

window = turtle.Screen()

#Escolhe uma palavra aleatória da lista importada para ser a palavra secreta
lista_de_palavras = ["São Paulo"]

palavra = random.choice(lista_de_palavras).upper()
#lista_de_palavras.remove(palavra)
contagem_de_letras = len(palavra)
  
#Cria uma janela
window.bgcolor("lightblue")
window.title("Jogo da forca")

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



#Define a cabeça
def cabeca():
    forca.color("black")
    forca.speed(5)
    forca.penup()       
    forca.setpos(-200,130)
    forca.pendown()
    forca.circle(20)
    forca.hideturtle()

#Define o corpo
def corpo():
    forca.color ("black")
    forca.speed(5)
    forca.penup()
    forca.setpos(-200,130)
    forca.pendown()
    forca.right(90)
    forca.forward(80)
    forca.hideturtle()

#Define a perna esquerda
def perna_esquerda():
    forca.color ("black")
    forca.speed(5)
    forca.penup()
    forca.setpos(-200,50)
    forca.pendown()
    forca.left(90)
    forca.forward(60)
    forca.hideturtle()
    
#Define o braço esquerdo
def braco_esquerdo():
    forca.color ("black")
    forca.speed(5)
    forca.penup()
    forca.setpos(-200,110)
    forca.pendown()
    forca.left(90)
    forca.forward(60)
    forca.hideturtle()
    
#Define a perna direita
def perna_direita():
    forca.color ("black")
    forca.speed(5)
    forca.penup()
    forca.setpos(-200,50)
    forca.pendown()
    forca.right(90)
    forca.forward(60)
    forca.hideturtle()
    
#Define o braço direito
def braco_direito():
    forca.color ("black")
    forca.speed(5)
    forca.penup()
    forca.setpos(-200,110)
    forca.pendown()
    forca.right(45)
    forca.forward(60)
    forca.hideturtle()
    
def acentos(txt):
    return normalize ("NFKD",txt).encode("ASCII","ignore").decode("ASCII")
if __name__ == "__main__":
    from doctest import testmod
    testmod()
    
palavra2 = acentos(palavra)
        

c = 0
x = 0





while m <= 1:
    
#Define a quantidade de epsaços que serão a base para cada letra da palavra secreta
    for x in palavra:
        if x == " ":
            forca.penup()
            forca.setpos(-150+c,-200)
            forca.forward(20)
            c += 30
            forca.hideturtle()
        
        if x != " ":
            forca.penup()
            forca.setpos(-150+c,-200)
            forca.pendown()
            forca.forward(20)
            c += 30
            forca.hideturtle()
            
    

    todas_as_letras_usadas = []

    erro = 0
    acerto = 1
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
         
        elif letra not in palavra2:
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
                if letra in palavra2 and letra == palavra2[j]:
                    forca.penup()
                    forca.setpos(-150+30*j, -200)
                    forca.pendown()
                    forca.write(palavra[j], font = ("Arial",16))
                    forca.hideturtle()
                    j += 1
                    acerto += 1
                    todas_as_letras_usadas.append(letra)
                   
                elif letra in palavra2:
                    j += 1
       
        if erro == 6:
           perna_esquerda()
           erros = turtle.Turtle()
           erros.write ("Game over!", font = ("Arial",20))
           erros.hideturtle()
           time.sleep(1.5)
           erros.clear()
           jogar_novamente = window.textinput("Jogo da forca", "Você deseja jogar novamente")
    
           if jogar_novamente == "sim":
               m -= 1
               erro = 0
               acerto = 0
               forca.reset()
               
               
           if jogar_novamente == "nao":
               m += 1
        
        if acerto == contagem_de_letras:
            acertos = turtle.Turtle()
            acertos.write ("Parabéns, você ganhou!",font = ("Arial",20))
            acertos.hideturtle()
            time.sleep(1.5)
            acertos.clear()
            jogar_novamente = window.textinput("Jogo da forca", "Você deseja jogar novamente")
    
            if jogar_novamente == "sim":
               m -= 1
               erro = 0
               acerto = 0
               forca.reset()
               
            if jogar_novamente == "nao":
               m += 1


window.exitonclick()
