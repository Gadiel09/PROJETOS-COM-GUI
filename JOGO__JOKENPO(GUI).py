from tkinter import *
import time
import random


def TESOURA():
	if btn_tesoura["text"] == "TESOURA":
		 papel = 0
		 tesoura = 1
		 pedra = 2
		 jogadas = [  tesoura, papel, pedra  ]
		 comp = random.choice(jogadas)
		 name_papel = "0"
		 name_tesoura = "1"
		 name_pedra = "2"
		 if tesoura == comp:
		  	name = name_tesoura.replace("1","TESOURA")
		  	response.set(f''' 
EMPATE : [ Computador :  {name} |  Jogador : {btn_tesoura["text"]} ]
		  	''')
		  	result = Label(mensagens, textvariable = response, width = 75, font = "Times 5 bold", 
		  	fg = "white", bg = "red")
		  	result.grid(column = 0, row = 3, padx = (0,0))
		 elif tesoura > (comp == papel):
		  	name = name_papel.replace("0","PAPEL")
		  	response.set(f''' 
JOGADOR GANHOU :  [ Jogador : {btn_tesoura["text"]}  | Computador :  {name} ]
			  ''')
		  	result = Label(mensagens, textvariable = response, width = 75, font = "Times 5 bold", 
		  	fg = "white", bg = "green")
		  	result.grid(column = 0, row = 3, padx = (0,0))
		  	convert_int = int(jogador["text"])
		  	jogador["text"] = str(convert_int + 1)
		 elif tesoura < pedra :
		  	name = name_pedra.replace("2","PEDRA")
		  	response.set(f''' 
COMPUTADOR GANHOU :  [ Computador :  {name} |  Jogador : {btn_tesoura["text"]} ]
			 ''')
		  	result = Label(mensagens, textvariable = response, width = 75, font = "Times 5 bold", 
		  	fg = "white", bg = "orange")
		  	result.grid(column = 0, row = 3, padx = (0,0))
		  	convert_int = int(computador["text"])
		  	computador["text"] = str(convert_int + 1)
		
		

def PAPEL():
	if btn_papel["text"] == "PAPEL":
		 pedra = 0
		 papel = 1
		 tesoura = 2
		 jogadas = [  tesoura, papel, pedra  ]
		 comp = random.choice(jogadas)
		 name_pedra = "0"
		 name_papel = "1"
		 name_tesoura = "2"
		 if papel == comp:
		  	name = name_papel.replace("1","PAPEL")
		  	response.set(f'''
EMPATE [ Computador :  {name} |  Jogador ; {btn_papel["text"]} ]
			  ''')
		  	result = Label(mensagens, textvariable = response, width = 75, font = "Times 5 bold", 
		  	fg = "white", bg = "red", bd = 2, relief = GROOVE)
		  	result.grid(column = 0, row = 3, pady = 0)
		 elif papel > (comp == pedra):
		  	name = name_pedra.replace("0","PEDRA")
		  	response.set(f''' 
JOGADOR GANHOU :  [ Jogador : {btn_papel["text"]} | Computador :  {name} ]
			  ''')
		  	result = Label(mensagens, textvariable = response, width = 75, font = "Times 5 bold", 
		  	fg = "white", bg = "green", bd = 2, relief = GROOVE)
		  	result.grid(column = 0, row = 3, pady = 0)
		  	convert_int = int(jogador["text"])
		  	jogador["text"] = str(convert_int + 1)
		 elif papel < tesoura :
		  	name = name_tesoura.replace("2","TESOURA")
		  	response.set(f'''
COMPUTADOR GANHOU :  [ Computador :  {name} |  Jogador : {btn_papel["text"]} ]
			   ''')
		  	result = Label(mensagens, textvariable = response, width = 75, font = "Times 5 bold", 
		  	fg = "white", bg = "orange", bd = 2, relief = GROOVE)
		  	result.grid(column = 0, row = 3, pady = 0)
		  	convert_int = int(computador["text"])
		  	computador["text"] = str(convert_int + 1)
		 
		 
		 
	 
