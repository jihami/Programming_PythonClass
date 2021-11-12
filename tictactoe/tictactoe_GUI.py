import tkinter
from tkinter import messagebox

from tictactoe_gameengine import TictactoeGameEngine


class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root=tkinter.Tk()
        self.root.title("틱택토")
        self.root.geometry(f"{self.CANVAS_SIZE}x{self.CANVAS_SIZE}")
        self.root.resizable(width=False, height=False) #창 크기 변경 x

        self.canvas = tkinter.Canvas(self.root, bg="white", width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)
        self.canvas.pack()

        self.images = {}        #{"X":PhotoImage객체, "O":PhotoImage객체}
        self.images["X"] = tkinter.PhotoImage(file="X.gif")
        self.images["O"] = tkinter.PhotoImage(file="O.gif")

        self.canvas.bind("<Button-1>", self.click_handler) #self.click_handler() 를 쓰면 클릭 안되도 실행 -> 시험

        self.root.mainloop()

    def click_handler(self, event):
        row, col = self.coordinate_to_position(event.x, event.y)
        # set row, col
        self.game_engine.set(row,col)
        # show board
        self.game_engine.show_board()
        self.draw_board()
        # set winner
        winner = self.game_engine.set_winner()
        # 승자가 있거나 무승부면, 게임오버, 결과표시
        if winner == "O" or winner == "X":
            messagebox.showinfo("Game ovr",f"{winner} win")
            self.root.quit()
        elif winner == "d":
            messagebox.showinfo("Game ovr",f"무승부")
            self.root.quit()
        # chang_turn
        self.game_engine.change_turn()

    def draw_board(self):
        TILE_SIXE = self.CANVAS_SIZE // self.game_engine.SIZE #300//3 = 100
        x = 0
        y = 0
        for i,v in enumerate(self.game_engine.board):
            if v == ".":
                pass
            else:   #elif v == "X" or V == "O";
                self.canvas.create_image(x,y,anchor="nw", image=self.images[v])
            x += TILE_SIXE
            if i % self.game_engine.SIZE == self.game_engine.SIZE - 1 :
                x = 0
                y += TILE_SIXE

    def coordinate_to_position(self, x, y):
        row = y // (self.CANVAS_SIZE//self.game_engine.SIZE) + 1
        col = x // (self.CANVAS_SIZE//self.game_engine.SIZE) + 1
        return row, col


if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()