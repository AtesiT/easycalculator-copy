from tkinter import *

def button_press(num):
    pass

def equals():
    pass

def clear():
    pass

window = Tk() #Вывод оконного интерфейса
window.title('My calculator') #Заголовок
window.geometry('500x500') #Размер окна

equation_text = ""

equation_label = StringVar() #Строка 

label = Label(window,  textvariable = equation_label, font=('consolas', 20), bg='white', width=24, height=2) #окно,  , #шрифт, #задний фон, #ширина, #длина, 
label.pack()

window.mainloop() #цикл окна, чтобы дальше код не работал, пока не закроется окно

print('The window was closed by user')