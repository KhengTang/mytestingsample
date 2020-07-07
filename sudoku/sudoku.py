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
    
def checkInput(usrStr, min):
  while(True):
    try:
      val = int(input("Enter " + usrStr + " between " + str(min+1) + " - 9: "))
      if(min == -1):
        min = -2
    except ValueError:
      print("Please enter a valid integer")
      continue
    if (val == min or val < -1 or val > 9):
      print("Please enter a valid " + usrStr)
      continue
    else:
      break
  
  return val
    
def userInput():
  print("")
  print("Enter -1 to go to menu")
  
  row = checkInput("row", 0)
  if(row == -1):
    return True, 0, 0, 0
  col = checkInput("col", 0)
  if(col == -1):
    return True, 0, 0, 0
  val = checkInput("val", -1)
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
  exit, row, col, val = userInput()
  
  if(exit):
    return menu()
  
  fillBoard(row-1, col-1, val)
  
  if(complete()):
    print("Sudoku complete")
  
  sudoku()
  
def complete():
  for i in range(rows):
    for j in range(cols):
      if(board[i][j] == 0):
        return False, i, j
  
  return True, i, j
  
def solve():
  done, row, col = complete()
  
  if(done):
    printBoard()
    return True
  
  for k in range(1, 10):
    if(not checkInvalidMove(row, col, k)):
      board[row][col] = k
      
      if(solve()):
        return True
    
      board[row][col] = 0
  
  return False
  
def quit():
  return
  
def menu():
  print("sudoku")
  print("solve")
  print("quit")
  choices = input("Enter your choices: ")
  choices = choices.lower()
  
  while choices not in {"sudoku", "solve", "quit"}:
    print("Please enter only from the choices below:")
    print("sudoku")
    print("solve")
    print("quit")
    choices = input("Enter your choices: ")
    choices = choices.lower()

  eval(choices+"()")

menu()
