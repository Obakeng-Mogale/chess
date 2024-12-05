from picture import Picture
from math import dist

bBISHOP=Picture('pieces-png/bB.png')
bROOK= Picture('pieces-png/bR.png')
bKING= Picture('pieces-png/bK.png')
bQUEEN= Picture('pieces-png/bQ.png')
bPAWN= Picture('pieces-png/bP.png')
bKNIGHT=Picture('pieces-png/bN.png')

wBISHOP=Picture('pieces-png/wB.png')
wROOK= Picture('pieces-png/wR.png')
wKING= Picture('pieces-png/wK.png')
wQUEEN= Picture('pieces-png/wQ.png')
wPAWN= Picture('pieces-png/wP.png')
wKNIGHT=Picture('pieces-png/wN.png')
letters = ['a','b','c','d','e','f','g','h']
class Matrix:
    pass
class Pawn:
    
    def __init__(self,rank,rfile,color:bool):
        self.rank = rank
        self.rfile = rfile
        self.color = color
        self.is_first_move = True
        self.en_passant = False
        self.char = letters[rfile]
        if self.color:
            self.image = wPAWN
        else:self.image = bPAWN
    
    def move(self,rank,rfile):
        if self.is_first_move and dist([rank,rfile],[self.rank,self.rfile])==2:
            self.en_passant = True
        
        self.is_first_move = False
        self.rank = rank
        self.rfile = rfile
        return
    
    def get_color(self):
        return self.color
    def get_image(self)->Picture:
        return self.image
    
   
    
    def __str__(self):
        return self.char
    
    def __eq__(self, value):
        if value == None:
            return False
        
        return self.color == value.color
    

    def __repr__(self):
        return '{}'.format(type(self))
    

class Rook(Pawn):
    def __init__(self, rank, rfile, color):
        super().__init__(rank, rfile, color)
        self.char = 'R'
        self.has_moved = False
        if self.color:
            self.image = wROOK
            
        else:self.image = bROOK

    def move(self,rank,rfile):
        self.rank = rank
        self.rfile = rfile
        return

class King(Pawn):
    def __init__(self, rank, rfile, color):
        super().__init__(rank, rfile, color)
        self.has_moved = False
        self.char = 'K'
        if self.color:
            self.image = wKING
            
        else:self.image = bKING

    def move(self,rank,rfile):
        self.rank = rank
        self.rfile = rfile
        return
class Bishop(Pawn):
    def __init__(self, rank, rfile, color):
        super().__init__(rank, rfile, color)
        self.char = 'B'
        if self.color:
            self.image = wBISHOP
            
        else:self.image = bBISHOP

    def move(self,rank,rfile):
        self.rank = rank
        self.rfile = rfile
        return
class Queen(Pawn):
    def __init__(self, rank, rfile, color):
        super().__init__(rank, rfile, color)
        self.char = 'Q'
        if self.color:
            self.image = wQUEEN
            
        else:self.image = bQUEEN

    def move(self,rank,rfile):
        self.rank = rank
        self.rfile = rfile
        return
class Knight(Pawn):
    def __init__(self, rank, rfile, color):
        super().__init__(rank, rfile, color)
        self.char = 'N'
        if self.color:
            self.image = wKNIGHT
            
        else:self.image = bKNIGHT

    def move(self,rank,rfile):
        self.rank = rank
        self.rfile = rfile
        return

if __name__ == "__main__":
    k1 = Knight(1,1,True)
    print(k1.image)
