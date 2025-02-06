from tkinter import * # o * significa q ele esta importando tudo da biblioteca
from tkinter import ttk


#Cores

cor1 = "#804f7e" #cinza escuro

cor2 = "#752272" #rosa kark

cor3 = "#f0bcf5" #rosa 

cor4 = "#b579ba" #rosa escuro

cor5 = "#f7f7f7" #rosa branco




#Config da Janela

janela = Tk()
janela.title("Calculadora")

janela.geometry("280x310") #Define tamanho basico da janela

frame_tela = Frame(janela, width=280, height=50, bg=cor2)


frame_tela.grid(row=0, column=0)


frame_botão = Frame(janela, width=280, height=300)
frame_botão.grid(row=1, column=0)




#variavel valores

valores = ''


#Criando FUNÇÕES

valor_texto= StringVar()

#Criando função calcular


def inserir_D(event):

    global valores 

    valores = valores + str(event)
    

    #Passando valor para tela
    valor_texto.set(valores)


#função para calcular

def calcular():
    try:
        global valores

        valores = valores.replace('x', '*')
        valores = valores.replace('÷', '/')
        if '**' in valores:

            valor_texto.set('Equação Inválida.')
        if '*-+' in valores:
            valor_texto.set('Equação Inválida.')
        if '*+-' in valores:
            valor_texto.set('Equação Inválida.')
        else:
            resultado = eval(valores)

            valores.set(resultado)

    except SyntaxError:
        valor_texto.set('Equação Inválida.')
    except ZeroDivisionError:
        valor_texto.set('Impos. dividir por 0.')


def limpar_tela():

    global valores

    valores = ''

    valor_texto.set('')



app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=15, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 19 '), bg=cor2, fg=cor5)
app_label.place(x=0, y=0)




#criando botões

#linha 1
b_c = Button(frame_botão, command= limpar_tela, text="C", width=13, height=2, bg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_c.place(x=0,y=0) #X é horizontal e y é vertical

b_div = Button(frame_botão, command= lambda:inserir_D('%'), text="%", width=6, height=2, bg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=140,y=0)

b_barr = Button(frame_botão, command= lambda:inserir_D('/'), text="/", width=6, height=2, bg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_barr.place(x=210,y=0)


#Linha 2

b_div = Button(frame_botão, command= lambda:inserir_D('7'), text="7", width=6, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=0,y=52)

b_div = Button(frame_botão, command= lambda:inserir_D('8'), text="8", width=6, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=70,y=52)

b_div = Button(frame_botão, command= lambda:inserir_D('9'), text="9", width=6, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=140,y=52)

b_div = Button(frame_botão, command= lambda:inserir_D('*'), text="*", width=6, height=2, bg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=210,y=52)

#linha 3

b_div = Button(frame_botão, command= lambda:inserir_D('4'), text="4", width=6, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=0,y=104)

b_div = Button(frame_botão, command= lambda:inserir_D('5'), text="5", width=6, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=70,y=104)

b_div = Button(frame_botão, command= lambda:inserir_D('6'), text="6", width=6, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=140,y=104)

b_div = Button(frame_botão, command= lambda:inserir_D('-'), text="-", width=6, height=2, bg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=210,y=104)

#linha 4

b_div = Button(frame_botão, command= lambda:inserir_D('1'), text="1", width=6, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=0,y=156)

b_div = Button(frame_botão, command= lambda:inserir_D('2'), text="2", width=6, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=70,y=156)

b_div = Button(frame_botão, command= lambda:inserir_D('3'), text="3", width=6, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=140,y=156)

b_div = Button(frame_botão, command= lambda:inserir_D('+'), text="+", width=6, height=2, bg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=210,y=156)


#linha 5

b_c = Button(frame_botão, command= lambda:inserir_D('0'), text="0", width=13, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_c.place(x=0,y=208) #X é horizontal e y é vertical

b_div = Button(frame_botão, command= lambda:inserir_D('.'), text=".", width=6, height=2, bg=cor3, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE )
b_div.place(x=140,y=208)

b_barr = Button(frame_botão, command= calcular, text="=", width=6, height=2, bg=cor4, font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_barr.place(x=210,y=208)




janela.mainloop()