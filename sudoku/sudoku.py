rows, cols = 9, 9
board = [[0 for i in range(cols)] for j in range(rows)]

def printBoard():
  print("")
  for i in range(rows):
    for j in range(cols):
      if (j == 3 or j == 6):
        print("|", end = ''),
      print(board[i][j], end = ''),
    if (i == 2 or i == 5):
      print("")
      print("______________________"),
    print("")
    
def checkInput():
  print("")
  print("Enter -1 to exit")
  row = int(input("Enter row: "))
  if(row == -1):
    return True, 0, 0, 0
  col = int(input("Enter col: "))
  if(col == -1):
    return True, 0, 0, 0
  val = int(input("Enter val: "))
  if(val == -1):
    return True, 0, 0, 0
  
  return False, row, col, val
  
def fillBoard(row, col, val):
  exist = checkInvalidMove(row, col, val)
  if(exist):
    return
  board[row][col] = val
  
def checkInvalidMove(row, col, val):
  if(val == 0):
    return False
  for i in range(cols):
    if(board[row][i] == val):
      print("Value " + str(val) + " exist in board[" + str(row+1) + "][" + str(i+1) + "]. Please try another cell")
      return True
  
  for i in range(rows):
    if(board[i][col] == val):
      print("Value " + str(val) + " exist in board[" + str(i+1) + "][" + str(col+1) + "]. Please try another cell")
      return True
      
  boxR = row // 3 * 3
  boxC = col // 3 * 3
  for i in range(3):
    for j in range(3):
      if(board[i+boxR][j+boxC] == val):
        print("Value " + str(val) + " exist in board[" + str(i+boxR+1) + "][" + str(j+boxC+1) + "]. Please try another cell")
        return True
      
  return False
      
def sudoku():
  printBoard()
  exit, row, col, val = checkInput()
  
  if(exit):
    return
  fillBoard(row-1, col-1, val)
  sudoku()
  
def solve():
  return
  
def quit():
  return

print("sudoku")
print("solve")
print("quit")
choices = input("Enter your choices: ")
eval(choices+"()")