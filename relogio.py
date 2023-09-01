from tkinter import *
import tkinter
import pyglet
pyglet.font.add_file("digital-7.ttf")
from datetime import datetime


####### CORES #######
cor_um = "#3d3d3d" #Preta
cor_dois = "#fafcff" #Branca
cor_tres = "#21c25c" #Verde
cor_quatro = "#eb463b" #Vermelha
cor_cinco = "#dedcdc" #Cinza
cor_seis = "#3080f0" #Azul

fundo_relogio = cor_um
cor_escolhida = cor_seis

janela_relogio = Tk()
janela_relogio.title("")
janela_relogio.geometry("440x180")
janela_relogio.resizable(width=FALSE, height=FALSE)
janela_relogio.configure(bg=cor_um)

def relogio():
    tempo=datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia_atual = tempo.day
    mes_atual = tempo.strftime("%b")
    ano_atual = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + ", " + str(dia_atual) + "/" + str(mes_atual) + "/" + str(ano_atual))

l1 = Label(janela_relogio, text="", font="digital-7 100", bg=fundo_relogio, fg=cor_escolhida)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela_relogio, text="", font="digital-7 16", bg=fundo_relogio, fg=cor_escolhida)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela_relogio.mainloop()