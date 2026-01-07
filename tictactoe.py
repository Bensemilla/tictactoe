import random
import time

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    sq_1 = board[0][0]
    sq_2 = board[1][0]
    sq_3 = board[2][0]
    sq_4 = board[0][1]
    sq_5 = board[1][1]
    sq_6 = board[2][1]
    sq_7 = board[0][2]
    sq_8 = board[1][2]
    sq_9 = board[2][2]
 
    print(' +-------+-------+-------+\n',
          '|       |       |       |\n',
          f'|   {sq_1}   |   {sq_2}   |   {sq_3}   |\n',
          '|       |       |       |\n',
          '+-------+-------+-------+\n',
          '|       |       |       |\n',
          f'|   {sq_4}   |   {sq_5}   |   {sq_6}   |\n',
          '|       |       |       |\n',
          '+-------+-------+-------+\n',
          '|       |       |       |\n',
          f'|   {sq_7}   |   {sq_8}   |   {sq_9}   |\n',
          '|       |       |       |\n',
          '+-------+-------+-------+\n')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move_coords = 0
            player_move = int(input("Please choose the field you want to play: "))

            if player_move not in range(0,10):
                print("Please choose a number thats on the board!")
                continue

            else:
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == player_move:
                            move_coords = (i, j)
                        else:
                            continue
            
            if move_coords in free_moves:
                board[move_coords[0]][move_coords[1]] = 'O'
                break

            else:
                print("Field not available anymore!")
            
        except ValueError:
            print("This is not a number, please choose a valid number!")
            

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free_moves
    free_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'X' or board[i][j] == 'O':
                continue
            else:
                free_moves.append((i,j))

    if not free_moves:
        print("It's a tie!")
        return False

    return True


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    winning_conditions = [[(0,0),(1,1),(2,2)],
                          [(2,0),(1,1),(0,2)],
                          [(0,0),(1,0),(2,0)],
                          [(0,1),(1,1),(2,1)],
                          [(0,2),(1,2),(2,2)],
                          [(0,0),(0,1),(0,2)],
                          [(1,0),(1,1),(1,2)],
                          [(2,0),(2,1),(2,2)]]
    victory_list = []
      
    for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == sign:
                    victory_list.append((i, j))

    for i in range(len(winning_conditions)):
        if set(winning_conditions[i]).issubset(set(victory_list)):
            print(f"We have a winner, its {sign}!!!")
            return False

    return True


def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        
        if board[1][1] == 5:
            board[1][1] = 'X'
            break

        move_coords = 0
        comp_move = random.randrange(1,10)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == comp_move:
                    move_coords = (i, j)
                else:
                    continue
        
        if move_coords in free_moves:
            board[move_coords[0]][move_coords[1]] = 'X'
            break
    




def main():
    
    #Initializing the base board:
    

    board = [[1,4,7],[2,5,8],[3,6,9]]

    global no_victor
    no_victor = True


    #Initializing game:
    

    display_board(board)

    game_status =input("This is the board and the computer has the first move,\n"
                        "are you ready to begin? Type 'y' to start, or 'n' to cancel: ")

    if game_status == 'y':

        while no_victor:
        
            no_victor = make_list_of_free_fields(board)

            draw_move(board)
            print("Computer is thinking....")
            time.sleep(1)
            display_board(board)
            no_victor = victory_for(board, 'X')

            if no_victor == False:
                break

            no_victor = make_list_of_free_fields(board)
            if no_victor == False:
                break

            enter_move(board)
            display_board(board)
            no_victor = victory_for(board, 'O')
            

        
if __name__ == '__main__':
    main()
