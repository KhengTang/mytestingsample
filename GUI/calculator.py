from tkinter import *

window = Tk()

userInput = Entry(window)
userInput.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add():
  return
btn_1 = Button(window, text="1", padx=40, pady=20, command=button_add)
btn_2 = Button(window, text="2", padx=40, pady=20, command=button_add)
btn_3 = Button(window, text="3", padx=40, pady=20, command=button_add)
btn_4 = Button(window, text="4", padx=40, pady=20, command=button_add)
btn_5 = Button(window, text="5", padx=40, pady=20, command=button_add)
btn_6 = Button(window, text="6", padx=40, pady=20, command=button_add)
btn_7 = Button(window, text="7", padx=40, pady=20, command=button_add)
btn_8 = Button(window, text="8", padx=40, pady=20, command=button_add)
btn_9 = Button(window, text="9", padx=40, pady=20, command=button_add)
btn_0 = Button(window, text="0", padx=40, pady=20, command=button_add)

# Put button on screen

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0.grid(row=4, column=0)

window.mainloop()