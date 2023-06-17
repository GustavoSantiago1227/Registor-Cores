# Importações

# tkinter para a interface
from tkinter import *

#Configuração da tela

root = Tk() #Cria tela
root.geometry("350x250") #dimenções w,h
root.title("Registores") #Titulo

#Titulo
txt = Label(root, text="Registor")
txt.pack()


#Canvas - Desenhando um registor

#um canvas com w,h definidos e backgroud branco
canvas = Canvas(root, width=350, height=100, bg="#fff")

#Contorno do registor
#create_line cria pontos seguindo X0,Y0; X1,Y1;Xn,Yn
contorno = canvas.create_line(10, 48, 10, 52, 50, 52, 50, 80, 290, 80,
                                290, 52, 340, 52, 340, 48, 290, 48, 290, 20,
                              50, 20, 50, 48, 10, 48)

#Criação dos quadrados para a marcação das cores

#create_rectangle cria retangulos usando as cordenadas X0,Y0 como pontos (0,0)
# e X1,Y1 como pontos finais (obs, não é a dimensão W,H)

rect1 = canvas.create_rectangle(65, 20, 75, 80, fill='#000') #Inicias na posição 65,20 termina na 75,80 cor preta
rect2 = canvas.create_rectangle(85, 20, 95, 80, fill='#000')
rect3 = canvas.create_rectangle(105, 20, 115, 80, fill='#000')
rect4 = canvas.create_rectangle(150, 20, 165, 80, fill='#000')
canvas.pack() #Desenhar Canvas na tela



#globais
valor_registor = [0, 0, 0, 0]  # Cada zero é referente a um botão em sequencia
valor_completo = 0

#Funções
#Para não repetir código
def cor(titulo, botao):
    top = Toplevel(root)
    top.title(titulo)

   #Listas

    # Cores que serão utilizadas
    lista_cores = [
        "000",
        "6B350F",
        "A61C00",
        "FF6E00",
        "FAD501",
        "309412",
        "002FFA",
        "580C87",
        "8C8481",
        "FFF",
    ]

    #Botões
    lista_botoes = [primeiro, segundo, muiltiplicador] #0,1,2

    #Retangulos
    lista_rect = [rect1, rect2, rect3] #0,1,2

    #Radios para cores

    #cada Radio button recebe a janela, o texto de exibição, comando quando cliclado sobre, e a variavel
    #que guardará seus dados e seu valor

    var = IntVar() #guardar valor
    var.set(0) #setar valor

    #Fução chamada quando clicada sobre um button
    def mudar():

        #verificar qual botão foi selecionado
        for c, mudar_botao in enumerate(lista_botoes):
            if c == botao:

                #Cor escolida na var
                cor_escolida = lista_cores[var.get()]

                #Cores que não combinam com as letras brancas
                cor_letra = "#fff"
                for cor_preta in [4, 5, 8, 9]:
                    if var.get() == cor_preta:
                        cor_letra = "#000"

                #Mudar cor de Botão e retangulo
                mudar_botao.configure(bg=f"#{cor_escolida}", fg=f"{cor_letra}")
                canvas.itemconfig(lista_rect[c], fill=f"#{lista_cores[var.get()]}")

                #mudar texto
                valor_registor[c] = var.get() #Mudar valor de acordo com o selecionado

                #Primeiro e segundo valor significativo e multiplicador
                val_1 = valor_registor[0]
                val_2 = valor_registor[1]
                zero = ''

                for c in range(valor_registor[2]): #Juntar os valores e o multiplicador
                    zero += '0'
                valor_completo = int(f'{val_1}{val_2}{zero}')

                #Verificar Qual a notação cientifica através da base 10
                if valor_completo >= 10 ** 9:
                    valor_completo = f'{valor_completo / 10 ** 9}G'

                elif valor_completo >= 10**6:
                    valor_completo = f'{valor_completo / 10**6}M'

                elif valor_completo >= 10**3:
                    valor_completo = f'{valor_completo / 10**3}K'


                #Verificar Tolerancia
                if valor_registor[3] == 0:
                    valor_tolerancia = 1

                elif valor_registor[3] == 1:
                    valor_tolerancia = 5

                elif valor_registor[3] == 2:
                    valor_tolerancia = 10

                #Imprimir Texto
                txt['text'] = f'Registor: {valor_completo} {valor_tolerancia:02d}%'

        top.destroy()







    #Cores
    p = Radiobutton(top, text="Preto", command=mudar, variable=var, value=0)
    m = Radiobutton(top, text="Marron", command=mudar, variable=var, value=1)
    v = Radiobutton(top, text="Vermelho", command=mudar, variable=var, value=2)
    l = Radiobutton(top, text="Laranja", command=mudar, variable=var, value=3)
    a = Radiobutton(top, text="Amarelo", command=mudar, variable=var, value=4)
    v1 = Radiobutton(top, text="Verde", command=mudar, variable=var, value=5)
    a1 = Radiobutton(top, text="Azul", command=mudar, variable=var, value=6)
    r = Radiobutton(top, text="Roxo", command=mudar, variable=var, value=7)
    c = Radiobutton(top, text="Cinza", command=mudar, variable=var, value=8)
    b = Radiobutton(top, text="Branco", command=mudar, variable=var, value=9)

    #Exibir
    p.pack()
    m.pack()
    v.pack()
    l.pack()
    a.pack()
    v1.pack()
    a1.pack()
    r.pack()
    c.pack()
    b.pack()







