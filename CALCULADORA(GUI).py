from tkinter import *
import math

app = Tk()
app.geometry("500x500")
app.configure(bg = "black")
app.title("Calculadora")


#global expressao
def btn_click(n):
	global expression
	expression = expression + str(n)
	input_text.set(expression)


def btn_limpar():
	global expression
	expression = " "
	input_text.set("")
	
	
	
	
def btn_equal():
 
    global expression
 
    result = str(eval(expression))
    input_text.set(result)
    expression = " "
	 
expression = " "





input_text = StringVar()

title = Message(app, text = "CALCULADORA", font = "Arial 18 italic", width = 1000, fg = "#FFF", bg = "black")
apresentacao = Label(app, textvariable = input_text,
	font = " Arial 10 bold", width = 60, bg = "white", fg = "red", height = 5, justify = LEFT, anchor = W)

title.grid(column = 0, row = 0, padx =(0,450), pady = (60,0))
apresentacao.grid(columnspan = 5, row = 1, stick = "we", pady = (90,40))





button = Frame(app)
#______________________________________________GRID_01____________________________________________________#
btn_clear = Button(button, text = "C", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_limpar())
btn_7 = Button(button, text = "7", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click(7)
)
btn_4 = Button(button, text = "4", font = "Arial 7 bold",  fg = "blue", width = 5, height = 4,
command = lambda: btn_click(4)
)
btn_1 = Button(button, text = "1", font = "Arial 7 bold",  fg = "blue", width = 5, height = 4,
command = lambda: btn_click(1)
)
btn_alt = Button(button, text = "+/-", font = "Arial 7  bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click("-")
)
#______________________________________________GRID_01____________________________________________________#


#______________________________________________GRID_02____________________________________________________#
btn_cochete = Button(button, text = "()", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click("()")
)
btn_8 = Button(button, text = "8", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click(8)
)
btn_5 = Button(button, text = "5", font = "Arial 7 bold",  fg = "blue", width = 5, height = 4,
command = lambda: btn_click(5)
)
btn_2 = Button(button, text = "2", font = "Arial 7 bold",  fg = "blue", width = 5, height = 4,
command = lambda: btn_click(2)
)
btn_0 = Button(button, text = "0", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click(0)
)
#______________________________________________GRID_02____________________________________________________#


#______________________________________________GRID_03____________________________________________________#
btn_porc = Button(button, text = "%", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click("/100")
)
btn_9 = Button(button, text = "9", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click(9)
)
btn_6 = Button(button, text = "6", font = "Arial 7 bold",  fg = "blue", width = 5, height = 4,
command = lambda: btn_click(6)
)
btn_3 = Button(button, text = "3", font = "Arial 7 bold",  fg = "blue", width = 5, height = 4,
command = lambda: btn_click(3)
)
btn_dec = Button(button, text = ",", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click(".")
)
#______________________________________________GRID_03____________________________________________________#



#______________________________________________GRID_04____________________________________________________#
btn_divisao = Button(button, text = "/", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click("/")
)
btn_raiz = Button(button, text = "√", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click("√")
)
btn_sub = Button(button, text = "-", font = "Arial 7 bold",  fg = "blue", width = 5, height = 4,
command = lambda: btn_click("-")
)
btn_sum = Button(button, text = "+", font = "Arial 7 bold",  fg = "blue", width = 5, height = 4,
command = lambda: btn_click("+")
)
btn_multi = Button(button, text = "X", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click("*")
)
#______________________________________________GRID_04____________________________________________________#



#______________________________________________GRID_05____________________________________________________#
btn_pot = Button(button, text = "pot", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click("**")
)

btn_fat = Button(button, text = " π", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,
command = lambda: btn_click("*3.141592"))


btn_pot3 = Button(button, text = "x³", font = "Arial 7 bold",  fg = "blue", width = 5, height = 4,
command = lambda: btn_click("**3")
)


btn_pot6 = Button(button, text = "x⁶", font = "Arial 7 bold",  fg = "blue", width = 5, height = 4,
command = lambda: btn_click("**6")
)

btn_igual = Button(button, text = "=", font = "Arial 7 bold", fg = "blue", width = 5, height = 4,command = lambda: btn_equal())

#______________________________________________GRID_05____________________________________________________#





btn_clear.grid(column = 0, row = 0)
btn_7.grid(column = 0, row = 1)
btn_4.grid(column = 0, row = 2)
btn_1.grid(column = 0, row = 3)
btn_alt.grid(column = 0, row = 4)




btn_cochete.grid(column = 1, row = 0)
btn_8.grid(column = 1, row = 1)
btn_5.grid(column = 1, row = 2)
btn_2.grid(column = 1, row = 3)
btn_0.grid(column = 1, row = 4)





btn_porc.grid(column = 2, row = 0)
btn_9.grid(column = 2, row = 1)
btn_6.grid(column = 2, row = 2)
btn_3.grid(column = 2, row = 3)
btn_dec.grid(column = 2, row = 4)




btn_divisao.grid(column = 3, row = 0)
btn_raiz.grid(column = 3, row = 1)
btn_multi.grid(column = 3, row = 2)
btn_sub.grid(column = 3, row = 3)
btn_sum.grid(column = 3, row = 4)




btn_pot.grid(column = 4, row = 0)
btn_fat.grid(column = 4, row = 1)
btn_pot3.grid(column = 4, row = 2)
btn_pot6.grid(column = 4, row = 3)
btn_igual.grid(column = 4, row = 4)



button.grid(padx = (0,570))


app.mainloop()
