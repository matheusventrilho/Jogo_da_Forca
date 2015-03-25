# -*- coding: utf-8 -*-

import turtle          # Usa a biblioteca de turtle graphics
import random

window = turtle.Screen()

arquivo = open("entrada.txt","r", encoding="UTF-8")
leitura = arquivo.readlines()
lista_de_palavras = []

for i in range(0,len(leitura)):
    limpa = leitura[i].strip()
    if (limpa != ""):
        lista_de_palavras.append(limpa)
        
print(lista_de_palavras)

palavra = random.choice(lista_de_palavras)
contagem_de_letras = len(palavra)
  
#Cria uma janela
window.bgcolor("lightblue")
window.title("Jogo da forca")


def cabeca():
    cabeca = turtle.Turtle()
    cabeca.color("black")
    cabeca.speed(5)
    cabeca.penup()       
    cabeca.setpos(-200,130)
    cabeca.pendown()
    cabeca.circle(20)

def corpo():
    corpo = turtle.Turtle()
    corpo.color ("black")
    corpo.speed(5)
    corpo.penup()
    corpo.setpos(-200,130)
    corpo.pendown()
    corpo.right(90)
    corpo.forward(80)

def perna_esquerda():
    perna_esquerda = turtle.Turtle()
    perna_esquerda.color ("black")
    perna_esquerda.speed(5)
    perna_esquerda.penup()
    perna_esquerda.setpos(-200,50)
    perna_esquerda.pendown()
    perna_esquerda.left(225)
    perna_esquerda.forward(60)
    
def braco_esquerdo():
    braco_esquerdo = turtle.Turtle()
    braco_esquerdo.color ("black")
    braco_esquerdo.speed(5)
    braco_esquerdo.penup()
    braco_esquerdo.setpos(-200,110)
    braco_esquerdo.pendown()
    braco_esquerdo.left(225)
    braco_esquerdo.forward(60)
    
def perna_direita():
    perna_direita = turtle.Turtle()
    perna_direita.color ("black")
    perna_direita.speed(5)
    perna_direita.penup()
    perna_direita.setpos(-200,50)
    perna_direita.pendown()
    perna_direita.right(45)
    perna_direita.forward(60)
    
def braco_direito():
    braco_direito = turtle.Turtle()
    braco_direito.color ("black")
    braco_direito.speed(5)
    braco_direito.penup()
    braco_direito.setpos(-200,110)
    braco_direito.pendown()
    braco_direito.right(45)
    braco_direito.forward(60)

def espacos():
    espacos = turtle.Turtle()
    espacos.color("black")
    espacos.speed(5)
    espacos.penup()
    espacos.setpos(-150,-180)
    espacos.forward(30)
    espacos.penup()
    
    #Define a base:
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
forca.penup()
 
espacos()*contagem_de_letras
 
letras = []

letra = window.textinput("Letra", "Tente acertar uma letra da palavra secreta")
letras.append(letra)

partes_do_humano = [cabeca(),corpo(),braco_direito(),braco_esquerdo(),perna_direita(),perna_esquerda()]

erro = 0
        
def erros():
    partes_do_humano[0]
    del partes_do_humano[0]
    


window.exitonclick()
