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
        self.pin = False
        self.is_first_move = False
        self.en_passant = False
        self.char = letters[rfile]
        if self.color:
            self.image = wPAWN
            if self.rank == 6:
                self.is_first_move = True
        else:
            self.image = bPAWN
            if self.rank == 1:
                self.is_first_move = True
        
    
    def move(self,rank,rfile):
        """pawn move 1 foward but can make 2 on the first move but only capture diagonally"""
        if self.is_first_move and dist([rank,rfile],[self.rank,self.rfile])==2:
            self.en_passant = True
        
        self.is_first_move = False
        self.rank = rank
        self.rfile = rfile
        return
    
    def pin(self):
        self.pin = True
        return
    
    def get_pin_status(self):
        return self.pin
    
    def get_possible_moves(self)->list:
        """ gives all moves possible
            1 move 
            first move
            left capture
            right capture
        """
        self.move_locations = []
        if self.color:
            self.move_locations.append([self.rank-1,self.rfile])
            if self.is_first_move:
                self.move_locations.append([self.rank-2,self.rfile])
            
            if self.rfile==0:
                self.move_locations.append([self.rank-1,self.rfile+1])
            elif self.rfile==7:
                self.move_locations.append([self.rank-1,self.rfile-1])
            else:  
                self.move_locations.append([self.rank-1,self.rfile+1])
                self.move_locations.append([self.rank-1,self.rfile-1])
        else: 
            self.move_locations.append([self.rank+1,self.rfile])
            if self.is_first_move:
                self.move_locations.append([self.rank+2,self.rfile])
            if self.rfile==0:
                self.move_locations.append([self.rank+1,self.rfile+1])
            elif self.rfile==7:
                self.move_locations.append([self.rank+1,self.rfile-1])
            else:  
                self.move_locations.append([self.rank+1,self.rfile+1])
                self.move_locations.append([self.rank+1,self.rfile-1]) 
        out_of_range = []
        for move in self.move_locations:
            
            if move[0]>=8 or move[0]<0 or move[1]>=8 or move[1]<0:
                    out_of_range.append(move)

        self.move_locations = [x for x in self.move_locations if x not in out_of_range]
            
        return self.move_locations
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

    def get_direction(self, coord:list):
        """gets all things blocking in the direction
        
        return down [0,1] or up[0,-1] or left[-1,0] or right[1,0]"""
        if coord[0]>self.rank and coord[1]==self.rfile:
            return [0,1]
        elif coord[0]<self.rank and coord[1]==self.rfile:
            return [0,-1]
        elif coord[1]<self.rfile and coord[0]==self.rank:
            return [-1,0]
        elif coord[1]>self.rfile and coord[0]==self.rank:
            return [1,0]
        
    def get_blocked_in_direction(self,blocking:list,direction,coords):
        invalid = []
        print(coords ,"\n",blocking)
        for coord in coords:
            # print(coord,blocking)
            if direction == [0,1] and coord[0]>blocking[0] and coord[1]==blocking[1]:
                invalid.append(coord)
            elif direction == [0,-1] and coord[0]<blocking[0]and coord[1]==blocking[1]: 
                invalid.append(coord)
            elif direction == [-1,0] and coord[1]<blocking[1]and coord[0]==blocking[0]:
                invalid.append(coord) 
            elif direction == [1,0] and coord[1]>blocking[1]and coord[0]==blocking[0]:
                invalid.append(coord)      
        return invalid
    
    def get_possible_moves(self)->list:
        """rooks move in straignt lines and cannot jump over pieces"""
        self.move_locations = []
        for direction in range(4):
            
            for move in range(1,9):
                if direction == 0:
                    self.move_locations.append([self.rank+move,self.rfile])

                elif direction ==1: 
                    self.move_locations.append([self.rank-move,self.rfile])

                elif direction ==2: 
                    self.move_locations.append([self.rank,self.rfile+move])

                else:
                    self.move_locations.append([self.rank,self.rfile-move])
                if self.move_locations[-1][0]>=8 or self.move_locations[-1][0]<0 or self.move_locations[-1][1]>=8 or self.move_locations[-1][1]<0:
                    self.move_locations.pop()
            
        return self.move_locations 
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
    
    def get_possible_moves(self):
        
        self.move_locations = []
        out_of_range = []
        self.move_locations.append([self.rank+1,self.rfile-1])
        self.move_locations.append([self.rank+1,self.rfile+1])
        self.move_locations.append([self.rank+1,self.rfile])
        self.move_locations.append([self.rank-1,self.rfile+1])
        self.move_locations.append([self.rank-1,self.rfile-1])
        self.move_locations.append([self.rank-1,self.rfile])
        self.move_locations.append([self.rank,self.rfile+1])
        self.move_locations.append([self.rank,self.rfile-1])
        for move in self.move_locations:
            
            if move[0]>=8 or move[0]<0 or move[1]>=8 or move[1]<0:
                    out_of_range.append(move)
        print(out_of_range)
        self.move_locations = [x for x in self.move_locations if x not in out_of_range]
        return self.move_locations
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
    
    def get_possible_moves(self)->list:
        """rooks move in straignt lines and cannot jump over pieces"""
        self.move_locations = []
        for direction in range(4):
            
            for move in range(1,9):
                if direction == 0:
                    self.move_locations.append([self.rank+move,self.rfile+move])

                elif direction ==1: 
                    self.move_locations.append([self.rank-move,self.rfile-move])

                elif direction ==2: 
                    self.move_locations.append([self.rank-move,self.rfile+move])

                else:
                    self.move_locations.append([self.rank+move,self.rfile-move])
                if self.move_locations[-1][0]>=8 or self.move_locations[-1][0]<0 or self.move_locations[-1][1]>=8 or self.move_locations[-1][1]<0:
                    self.move_locations.pop()
    
class Queen(Rook):

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
    
    def get_possible_moves(self):
        """knights can jump over pieces and """
        self.move_locations = []
        out_of_range = []
        self.move_locations.append([self.rank+2,self.rfile-1])
        self.move_locations.append([self.rank+2,self.rfile+1])
        self.move_locations.append([self.rank-2,self.rfile-1])
        self.move_locations.append([self.rank-2,self.rfile+1])
        self.move_locations.append([self.rank-1,self.rfile-2])
        self.move_locations.append([self.rank+1,self.rfile-2])
        self.move_locations.append([self.rank-1,self.rfile+2])
        self.move_locations.append([self.rank+1,self.rfile+2])
        for move in self.move_locations:
            
            if move[0]>=8 or move[0]<0 or move[1]>=8 or move[1]<0:
                    out_of_range.append(move)
        print(out_of_range)
        self.move_locations = [x for x in self.move_locations if x not in out_of_range]
        return self.move_locations

if __name__ == "__main__":
    k1 = Knight(1,1,True)
    print(k1.image)
