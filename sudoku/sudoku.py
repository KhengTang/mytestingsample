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
  exist = checkLine(row, col, val)
  if(exist):
    return
  board[row][col] = val
  
def checkLine(row, col, val):
  for i in range(cols):
    if(board[row][i] == val):
      print("Value " + str(val) + " exist in board[" + str(row+1) + "][" + str(i+1) + "]. Please try another cell")
      return True
  
  for i in range(row):
    if(board[i][col] == val):
      print("Value " + str(val) + " exist in board[" + str(i+1) + "][" + str(col+1) + "]. Please try another cell")
      return True  
      
  return False
      
def game():
  printBoard()
  exit, row, col, val = checkInput()
  
  if(exit):
    return
  fillBoard(row-1, col-1, val)
  game()

print("game()")  
choices = input("Enter your choices: ")
eval(choices)