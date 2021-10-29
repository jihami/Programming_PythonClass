class TicTacTocGameEngine:
    def __init__(self):
        self.board=list("."*9)         #[".",".",".",".",".",".",".",".","."]
        self.turn = "X"

    def show_board(self):
        print(self.board)

    def set(self, row, col):
        pass

    def set_winner(self): #우리, 가영이네
        #우리
        #- 3줄
        #| 3줄
        pass

    def change_tuen(self):
        pass
if __name__ == "__main__":
    game_engine = TicTacTocGameEngine()
    game_engine.show_board()
    game_engine.set(2, 2)    # ....\n...\n...
    game_engine.show_board()    #[".",".",".",".",".",".",".",".","."]
    game_engine.set(2, 1)
    game_engine.set(2, 3)
    game_engine.show_board()    #[".",".",".","X","X","X",".",".","."]
    game_engine.board = [".",".",".","X","X","X",".",".","."]
    game_engine.set_winner()    #"-"
    game_engine.change_tuen()
    game_engine.change_tuen()
    print(game_engine.turn)     # "X"