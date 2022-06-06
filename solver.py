# this is going to be my sudoku solver
board = [
  [0, 0, 9, 0, 0, 5, 3, 0, 2],
  [0, 2, 3, 6, 9, 0, 7, 5, 4],
  [4, 0, 7, 0, 1, 2, 0, 9, 0],
  [3, 0, 2, 0, 0, 9, 4, 0, 0],
  [0, 0, 4, 1, 3, 6, 0, 8, 0],
  [0, 8, 5, 0, 0, 4, 9, 0, 1],
  [0, 3, 0, 9, 2, 0, 6, 0, 0],
  [0, 0, 6, 5, 0, 3, 0, 0, 0],
  [0, 0, 8, 0, 6, 1, 0, 7, 0]
]

def solve(board):

  # finds the empty spot
  empty = empty_pos(board)
  # board is full
  if not empty:
    return True
  else:
    # unpack tuple to get row and col values
    row, col = empty

  # for loop to test each number from 1-9
  for i in range(1, 10):
    if valid_number(board, i, (row, col)):
      board[row][col] = i

      # recurse so we test all numbers while backtracking as well
      if solve(board):
        return True

      # back tracking
      board[row][col] = 0

def valid_number(board, num, pos):
  
  # check the row if the number can work
  for i in range(len(board[0])):
    if board[pos[0]][i] == num and pos[1] != i:
      return False

  # check the column if the number can work
  for i in range(len(board)):
    if board[i][pos[1]] == num and pos[0] != i:
      return False

  # find which 3x3 grid we need to go to
  box_x = pos[1] // 3
  box_y = pos[0] // 3

  # checking if the num there can't work
  for i in range(box_y * 3, box_y + 3):
    for j in range(box_x * 3, box_x + 3):
      if board[i][j] == num and (i, j) != pos:
        return False

  return True

# prints the board in a sudoku board looking fashion
def print_board(board):
  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      print("- " * 12)

    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        print(" | ", end="")

      if j == 8:
        print(board[i][j])
      else:
        print(str(board[i][j]) + " ", end='')

# finds an empty position and returns that as a tuple (row, col)
def empty_pos(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        return (i, j)

  return None

# main function calling all functions
def main():
  print_board(board)
  print('=' * 50)
  solve(board)
  print_board(board)
  print('Solved')

# run main
if __name__ == '__main__':
  main()
  
