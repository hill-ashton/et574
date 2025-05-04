# Connect 4 Game

class Connect4:
  def __init__(self):
    self.board = [[' ' for _ in range(7)] for _ in range(6)]
    self.current_player = 'X'

  def switch_player(self):
    self.current_player = 'O' if self.current_player == 'X' else 'X'

  def print_board(self):
    for row in self.board:
      print('|', end='')
      for cell in row:
        print(cell, end='|')
      print()
    print('---------------')
    print(' 1 2 3 4 5 6 7')


  """
  REPLACE THE SKELETON METHOD drop_chip() WITH YOUR OWN HERE. AFTER THIS IS DONE RUN THE PROGRAM TO MAKE SURE YOUR drop_chip()
  WORKS AS EXPECTED.
  """
  def drop_chip(self, column):
    """
    Drops a chip into the selected column of the Connect 4 board.

    Args:
      column (int): The column number where the chip is to be dropped. It must be between 1 and 7.

    Returns:
      bool: True if the chip was successfully dropped, False if the column is full or if the column is out of range.
    """
    #input validation
    if(column<1 or column>7):
      return False
    
    #Question: what indicates the column is full?
    #If the while loop iterates through all rows and does not find ' ', this means the column is full.

    #finding empty slots
    index = column - 1
    row = 5
    while row >=0:
      if self.board[row][index] == ' ':
        #dropping the chip & returning result
        self.board[row][index] = self.current_player
        return True 
      row -= 1
    return False


  def check_win(self, player):
    """
    Check if the specified player has won the game.

    Args:
      player (str): The player to check for a win. It can be either 'X' or 'O'.

    Returns:
      bool: True if the player has won, False otherwise.
    """
    # Check horizontal


    # Check vertical


    # Check diagonal (top-left to bottom-right)


    # Check diagonal (bottom-left to top-right)


    return False

  def play_game(self):
    game_over = False
    while not game_over:
      self.print_board()
      print(f"Player {self.current_player}'s turn.")

      try:
        column = int(input("Enter the column number (1-7): "))
      except ValueError:
        print("Invalid input. Please enter a valid column number.")
        continue

      if not self.drop_chip(column):
        print("Column is full or out of range. Try again.")
        continue

      if self.check_win(self.current_player):
        self.print_board()
        print(f"Player {self.current_player} wins!")
        game_over = True

      self.switch_player()

if __name__ == "__main__":
  game = Connect4()
  game.play_game()
