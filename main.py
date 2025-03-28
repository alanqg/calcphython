# importando tkinter
from tkinter import *
from tkinter import ttk


#Cores do projetos 
cor1 = "#1e1f1e" # cor escura
cor2 = "#feffff" # cor clara
cor3 = "#38576b" # Azul caeeragar
cor4 = "#eceff1" # cinzenta
cor5 = "#ffab40" #orange
janela =Tk()

#titulo da janela
janela.title("Calculadora")
#definindo lagura e altura
janela.geometry("235x310")
#confirações gerais
janela.config(bg=cor1)


#frames 
#diplay tela top da calculadora
frame_tela = Frame(janela, width=235,height=50, bg=cor3)
#grid
frame_tela.grid(row=0, column=0)

#corpo da calculadora 
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = '' #variavel global para armazenar todos os valores


#label para os números
valor_texto = StringVar()
#Criando funções
def entrar_valoeres(event):

    #Criando uma variavel global 
    global todos_valores


    todos_valores = todos_valores + str(event)

    #passando valor para a tela
    valor_texto.set(todos_valores)

#Função calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


#função limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7,relief=FLAT, anchor="e", justify="right", font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#cirando botões 
b_c = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_c.place(x=0, y=0) #finalizado o primeiro botão 

#segundo botão
b_pcente = Button(frame_corpo, command = lambda: entrar_valoeres('%') , text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_pcente.place(x=118, y=0)


#terceiro botão
b_divisao = Button(frame_corpo,  command = lambda: entrar_valoeres('/'),  text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_divisao.place(x=177, y=0)

#Segunda estapa dos botões 
b_7 = Button(frame_corpo, command = lambda: entrar_valoeres('7'),  text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=52)
#segundo botão
b_8 = Button(frame_corpo,  command = lambda: entrar_valoeres('8'),  text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=52)
#terceiro botão
b_9 = Button(frame_corpo, command = lambda: entrar_valoeres('9'),  text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=52)
#quarto botão
b_mult = Button(frame_corpo,  command = lambda: entrar_valoeres('*'),  text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_mult.place(x=177, y=52)



#Terceira estapa dos botões 
b_4 = Button(frame_corpo, command = lambda: entrar_valoeres('4'),  text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=104)
#segundo botão
b_5 = Button(frame_corpo, command = lambda: entrar_valoeres('5'),  text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=104)
#terceiro botão
b_6 = Button(frame_corpo, command = lambda: entrar_valoeres('6'),  text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=104)
#quarto botão
b_menos = Button(frame_corpo,  command = lambda: entrar_valoeres('-'),  text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_menos.place(x=177, y=104)



#Quarta estapa dos botões 
b_1 = Button(frame_corpo, command = lambda: entrar_valoeres('1'),  text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=156)
#segundo botão
b_2 = Button(frame_corpo, command = lambda: entrar_valoeres('2'),  text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=156)
#terceiro botão
b_3 = Button(frame_corpo, command = lambda: entrar_valoeres('3'),  text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=156)
#quarto botão
b_mais = Button(frame_corpo,  command = lambda: entrar_valoeres('+'),  text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_mais.place(x=177, y=156)


#botões finais 
#botões 
b_1 = Button(frame_corpo,  command = lambda: entrar_valoeres('0'),  text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=208) #finalizado o primeiro botão 

#segundo botão
b_2 = Button(frame_corpo, command = lambda: entrar_valoeres('.'),  text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=208)


#terceiro botão
b_3 = Button(frame_corpo,  command = calcular,  text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=208)





janela.mainloop()


