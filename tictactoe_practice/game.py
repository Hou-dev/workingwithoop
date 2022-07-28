from board import Board
from player import Player

class TicTacGame:
    def start(self):
        print("+++++++++++++++++")
        print(" Tic Tac Toe Game")
        print("+++++++++++++++++")
        
        board = Board()
        player = Player()
        computer = Player(False)
        
        board.print_board()
        
        while True:
            while True:
                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()
                
                if board.check_is_tie():
                    print("The game is Tied")
                elif board.check_is_game_over(player, player_move):
                    print("Good job you won")
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()
                    if board.check_is_game_over(computer, computer_move):
                        print("Computer player won")
                        break
            play_again = input("Play again? YES=Y , NO=N").upper()
            if play_again == "N":
                print("Goodbye")
                break
            elif play_again == "Y":
                self.start_new_round(board)
            else:
                print("Invaild input")
                self.start_new_round(board)
                
    def start_new_round(self,board):
        print("================")
        print("    NEW ROUND   ")
        print("================")
        board.reset_board()
        board.print_board()
                
game = TicTacGame()
game.start()