from random import randrange

def display_board(board):

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


#def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


#def draw_move(board):
    # The function draws the computer's move and updates the board.

def main():

    
    board = [[1,4,7],[2,5,8],[3,6,9]]

    display_board(board)
















if __name__ == '__main__':
    main()
