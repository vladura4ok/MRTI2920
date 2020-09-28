class Figure:
    def __init__(self, color, x, y):
        self.color = color 
        self.x = x
        self.y = y

    def move (self, x, y):
        self.x = x
        self.y = y

class Pawn(Figure):
    def move (self, x, y):
        if self.y == 2 and color == 'white' and y > 4:
            print('fail')
            return
#Добить оставшиеся кейсы для пешки
        Figure.move(self, x, y)

class GM:
    def __init__ (self):
        self.history = []
        self.board = []
        self.board.append(Pawn('white', 1, 2))
        ########3
        self.board.append(Pawn('white', 8, 2))

# Добавить все фигуры

    def log (self, init_x , init_y, x, y):
        for f in self.board:
            if f.x == init_x and f.y == init_y:
                f.move(x, y)
                self.history.append(f'{f.x}{f.y}->{x}{y}')








    





class Deck:

    x = [0, A, B, C, D, E, F, G, H]
    y = [0, 1, 2, 3, 4, 5, 6, 7, 8]


    def placePieces(self):
    
        for i in range(0,8):
            self.gameboard[(i,1)] = Pawn(WHITE,uniDict[WHITE][Pawn],1)
            self.gameboard[(i,6)] = Pawn(BLACK,uniDict[BLACK][Pawn],-1)
            
        placers = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        
        for i in range(0,8):
            self.gameboard[(i,0)] = placers[i](WHITE,uniDict[WHITE][placers[i]])
            self.gameboard[((7-i),7)] = placers[i](BLACK,uniDict[BLACK][placers[i]])
        placers.reverse()


(self, name, color, x, y)