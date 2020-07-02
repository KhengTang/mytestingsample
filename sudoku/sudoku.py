rows, cols = 9, 9
board = [[0 for i in range(cols)] for j in range(rows)]

def printBoard():
  for i in range(rows):
    for j in range(cols):
      if (j == 3 or j == 6):
        print("|"),
      print(board[i][j]),
    if (i == 2 or i == 5):
      print("")
      print("______________________"),
    print("")

def game():
  printBoard()
  print("Enter -1 to exit")
  row = input("Enter row: ")
  col = input("Enter col: ")
  val = input("Enter val: ")
  
  if(row == -1 or col == -1 or val == -1):
    return
  
  board[row+1][col+1] = val
  game()

print("game()")  
choices = input("Enter your choices: ")
