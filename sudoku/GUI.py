from tkinter import *
from tkinter.ttk import Separator, Style

rows, cols = 9, 9
board = [[0 for i in range(cols)] for j in range(rows)]

window = Tk()
window.title("Sudoku")

def start():
  return

def solve():
  return
  
def close(r,c,v):
  board[r][c] = v
  window.newWindow.destroy()

def button_click(r,c):
  window.newWindow = Toplevel(window)
  input = Entry(window.newWindow)
  buttonExample = Button(window.newWindow, text = "Fill", command=lambda: close(r,c,input))

  input.pack()
  buttonExample.pack()
  
myCanvas = Canvas(window, width=500, height=500, background='black')
myCanvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)
  
button_start = Button(window, text="Start", padx=30, pady=10, command=start)
button_solve = Button(window, text="Solve", padx=30, pady=10, command=solve)
button_quit = Button(window, text="Quit", padx=30, pady=10, command=window.destroy)

button_start.grid(row=0, column=0, columnspan=3)
button_solve.grid(row=0, column=3, columnspan=3)
button_quit.grid(row=0, column=6, columnspan=3)

for i in range(rows):
  for j in range(cols):
    board[i][j] = Button(window, text=str(board[i][j]), padx=10, pady=10, command=lambda: button_click(i,j))

for i in range(rows):
  for j in range(cols):
    board[i][j].grid(row=i+1, column=j)

window.mainloop()