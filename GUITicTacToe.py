from tkinter import * 
from tkinter import messagebox

class square(Button):
    """
    represents a square in tic-tac-toe
    """ 
    def __init__(self, master, pos):
        self.parent = master
        super().__init__(self.parent,text = "",command=self.clickedPiece,width=20,height=10)
        self.grid(row=pos[0],column=pos[1])

        self.pos = pos 
        self.hasUsed = False
    def clickedPiece(self):
        if self.hasUsed == False:
            self["text"] = self.parent.symbols[self.parent.turn]  
            self["fg"] = self.parent.colorSymbols[self.parent.turn]
            self.hasUsed = True 
            self.parent.board[self.pos[0]][self.pos[1]] = self["text"]
        
            if self.parent.check_win() == 1:
                messagebox.showinfo(title = "tic-tac-toe",message = f"Player {self.parent.symbols[0]} wins!",parent=self.parent.master)
                self.parent.master.destroy()
                self.parent.anyOneWon = True
                return
            elif self.parent.check_win() == 2:
                messagebox.showinfo(title = "tic-tac-toe",message=f"Player {self.parent.symbols[1]} wins!",parent=self.parent.master)
                self.parent.master.destroy()
                self.parent.anyOneWon = True 
                return

            remaningBlank = 9 
            for partBoard in self.parent.board:
                for part in partBoard:
                    if part != "":
                        remaningBlank -= 1 
            if remaningBlank == 0 and not(self.parent.anyOneWon):
                messagebox.showinfo(title="tic-tac-toe",message=f"The game is a draw!",parent=self.parent.master)
                self.parent.master.destroy()
                return 
            
            self.parent.turn = 1 - self.parent.turn 
            self.parent.currentTurnLabel.config(text = f"current player moving: player {self.parent.symbols[self.parent.turn]}")

class gameFrame(Frame):
    """
    represents the whole game board
    """
    def __init__(self,master,symbols,colorForSymbols):
        """
        __init__(Tk,list,list) -> gameFrame
        """
        super().__init__(master)
        self.grid()
        
        self.parent = master 
        self.symbols = symbols 
        self.colorSymbols = colorForSymbols
        self.piece = []
        self.turn = 0
        for row in range(3):
            for col in range(3):
                self.piece.append(square(self,(row,col)))
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.currentTurnLabel = Label(self.master,text=f"current player moving: player {self.symbols[self.turn]}",font=("Times New Roman",20,"bold"))
        self.currentTurnLabel.grid(row=3,columnspan=3)
        self.anyOneWon = False
    def check_win(self):
        """
        check_win() -> int
        returns:
        0 -> nobody won
        1 -> player 1 won
        2 -> player 2 won
        """

        b = self.board

        winning_lines = [
        # rows
        [b[0][0], b[0][1], b[0][2]],
        [b[1][0], b[1][1], b[1][2]],
        [b[2][0], b[2][1], b[2][2]],

        # columns
        [b[0][0], b[1][0], b[2][0]],
        [b[0][1], b[1][1], b[2][1]],
        [b[0][2], b[1][2], b[2][2]],

        # diagonals
        [b[0][0], b[1][1], b[2][2]],
        [b[0][2], b[1][1], b[2][0]]
    ]

        for line in winning_lines:
            if line[0] != "" and line[0] == line[1] == line[2]:
                if line[0] == self.symbols[0]:
                    return 1
                else:
                    return 2
                

        return 0

def play_tic_tac_toe(symbols = ["X","O"],colorForSymbols = ["black","red"]):
    """
    play_tic_tac_toe(symbols)
    """
    newSymbols = symbols[:]
    root = Tk()
    mainGame = gameFrame(root,symbols,colorForSymbols)
    root.mainloop()

firstOne = input("What is the symbol for player 1:\n")
secondOne = input("What is the symbol for player 2:\n")
firstColor = input("What is the color for player 1: \n")
secondColor = input("What is the color for player 2: \n")

play_tic_tac_toe([firstOne,secondOne],[firstColor,secondColor])