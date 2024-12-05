import stddraw
import stdarray,stdio,stdaudio
import math
from color import Color
from picture import Picture
import time
import pieces

#setting the scene
wKNIGHT=Picture('pieces-png/wN.png')
lightGreen = Color(238,238,210)
darkGreen = Color(118,150,86)
darkGrey = Color(48,46,43)
highlighted_dark = Color(185,202,67)
highlighted_light = Color(245,246,130)
stddraw.setCanvasSize(800,800)
stddraw.setPenColor(darkGreen)
stddraw.setXscale(-2,9)
stddraw.setYscale(-2,9)
winner = None
letters = ['a','b','c','d','e','f','g','h']

"""
image of pieces
"""


class Board:
    def __init__(self):
        self.move_history = [[]]
        self.board = stdarray.create2D(8,8,None)
        self.last_move = None
        self.black_castling_k = True#true meaning it can happen
        self.white_castling_K= True
        self.black_castling_q = True#true meaning it can happen
        self.white_castling_Q= True
        self.previous_location = None
        self.en_passants = []
        self.halfmove_clock = 0
        self.fullmove = 0

    def read_FEN(self,FEN:str):
        """rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
            starting Fen notation
        """
        white_to_play = True
        index = 0
        state = None
        FEN = FEN.split('/')
        FEN = ''.join(FEN)
        # FEN = list(FEN)
        for l in range(64):
            if FEN[l] in '12345678':
                FEN= ''.join([FEN[0:l],' '*int(FEN[l]),FEN[l+1:]])
       

        for i in range(8):
            letter:str
            for j in range(8):
                letter = FEN[index]
                discern = letter.lower()

                if discern == 'r':
                    if letter.isupper():self.board[i][j]= pieces.Rook(i,j,True)
                    else:self.board[i][j]= pieces.Rook(i,j,False)

                elif discern == 'p':
                    if letter.isupper():self.board[i][j]= pieces.Pawn(i,j,True)
                    else:self.board[i][j]= pieces.Pawn(i,j,False)

                elif discern == 'q':
                    if letter.isupper():self.board[i][j]= pieces.Queen(i,j,True)
                    else:self.board[i][j]= pieces.Queen(i,j,False)

                elif discern == 'n':
                    if letter.isupper():self.board[i][j]= pieces.Knight(i,j,True)
                    else:self.board[i][j]= pieces.Knight(i,j,False)

                elif discern == 'k':
                    if letter.isupper():self.board[i][j]= pieces.King(i,j,True)
                    else:self.board[i][j]= pieces.King(i,j,False)
                elif discern == 'b':

                    if letter.isupper():self.board[i][j]= pieces.Bishop(i,j,True)
                    else:self.board[i][j]= pieces.Bishop(i,j,False)
                index+=1
        return FEN[index+1:]
        
      

    def board_state(self,fen_state:str):

        """turn , castling_w, castling_black,possible en_passants
        -
        kq
        KQ
        kQ
        Kq

        """

        white_to_move=True
        fen_state=fen_state.split(' ')
        print(fen_state)
        castling = fen_state[1]
        en_passants = fen_state[2]
        halfmoves = fen_state[3]
        fullmoves = fen_state[4]
        self.fullmove=fullmoves
        self.halfmove_clock = halfmoves
        self.en_passants = en_passants
        if fen_state[1] == '-':
            self.white_castling_Q= False
            self.black_castling_q= False
            self.white_castling_K = False
            self.black_castling_k= False

        if "K" in fen_state[1] :
            self.black_castling_k= False
            self.black_castling_q= False
        if fen_state[1] == 'kq':
            self.black_castling_k= False
            self.black_castling_q= False
        if fen_state[0] =='w':
            white_to_move = True
        else: white_to_move = False

    def get_fen(self):

        """return current board states fen notation"""

        pass

    def convert_to_alphanumeric(self,rank,rfile):
        return letters[rfile]+str(8-rank)

    def getPiece(self,rank,rfile,Turn):

        """return the piece object"""

        piece = self.board[rank][rfile]
        
        if piece is None:
            return None
        if piece.color == Turn:
            print(type(piece),piece.color)
            return piece
        if piece.color !=Turn:
            print(type(piece),piece.color)
            return piece
  
    
    def get_piece_locations(self,piece):
        locations = []
        for rank in self.board:
            for square in rank:
                if square != None and square==piece:
                    locations.append(square)
        return locations
    

    """might need to be in pieces.py"""
    def getValidMoves(self,piece):
        if type(piece) == "Pawn":
                    pass
        elif type(piece)=="Rook":
            pass
        elif type(piece) == "Knight":
            pass
        elif type(piece)=="Bishop":
            pass
        elif type(piece) == "Queen":
            pass
        elif type(piece)=="King":
            pass
        for rank in range(len(self.board)):
            for rfile in range(len(self.board[rank])):
                pass
                

    def await_move(self):

        while not(stddraw.mousePressed()):
                stddraw.show(0.1)

        rfile,rank = int(round(stddraw.mouseX())),(7-int(round(stddraw.mouseY())))\
        
        stddraw.clear()

        if not(0<=rank<=7)or not(0<=rfile<=7):
            self.draw_board()
            return self.await_move()
        self.draw_board()
        return rfile,rank
        
            
    def handleMove(self,piece,rank,rfile, previousrank,previousfile,turn:bool, captures=-1)->bool:
        capture = ''
        if captures != -1:
            capture = 'x'
        previous_block = self.convert_to_alphanumeric(previousrank,previousfile)
        self.board[piece.rank][piece.rfile]= None
        piece.move(rank,rfile)
        if piece.is_first_move and type(pieces.Pawn):
            self.en_passant = previous_block

        if type(piece)== pieces.Pawn:
            if captures==0:
                self.move_history[self.fullmove]
                self.move_history[self.fullmove].append(str(letters[previousfile]+capture+self.convert_to_alphanumeric(rank,rfile)))
            else:self.move_history[self.fullmove].append(str(self.convert_to_alphanumeric(rank,rfile)))
        else:self.move_history[self.fullmove].append(str(piece)+ capture+ self.convert_to_alphanumeric(rank,rfile))


        self.board[piece.rank][piece.rfile]= piece
        self.last_move= [rfile,rank]
        self.previous_location= [previousfile,previousrank]
        stdaudio.playFile("sounds/move")

        if not turn:
            self.move_history.append([])
            self.fullmove+=1

        print(self.move_history)
        return not turn
        
    def refresh(self,pos=None):
        stddraw.clear()
        #removes the previous highlight from move
      
        self.draw_board(highlighted=pos)
        return 
    
    def draw_board(self,highlighted:list = None, possible_moves=None):
        
        stddraw.setPenColor(darkGrey)
        stddraw.filledSquare((-1+8)/2,(-1+8)/2,10)
        for rank in range(len(self.board)):
            stddraw.setFontSize(16)
            for cfile in range(len(self.board[rank])):

                piece = self.board[7-rank][cfile]
                
                if ((rank+cfile)%2)==0:
                    if (cfile,7-rank) == highlighted or self.last_move ==[cfile,7-rank] or self.previous_location == [cfile,7-rank]:
                        stddraw.setPenColor(highlighted_dark)
                    # elif self.last_move!=None:
                    #     stddraw.setPenColor(highlighted_dark)
                    else:    
                        stddraw.setPenColor(darkGreen)
                    stddraw.filledSquare(cfile,rank,0.505)

                    if piece:

                        stddraw.picture(piece.get_image(),cfile,rank,1,1)
                    # if cfile==7 :
                    #     stddraw.setPenColor(darkGreen)
                    #     stddraw.text(cfile+0.25,rank+0.25,str(rank))
                    # if rank == 0:
                    #     stddraw.setPenColor(darkGreen)
                    #     stddraw.text(cfile+0.25,rank+0.25,letters[rank])
                
                else:
            
                    if (cfile,7-rank)== highlighted or self.last_move ==[cfile,7-rank] or self.previous_location == [cfile,7-rank]:

                        stddraw.setPenColor(highlighted_light)
                    else:
                        stddraw.setPenColor(lightGreen)
                    stddraw.filledSquare(cfile,rank,0.505)
                    
                    if piece:
                        stddraw.picture(piece.get_image(),cfile,rank,1,1)
                    # if cfile==0 and rank==7:
                    #     stddraw.setPenColor(lightGreen)
                    #     stddraw.text(cfile+0.99,rank+0.99,str(rank))
                    # if rank == 7:
                    #     stddraw.setPenColor(lightGreen)
                    #     stddraw.text(cfile+0.5,rank+0.5,letters[rank])
        stddraw.show(1)


    def __str__(self):
        return str(stdarray.write2D(self.board))


            
    #stddraw.show()
if __name__ == "__main__": 
    board = Board()
    default = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    random = "1b6/1p6/1k4P1/2p2B2/3qb2B/1K1p2PP/2p1pp2/8 w - - 0 1"
    random1 = "3k4/8/2pP2B1/P1P1p1p1/7P/1K4pp/7b/Bn2r3 w - - 0 1"
    random2 = "rnb1kbnr/ppp2ppp/3ppq2/8/5P2/6P1/PPPPP2P/RNBQKBNR w KQkq - 0 1"
    state = board.read_FEN(random)
    # state = board.board_state(state)
    # print(state,len(state))
    board.draw_board()
    board.board_state(state)
    print(board.convert_to_alphanumeric(0,0))
    piecexy = board.await_move()
    p = board.getPiece(piecexy[1],piecexy[0])
    print(piecexy,"\n",p)

