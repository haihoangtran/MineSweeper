import sys
sys.path.append('code/src')
from GameController import *
import random
from Tkinter import *

root = Tk()
buttonArray ={}

class Board():                
        
    def leftClick(self,event,gameController):
        global buttonArray
        brow =  buttonArray[event.widget]/10
        bcolumn = buttonArray[event.widget]%10 
        if gameController.exposeCell(brow, bcolumn) == True:
            if gameController.isGameOver(brow, bcolumn) == False:
                if gameController.countMines(brow, bcolumn) > 0:
                    self.updateGame(gameController)
                else:
                    gameController.recursiveExposeEmptyCells(brow, bcolumn)
                    self.updateGame(gameController)
                if gameController.winGame() == True:
                    self.label = Label(self.frame1, text = "You Won!", height = 3)
                    self.label.pack()
            else:
                for x in range (10):
                    for y in range (10):
                        gameController.cellStatus[x][y] = gameController.EXPOSED
                self.updateGame(gameController)
                self.label = Label(self.frame1, text = "Game Over!", height = 3)
                self.label.pack()
    
    def rightClick(self,event,gameController):
        global buttonArray
        brow =  buttonArray[event.widget]/10
        bcolumn = buttonArray[event.widget]%10
        gameController.toggleSeal(brow, bcolumn)
        self.updateGame(gameController)
        if gameController.winGame() == True:
            self.label = Label(self.frame1, text = "You Win !", height = 3)
            self.label.pack()
    
    def createRandomMinedCell(self, gameController):
        numberMine = 0
        while (numberMine < 10):
            mRow = random.randrange(10)
            mCol = random.randrange(10)
            if gameController.cellMined[mRow][mCol] == False:
                gameController.setMine(mRow, mCol)
                numberMine += 1
        
    def createBoardGUI(self,gameController):
        number = 0
        self.frame1 = Frame(root)
        self.frame1.pack()
        self.instruction = Label(self.frame1, text = "To Seal: Right Click (PC) or Ctrl + Left Click (Mac)", height = 2)
        self.instruction.pack()
        self.restartButton = Button(self.frame1, text = "Restart Game",command = self.restartGame)
        self.restartButton.pack(side= 'top')
        
        self.frame = Frame(root)
        self.frame.pack()
        for x in range (gameController.getSize()):
            for y in range (gameController.getSize()):
                self.button = Button(self.frame,text= "",width = 2)
                buttonArray[self.button] = number
                number += 1
                self.button.bind('<Button-1>', lambda event, gameController = gameController : self.leftClick(event,gameController))
                self.button.bind('<Button-3>', lambda event, gameController = gameController : self.rightClick(event,gameController))
                self.button.bind('<Control-Button-1>', lambda event, gameController = gameController : self.rightClick(event,gameController))
                self.button.grid(row = x, column= y)
        root.mainloop()

    def updateGame(self,gameController):
        self.frame.destroy()
        self.frame = Frame(root)
        self.frame.pack()
        number = 0
        for x in range (gameController.getSize()):
            for y in range (gameController.getSize()):
                if gameController.isExposed(x,y) == False:
                    if gameController.isSealed(x, y) == True:
                        self.button = Button(self.frame,text="F",fg = "red",width = 2)
                    else:   
                        self.button = Button(self.frame,text="",width = 2)
                else:
                    if gameController.isGameOver(x,y) == True:
                        self.button = Label(self.frame,text="M",bg ="red",width = 2)
                    else:
                        if gameController.countMines(x,y) > 0:
                            self.button = Label(self.frame,text="%d" %gameController.countMines(x,y),width = 2)
                        elif gameController.countMines(x ,y) == 0:
                            self.button = Label(self.frame,text="", width = 2)
                buttonArray[self.button] = number
                number += 1
                self.button.bind('<Button-1>', lambda event, gameController = gameController : self.leftClick(event,gameController))
                self.button.bind('<Button-3>', lambda event, gameController = gameController : self.rightClick(event,gameController))
                self.button.bind('<Control-Button-1>', lambda event, gameController = gameController : self.rightClick(event,gameController)) 
                self.button.config(state= NORMAL)
                self.button.grid(row = x, column= y)

    def restartGame(self):
        self.frame1.destroy()
        self.frame.destroy()
        self.main()
        
    def main(self):
        self.gameController = GameController()
        self.createRandomMinedCell(self.gameController)
        self.createBoardGUI(self.gameController)


if __name__ == '__main__':
    board = Board()
    board.main()

        