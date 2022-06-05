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
  [0, 0, 8, 0, 6, 1, 0, 7, 0],
]

def solve(board):
  empty = empty_pos(board)
  if not empty:
    return True
  else:
    row, col = empty

  for i in range(1, 10):
    if valid_number(board, i, (row, col)):
      board[row][col] = i

      if solve(board):
        return True

      board[row][col] = 0

def valid_number(board, num, pos):
  # check the row
  for i in range(len(board[0])):
    if board[pos[0]][i] == num and pos[1] != i:
      return False

  # check the column
  for i in range(len(board)):
    if board[i][pos[1]] == num and pos[0] != i:
      return False

  box_x = pos[1] // 3
  box_y = pos[0] // 3

  for i in range(box_y * 3, box_y + 3):
    for j in range(box_x * 3, box_x + 3):
      if board[i][j] == num and (i, j) != pos:
        return False

  return True

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

def empty_pos(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        # returns (row, col)
        return (i, j)

  return None


def main():
  print_board(board)
  print('=' * 50)
  solve(board)
  print_board(board)

if __name__ == '__main__':
  main()
  