#Ativava no botão
def fun_primeiro():
    cor("Primeiro", 0)

def fun_segundo():
    cor("Segundo", 1)

def multiplicador():
    cor("Multiplicador", 2)

def tolerancia():
    top = Toplevel(root)
    top.title("Tolerância")
    var = IntVar()
    var.set(0)

    def mudar():

        #Cores que serão utilizadas
        lista_cores = [
            "6B350F",
            "FFAA03",
            "8C8481",
        ]

        #Cor que fica ruim com preto
        cor_letra = "#000"
        if var.get() == 0:
            cor_letra = "#FFF"

        #Trocar cores do botão e do quadrado
        tolerancia.configure(bg=f"#{lista_cores[var.get()]}", fg= cor_letra)
        canvas.itemconfig(rect4, fill=f"#{lista_cores[var.get()]}")

        #validar Tolerancia
        valor_registor[3] = var.get()
        if valor_registor[3] == 0:
            valor_tolerancia = 1

        elif valor_registor[3] == 1:
            valor_tolerancia = 5

        elif valor_registor[3] == 2:
            valor_tolerancia = 10

        #Imprimir texto
        if txt['text'] != 'Registor':
            txt['text'] = f"{txt['text'][:-3].strip()} {valor_tolerancia:02d}%"

        top.destroy()

    #Tolerancias Radio
    m = Radiobutton(top, text="Marron", command=mudar, variable=var, value=0)
    d = Radiobutton(top, text="Dourado", command=mudar, variable=var, value=1)
    c = Radiobutton(top, text="Cinza", command=mudar, variable=var, value=2)

    m.pack()
    d.pack()
    c.pack()






#Conjunto dos botões
frame = Frame(root) #Uma divisaão na tela que agrupará tudo que está inserido dentro dela
primeiro = Button(frame, text="1° Significativo", command=fun_primeiro, bg="#000", fg="#fff")
segundo = Button(frame, command=fun_segundo, text='2° Significativo', bg="#000", fg="#fff")
muiltiplicador = Button(frame, command=multiplicador, text='Multiplicador', bg="#000", fg="#fff")
tolerancia = Button(frame, command=tolerancia, text='Tolerância', bg="#000", fg="#fff")

frame.pack()
primeiro.pack(side=LEFT) #Alinhamento para a esquerda
segundo.pack(side=LEFT)
muiltiplicador.pack(side=LEFT)
tolerancia.pack(side=LEFT)


#Loop
root.mainloop() #loop para tela não fechar