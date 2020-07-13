from tkinter import *
from tkinter.ttk import Separator, Style

rows, cols = 9, 9
board = [[0 for i in range(cols)] for j in range(rows)]

window = Tk()
window.title("Sudoku")

def start():
  boardBtn[2][1]['text'] = str(5)
  return

def solve():
  done, row, col = complete()
  
  if(done):
    return True
  
  for k in range(1, 10):
    if(not checkInvalidMove(row, col, str(k))):
      board[row][col]['text'] = str(k)
      board[row][col]['bg'] = 'green'
      
      if(solve()):
        return True
    
      board[row][col]['text'] = str(0)
  
  return False
  
def complete():
  for i in range(rows):
    for j in range(cols):
      if(board[i][j]['text'] == str(0)):
        return False, i, j
  
  return True, i, j
  
def checkInvalidMove(row, col, val):
  if(val == 0):
    return False
  for i in range(cols):
    if(board[row][i]['text'] == val):
      print("Value " + str(val) + " exist in board[" + str(row+1) + "][" + str(i+1) + "]. Please try another cell")
      return True
  
  for i in range(rows):
    if(board[i][col]['text'] == val):
      print("Value " + str(val) + " exist in board[" + str(i+1) + "][" + str(col+1) + "]. Please try another cell")
      return True
      
  boxR = row // 3 * 3
  boxC = col // 3 * 3
  for i in range(3):
    for j in range(3):
      if(board[i+boxR][j+boxC]['text'] == val):
        print("Value " + str(val) + " exist in board[" + str(i+boxR+1) + "][" + str(j+boxC+1) + "]. Please try another cell")
        return True
      
  return False
  
def close(r,c,v):
  if (checkInvalidMove(r,c,str(v))):
    board[r][c]['bg'] = 'red'
  else:
    board[r][c]['bg'] = 'green'
  board[r][c]['text'] = str(v)
  window.newWindow.destroy()

def button_click(r,c):
  window.newWindow = Toplevel(window)
  l = Label(window.newWindow, text="Value")
  input = Entry(window.newWindow)
  buttonExample = Button(window.newWindow, text = "Ok", command=lambda: close(r,c,input.get()))
  l.pack()
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
    board[i][j] = Button(window, text=str(board[i][j]), bg = 'white', padx=10, pady=10, command=lambda i=i,j=j: button_click(i,j))

for i in range(rows):
  for j in range(cols):
    board[i][j].grid(row=i+1, column=j)

window.mainloop()