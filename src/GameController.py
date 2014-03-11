
class GameController():

    def __init__(self):
        self.SIZE = 10
        (self.SEALED, self.EXPOSED, self.UNEXPOSED) = range(0, 3)     
        self.cellStatus = [[ 0 for i in range(self.SIZE) ] for j in range(self.SIZE)]
        self.cellMined = [[0 for i in range (self.SIZE)] for j in range (self.SIZE)]
        for x in range (self.SIZE):
            for y in range (self.SIZE):
                self.cellStatus[x][y] = self.UNEXPOSED
                self.cellMined[x][y] = False
    
    def getSize(self):
        return self.SIZE
        
    def isExposed(self, x, y):
        return self.cellStatus[x][y] == self.EXPOSED
        
    def isSealed(self, x, y):
        return self.cellStatus[x][y] == self.SEALED
       
    def isUnexposed(self, x, y):
        return self.cellStatus[x][y] == self.UNEXPOSED
        
    def setMine (self, x, y):
        self.cellMined[x][y] = True
    
    def exposeCell(self,x,y):
        if (self.cellStatus[x][y] == self.UNEXPOSED):
            self.cellStatus[x][y] = self.EXPOSED
            return True
        else:
            return False

    def toggleSeal(self, x, y):
        if self.cellStatus[x][y] != self.EXPOSED:
            if self.cellStatus[x][y] == self.SEALED:
                self.cellStatus[x][y] = self.UNEXPOSED
            elif self.cellStatus[x][y] == self.UNEXPOSED:
                self.cellStatus[x][y] = self.SEALED
            return True 
        else:
            return False
       
    def countMines(self, x, y):
        counter = 0
        for adjX in range (-1, 2):
           for adjY in range (-1, 2):
                if (x + adjX) in range (self.SIZE) and (y + adjY) in range (self.SIZE):
                    if self.cellMined[x + adjX][y + adjY] == True:
                        counter += 1                   
        return counter
        
    def isGameOver(self, x, y):
        return self.cellStatus[x][y] == self.EXPOSED and self.cellMined[x][y] == True

    def recursiveExposeEmptyCells(self, x, y):
        if self.isSealed(x, y) == False: 
            self.exposeCell(x,y)
            for adjX in range (-1, 2):
               for adjY in range (-1, 2):
                    neighborX = x + adjX
                    neighborY = y + adjY
                    if (neighborX) in range (self.SIZE) and (neighborY) in range (self.SIZE):
                        if self.cellStatus[neighborX][neighborY] == self.UNEXPOSED and self.cellMined[neighborX][neighborY] == False:
                            if self.countMines(neighborX, neighborY) > 0: 
                                self.exposeCell(neighborX,neighborY)
                            elif self.countMines(neighborX, neighborY) == 0:
                                self.recursiveExposeEmptyCells(neighborX, neighborY)
    
    def winGame(self):
        won = True
        for x in range (self.SIZE):
            for y in range (self.SIZE):
                if(self.cellMined[x][y] == False and self.cellStatus[x][y] == self.UNEXPOSED) or (self.cellMined[x][y] == True and self.cellStatus[x][y] != self.SEALED):
                    won = False
                    break
        return won