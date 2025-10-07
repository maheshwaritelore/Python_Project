
ROWS = 6
COLUMNS = 7
EMPTY = " "


RED = '●'    
YELLOW = '●' 

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]


def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("  " + "   ".join(map(str, range(1, COLUMNS + 1))))


def drop_piece(board, column, piece):
    for row in reversed(board):
        if row[column] == EMPTY:
            row[column] = piece
            return True
    return False


def check_win(board, piece):
    
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == piece and all(board[row][col + i] == piece for i in range(4)):
                return True

    
    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if board[row][col] == piece and all(board[row + i][col] == piece for i in range(4)):
                return True

    
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if board[row][col] == piece and all(board[row + i][col + i] == piece for i in range(4)):
                return True

   
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == piece and all(board[row - i][col + i] == piece for i in range(4)):
                return True

    return False


def play_game():
    board = create_board()
    turn = 0
    pieces = [RED, YELLOW] 
    
    while True:
        print_board(board)
        player = turn % 2
        piece = pieces[player]
        print(f"Player {player + 1}'s turn ({piece}).")

       
        try:
            column = int(input(f"Player {player + 1}, choose a column (1-{COLUMNS}): ")) - 1
            if column < 0 or column >= COLUMNS or not drop_piece(board, column, piece):
                raise ValueError
        except ValueError:
            print("Invalid move, try again.")
            continue

        
        if check_win(board, piece):
            print_board(board)
            print(f"Player {player + 1} ({piece}) wins!")
            break

        
        if all(row[0] != EMPTY for row in board):  
            print_board(board)
            print("The game is a draw!")
            break

        
        turn += 1

play_game()
