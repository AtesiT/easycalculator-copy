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

frame = Frame(window) #рамка
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, 
                command = lambda: button_press(1) ) #первая кнопка
button1.grid(row=0,column=0) # "сетка" и расположение кнопки

button2 = Button(frame, text=2, height=4, width=9, font=35, 
                command = lambda: button_press(2) ) #вторая кнопка
button2.grid(row=0,column=1) # "сетка" и расположение кнопки

button3 = Button(frame, text=3, height=4, width=9, font=35, 
                command = lambda: button_press(3) ) #третья кнопка
button3.grid(row=0,column=2) # "сетка" и расположение кнопки

button4 = Button(frame, text=4, height=4, width=9, font=35, 
                command = lambda: button_press(4) ) #четвертая кнопка
button4.grid(row=1,column=0) # "сетка" и расположение кнопки

button5 = Button(frame, text=5, height=4, width=9, font=35, 
                command = lambda: button_press(5) ) #пятая кнопка
button5.grid(row=1,column=1) # "сетка" и расположение кнопки

button6 = Button(frame, text=6, height=4, width=9, font=35, 
                command = lambda: button_press(6) ) #шестая кнопка
button6.grid(row=1,column=2) # "сетка" и расположение кнопки

button7 = Button(frame, text=7, height=4, width=9, font=35, 
                command = lambda: button_press(7) ) #седьмая кнопка
button7.grid(row=2,column=0) # "сетка" и расположение кнопки

button8 = Button(frame, text=8, height=4, width=9, font=35, 
                command = lambda: button_press(8) ) #восьмая кнопка
button8.grid(row=2,column=1) # "сетка" и расположение кнопки

button9 = Button(frame, text=9, height=4, width=9, font=35, 
                command = lambda: button_press(9) ) #девятая кнопка
button9.grid(row=2,column=2) # "сетка" и расположение кнопки

button0 = Button(frame, text=0, height=4, width=9, font=35, 
                command = lambda: button_press(0) ) #нулевая-десятая кнопка
button0.grid(row=3,column=0) # "сетка" и расположение кнопки

plus = Button(frame, text='+', height=4, width=9, font=35, 
                command = lambda: button_press('+') ) #плюс кнопка
plus.grid(row=0,column=3) # "сетка" и расположение кнопки

minus = Button(frame, text='-', height=4, width=9, font=35, 
                command = lambda: button_press('-') ) #минус кнопка
minus.grid(row=1,column=3) # "сетка" и расположение кнопки

multiply = Button(frame, text='*', height=4, width=9, font=35, 
                command = lambda: button_press('*') ) #умножить кнопка
multiply.grid(row=2,column=3) # "сетка" и расположение кнопки

divide = Button(frame, text='/', height=4, width=9, font=35, 
                command = lambda: button_press('/') ) #деление кнопка
divide.grid(row=3,column=3) # "сетка" и расположение кнопки

equal = Button(frame, text='=', height=4, width=9, font=35, 
                command = lambda: button_press('=') ) #равно кнопка
equal.grid(row=3,column=2) # "сетка" и расположение кнопки

decimal = Button(frame, text='.', height=4, width=9, font=35, 
                command = lambda: button_press('.') ) #десятичная кнопка
decimal.grid(row=3,column=1) # "сетка" и расположение кнопки

clear = Button(window, text='clear', height=4, width=12, font=35, 
                command = clear ) #очистить кнопка

clear.pack()





window.mainloop() #цикл окна, чтобы дальше код не работал, пока не закроется окно

print('The window was closed by user')