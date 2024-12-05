from picture import Picture

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

class Pawn:
    
    def __init__(self,rank,rfile,color):
        self.rank = rank
        self.rfile = rfile
        self.color = color
        self.is_first_move = True
        if self.color:
            self.image = wPAWN
        else:self.image = bPAWN
    
    def move(self,rank,rfile):
        self.rank = rank
        self.rfile = rfile
        return
    def get_image(self)->Picture:
        return self.image
    def __str__(self):
        if self.color:
            color = 'w'
        else:color = 'b'
        return '{}, {}'.format(color, type(self))
    
    def __repr__(self):
        return '{}'.format(type(self))
    

class Rook(Pawn):
    def __init__(self, rank, rfile, color):
        super().__init__(rank, rfile, color)
        if self.color:
            self.image = wROOK
        else:self.image = bROOK


class King(Pawn):
    def __init__(self, rank, rfile, color):
        super().__init__(rank, rfile, color)
        if self.color:
            self.image = wKING
        else:self.image = bKING

class Bishop(Pawn):
    def __init__(self, rank, rfile, color):
        super().__init__(rank, rfile, color)
        if self.color:
            self.image = wBISHOP
        else:self.image = bBISHOP

class Queen(Pawn):
    def __init__(self, rank, rfile, color):
        super().__init__(rank, rfile, color)
        if self.color:
            self.image = wQUEEN
        else:self.image = bQUEEN

class Knight(Pawn):
    def __init__(self, rank, rfile, color):
        super().__init__(rank, rfile, color)
        if self.color:
            self.image = wKNIGHT
        else:self.image = bKNIGHT

if __name__ == "__main__":
    k1 = Knight(1,1,True)
    print(k1.image)
