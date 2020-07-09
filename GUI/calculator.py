from tkinter import *

historyStr = []

window = Tk()

inputHistory = Label(window, text='')
inputHistory.grid(row=0, column=0, columnspan=3, padx=10)

userInput = Entry(window)
userInput.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
  #userInput.delete(0, END)
  curr = userInput.get()
  userInput.delete(0, END)
  userInput.insert(0, str(curr) + str(number))
  
def button_clear():
  userInput.delete(0, END)
  global historyStr
  historyStr.clear()
  inputHistory.destroy()
  
def button_sign(logic):
  first = userInput.get()
  global f_num
  global math
  global historyStr
  sign = ""
  if logic == "add":
    math = "add"
    sign = " + "
  if logic == "sub":
    math = "sub"
    sign = " - "
  if logic == "mul":
    math = "mul"
    sign = " * "
  if logic == "div":
    math = "div"
    sign = " / "
  f_num = int(first)
  historyStr.append(first + sign)
  inputHistory = Label(window, text=''.join(map(str, historyStr)))
  inputHistory.grid(row=0, column=0, columnspan=3, padx=10)
  userInput.delete(0, END)
  
def button_equal():
  second = userInput.get()
  userInput.delete(0, END)
  
  if math == "add":
    userInput.insert(0, f_num + int(second))
  if math == "sub":
    userInput.insert(0, f_num - int(second))
  if math == "mul":
    userInput.insert(0, f_num * int(second))
  if math == "div":
    userInput.insert(0, f_num / int(second))
  
btn_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
btn_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
btn_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
btn_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
btn_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
btn_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
btn_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
btn_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
btn_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
btn_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
btn_add = Button(window, text="+", padx=39, pady=20, command=lambda: button_sign("add"))
btn_equal = Button(window, text="=", padx=91, pady=20, command=button_equal)
btn_clear = Button(window, text="Clear", padx=79, pady=20, command=button_clear)
btn_subtract = Button(window, text="-", padx=40, pady=20, command=lambda: button_sign("sub"))
btn_multiply = Button(window, text="*", padx=40, pady=20, command=lambda: button_sign("mul"))
btn_divide = Button(window, text="/", padx=40, pady=20, command=lambda: button_sign("div"))
# Put button on screen

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)

btn_0.grid(row=5, column=0)
btn_clear.grid(row=5,column=1, columnspan=2)
btn_add.grid(row=6,column=0)
btn_equal.grid(row=6,column=1, columnspan=2)

btn_subtract.grid(row=7,column=0)
btn_multiply.grid(row=7,column=1)
btn_divide.grid(row=7,column=2)

window.mainloop()