def PEDRA():
	if btn_pedra["text"] == "PEDRA":
		 tesoura = 0
		 pedra = 1
		 papel = 2
		 jogadas = [  tesoura, papel, pedra  ]
		 comp = random.choice(jogadas)
		 name_tesoura = "0"
		 name_pedra = "1"
		 name_papel = "2"
		 if pedra == comp:
		  	name = name_pedra.replace("1","PEDRA")
		  	response.set(f'''
EMPATE [ Computador :  {name} |  Jogador : {btn_pedra["text"]} ]
			  ''')
		  	result = Label(mensagens, textvariable = response, width = 75, font = "Times 5 bold", 
		  	fg = "white", bg = "red", bd = 2, relief = GROOVE)
		  	result.grid(column = 0, row = 3)
		 elif pedra > (comp == tesoura):
		  	name = name_tesoura.replace("0","TESOURA")
		  	response.set(f'''
JOGADOR GANHOU :  [ Jogador : {btn_pedra["text"]} | Computador :  {name} ]
			   ''')
		  	result = Label(mensagens, textvariable = response, width = 75, font = "Times 5 bold", 
		  	fg = "white", bg = "green", bd = 2, relief = GROOVE)
		  	result.grid(column = 0, row = 3)
		  	convert_int = int(jogador["text"])
		  	jogador["text"] = str(convert_int + 1)
		 elif pedra < papel :
		  	name = name_papel.replace("2","PAPEL")
		  	response.set(f''' 
COMPUTADOR GANHOU :  [ Computador :  {name} |  Jogador : {btn_pedra["text"]} ]
		  	''')
		  	result = Label(mensagens, textvariable = response, width = 75, font = "Times 5 bold", 
		  	fg = "white", bg = "orange", bd = 2, relief = GROOVE)
		  	result.grid(column = 0, row = 3)
		  	convert_int = int(computador["text"])
		  	computador["text"] = str(convert_int + 1)
		  	
		  	
		  	
def Placar():
	placar.grid(column = 0, row = 0)
	jogador.grid(column = 1, row = 0)
	char_x.grid(column = 2, row = 0)
	computador.grid(column = 3, row = 0)
	msg.grid(column = 0, row = 0, pady = (260,0))
			 


		


app = Tk()
app.title("JOKENPO")
app.geometry("600x600")
app.configure(bg = "black")


#_______________________________________________TÍTULO____________________________________________________#
title = Message(app, text = "JOKENPO", font = "Times 18 bold", width = 320, fg = "white", bg="black")
title.grid(columnspan = 3, row  = 0, pady = (0,320))
#_______________________________________________TÍTULO____________________________________________________#





#_______________________________________________PLACAR____________________________________________________#
msg = Frame(app)
msg.configure(bd = 4, relief = GROOVE,width = 100)
placar = Label(msg, text ="PLACAR : ", bg ="black", fg = "white", font = "Times 14 bold", height = 3 
,width = 10)
jogador = Label(msg, text = "0",  bg ="black", fg = "white", font = "Times 14 bold", height = 3 
,width = 2)
char_x =Label(msg, text = "X"  ,  bg ="black", fg = "white", font = "Times 14 bold", height = 3 
,width = 2)
computador =Label(msg, text = "0   ", bg ="black", fg = "white", font = "Times 14 bold", height = 3 
,width = 2)
Placar()
#_______________________________________________PLACAR____________________________________________________#





#_______________________________________________BOTÕES____________________________________________________#
buttons = Frame(app)
btn_pedra = Button(buttons, text = "PEDRA", font = "Times 10 bold", bd = 6, relief = GROOVE, height = 3, command =PEDRA, activeforeground = "blue")
btn_papel = Button(buttons, text = "PAPEL", font = "Times 10 bold", bd = 6, relief = GROOVE, height = 3, command =PAPEL, activeforeground = "blue")
btn_tesoura = Button(buttons, text = "TESOURA", font = "Times 10 bold", bd = 6, relief = GROOVE, height = 3, command =TESOURA, activeforeground = "blue")
btn_pedra.grid(column = 0, row = 0)
btn_papel.grid(column = 1, row = 0)
btn_tesoura.grid(column = 2, row = 0)
buttons.grid(pady = (120,40), padx= (20,60))
#_______________________________________________BOTÕES____________________________________________________#






#____________________________________________MENSAGENS_________________________________________________#
response = StringVar()
mensagens = Frame(app)
mensagens.configure(bd = 1, relief = GROOVE, bg = "white")
mensagens.grid()
#____________________________________________MENSAGENS_________________________________________________#







#________________________________________________FOOTER___________________________________________________#
foo= Frame(app)
foo.configure(bg = "black")
text = Message(app, text = " DESENVOLVIDO POR GADIEL", font = "Times 4 italic", width = 420, bg = "black", fg = "white")
text.grid(pady = 370, padx = (0,70))
foo.grid()
#________________________________________________FOOTER___________________________________________________#




app.mainloop()
