class Color(object):
    black = 0
    white = 1

# класс фигура 
class Figure(object):
    def move (self, x, y,  x_new, y_new):
        pass
    # внешний вид фигуры из юникода взял 
    IMG = None
    
    def __init__(self, color):
        # цвет 
        self.color = color
        
    def __repr__(self):
        # вернуть цвет шахматы по ее расположению 0-черный 1-белый 
        return self.IMG[ 0 if self.color == Color.black else 1]
    def _get_color_(self):
        return self.color



# класс кароль 
class King(Figure):
    # внешний вид фигуры 
    IMG = ('♔','♚')
# класс пешка 
class Pawn(Figure):
    def __init__(self, color):
        Figure.__init__(self, color)
        self.init_poz = True 

    def move (self, x, y,  x_new, y_new, move_type):
        if (self.color == 1 and x_new <= x) or (self.color == 0 and x_new >= x):
            print('fail5')
            return 0
        if not move_type:
            if y_new != y:
                print('fail')
                return 0
            if self.init_poz and abs(x_new -x) >2:
                print("fail9")
                return 0 
            if not self.init_poz and abs(x_new -x) >1:
                print("fail10")
                return 0 
            self.init_poz = False 
            return 1
        else:
            if abs(x_new - x) > 1 and abs(y_new - y) > 1:
                print("fail32")
                return 0 
            return 1 


             




    # внешний вид фигуры
    IMG = ('♙', '♟')
# класс конь
class Horse(Figure):
    # внешний вид фигуры
    IMG = ('♘','♞')
# класс ладья 
class Castle(Figure):
    # внешний вид фигуры
    IMG = ('♖','♜')
 # класс каролева 
class Queen(Figure):
    # внешний вид фигуры
    IMG = ('♕','♛')
 # класс слон 
class Elephant(Figure):
    # внешний вид фигуры
    IMG = ('♗','♝')
# класс доска 
class Board(object):
    
    def __init__(self):
        # создал массив в массиве 8 на 8 
        self.board = [["."] * 8 for i in range(8)]
        
        # шахматы выставляем в точках массива 
        
        # пешки белые 
        self.board[1] [0] = Pawn(1)
        self.board[1] [1] = Pawn(1)
        self.board[1] [2] = Pawn(1)
        self.board[1] [3] = Pawn(1)
        self.board[1] [4] = Pawn(1)
        self.board[1] [5] = Pawn(1)
        self.board[1] [6] = Pawn(1)
        self.board[1] [7] = Pawn(1)
        # пешки черные 
        self.board[6] [0] = Pawn(0)
        self.board[6] [1] = Pawn(0)
        self.board[6] [2] = Pawn(0)
        self.board[6] [3] = Pawn(0)
        self.board[6] [4] = Pawn(0)
        self.board[6] [5] = Pawn(0)
        self.board[6] [6] = Pawn(0)
        self.board[6] [7] = Pawn(0)
        # белый кароль 
        self.board[0] [3] = King(1)
        # черный кароль 
        self.board[7] [3] = King(0)
        # белая каролева 
        self.board[0] [4] = Queen(1)
        # черная каролева
        self.board[7] [4] = Queen(0)
        # белые кони 
        self.board[0] [6] = Horse(1)
        self.board[0] [1] = Horse(1)
        # черные кони 
        self.board[7] [6] = Horse(0)
        self.board[7] [1] = Horse(0)
        # белые ладья 
        self.board[0] [0] = Castle(1)
        self.board[0] [7] = Castle(1)
        # черная ладья 
        self.board[7] [7] = Castle(0)
        self.board[7] [0] = Castle(0)
        # белый слон 
        self.board[0] [5] = Elephant(1)
        self.board[0] [2] = Elephant(1)
        # черный слон 
        self.board[7] [5] = Elephant(0)
        self.board[7] [2] = Elephant(0)
        print(self.board)
    def play(self):
        while True:
            a = input("Введите: ")
            if a == "stop":
                break
            a = a.split()
            self.move(a[0], a[1])
            print(self)

            

    def move(self, old, new):
        print(self.board[int(new[0])][int(new[1])])
        if self.board[int(old[0])][int(old[1])] == ".":  
            print("Error!!!!")
        move_type = self.board[int(new[0])][int(new[1])] != "."
        if move_type and self.board[int(new[0])][int(new[1])]._get_color_() == self.board[int(old[0])][int(old[1])]._get_color_() :
            print("Error!!!!")
            
         
        else:
            if (self.board[int(old[0])][int(old[1])] == '♙'  or  self.board[int(old[0])][int(old[1])] == '♟') and (self.board[int(old[0]+1)][int(old[1])] == "."):
            if self.board[int(old[0])][int(old[1])].move(int(old[0]), int(old[1]), int(new[0]), int(new[1]), move_type ) :
                self.board[int(new[0])][int(new[1])] = self.board[int(old[0])][int(old[1])]
                self.board[int(old[0])][int(old[1])] = "."

                    

                    
                
    def __repr__(self):
        # растояние от начала строки 
        res = ''
        # обходим 8 и добавляем столькоже строк 
        for y in range(8):
            # join добавляет между каждой клеткой пробел 
            # map переводит все содержимое листа в str 
            res += ' '.join(map(str, self.board[y])) + "\n"
        return res



# вывожу 
b = Board()
b.play()
print(b)