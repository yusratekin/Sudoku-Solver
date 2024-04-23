# Sudoku game board
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Function to print the board to the screen
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Recursive function to solve the Sudoku board
def solve_board(board):
    # Check if the board is full
    empty_pos = find_empty(board)
    if not empty_pos:
        return True
    else:
        row, col = empty_pos

    # Try numbers for the empty cell
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve_board(board):
                return True
            board[row][col] = 0

    return False

# Function to check if a number can be placed in a specific cell
def is_valid(board, num, pos):
    # Check if the same number exists in the same row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check if the same number exists in the same column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check if the same number exists in the same 3x3 box
    box_row = pos[0] // 3
    box_col = pos[1] // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

# Function to find an empty cell
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Row, Column
    return None

# Print the board
print_board(board)
print("\n")
# Solve the board
solve_board(board)
print_board(board)
