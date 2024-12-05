import stddraw
import stdarray,stdio
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
highlighted_green = Color(185,202,67)
highlighted_light = Color(245,246,130)
stddraw.setCanvasSize(800,800)
stddraw.setPenColor(darkGreen)
stddraw.setXscale(-2,9)
stddraw.setYscale(-2,9)
winner = None
"""
image of pieces
"""


class Board:
    def __init__(self):
        self.board = stdarray.create2D(8,8,None)

    def read_FEN(self,FEN:str):
        """rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
            starting Fen notation
        """
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
        fen_state=fen_state.split(' ')
        return fen_state
    

    def getPiece(self,rank,rfile):
        piece = self.board[rank][rfile]
        return piece
    
    def getValidMoves(self,piece):
        for rank in range(len(self.board)):
            for rfile in range(len(self.board[rank])):
                pass

    def await_move(self):

        while not(stddraw.mousePressed()):
                stddraw.show(1)

        rfile,rank = int(round(stddraw.mouseX())),(7-int(round(stddraw.mouseY())))
        stddraw.clear()
        if not(0<=rank<=7)or not(0<=rfile<=7):
            return self.await_move()
        self.draw_board()
        return rfile,rank
        
            
    def handleMove(self,piece,rank,rfile):
        self.board[piece.rank][piece.rfile]= None
        piece.move(rank,rfile)
        self.board[piece.rank][piece.rfile]= piece
        pass
        
    def refresh(self):
        stddraw.clear()
        return 
    def draw_board(self, latest_move:list =None,highlighted:list = None):
        print(highlighted)

        stddraw.setPenColor(darkGrey)
        stddraw.filledSquare((-1+8)/2,(-1+8)/2,10)
        for rank in range(len(self.board)):

            for cfile in range(len(self.board[rank])):

                piece = self.board[7-rank][cfile]

                if ((rank+cfile)%2)==0:
                    if (cfile,rank) == highlighted:
                        stddraw.setPenColor(highlighted_green)
                    else:    
                        stddraw.setPenColor(darkGreen)
                    stddraw.filledSquare(cfile,rank,0.505)

                    if piece:

                        stddraw.picture(piece.get_image(),cfile,rank,1,1)


                else:
                    
                    if (cfile,rank)== highlighted:

                        stddraw.setPenColor(highlighted_light)
                    else:
                        stddraw.setPenColor(lightGreen)
                    stddraw.filledSquare(cfile,rank,0.505)
                    if piece:
                        stddraw.picture(piece.get_image(),cfile,rank,1,1)

        stddraw.show(1)


    def __str__(self):
        return str(stdarray.write2D(self.board))

'''
Pieces location using 2d array
'''





def getPiece(x,y):
    pass


            
    #stddraw.show()
if __name__ == "__main__": 
    board = Board()
    default = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    random = "1b6/1p6/1k4P1/2p2B2/3qb2B/1K1p2PP/2p1pp2/8 w - - 0 1"
    random1 = "3k4/8/2pP2B1/P1P1p1p1/7P/1K4pp/7b/Bn2r3 w - - 0 1"
    random2 = "rnb1kbnr/ppp2ppp/3ppq2/8/5P2/6P1/PPPPP2P/RNBQKBNR w KQkq - 0 1"
    state = board.read_FEN(default)
    state = board.board_state(state)
    print(state,len(state))
    board.draw_board()
    piecexy = board.await_move()
    p = board.getPiece(piecexy[1],piecexy[0])
    print(piecexy,"\n",p)
    movexy = board.await_move()
    move = getPiece(movexy[1],movexy[0])
    print(move)
    # for i in board:
    #     for j in i:
    #         print(j,end=' ')
    #     print()
    # draw_board(board)
    
    # # Check if the mouse button is pressed
    # while winner == None:
    #     while not stddraw.mousePressed():
    #         stddraw.show(1)
    #         # Get the coordinates of the mouse pointer
    #     x = int(stddraw.mouseX())
    #     y = int(stddraw.mouseY())
    #     stddraw.clear()
    #     draw_board(board)
    #     time.sleep(0.01)
    #     getPiece(x,y)
    #     print('here')
    #     while not stddraw.mousePressed():
    #         stddraw.show(1)
    #     xa = int(stddraw.mouseX())
    #     ya = int(stddraw.mouseY())
    #     # Draw a point at the mouse coordinate
    #     print(x,y)
    #     handle_move(x,y,xa,ya)
    #     # Show the result

    #     # Small delay to prevent multiple detections for a single click
    #     time.sleep(0.1)