import board

WINNER = None
game_board = board.Board()
default = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
test = "B5K1/1ppp2p1/6R1/2r1R1n1/3Pp3/3P4/5P1p/5k2 b - - 0 1"
TURN = True #true being whites turn false being blacks turn
game_board.read_FEN(default)
current_selection = None
def search_checks():
    return "check"
    return "check mate"
    return None

def moves():
    global TURN

    return
def promotion():
    pass
def main():
    global TURN
    while WINNER is None:

        game_board.draw_board()

        piece_clickedxy = None
        piece_clicked= None
        piece_clickedxy = game_board.await_move()
        piece_clicked = game_board.getPiece(piece_clickedxy[1],piece_clickedxy[0],TURN)

        

        """does this till piece is not none"""
        if piece_clicked == None or piece_clicked.color!=TURN:
            continue

        game_board.refresh(piece_clickedxy)#ensures square is highlighted
        valid_moves = game_board.getValidMoves(piece_clicked)
        print('piece can move to', valid_moves  )

        movexy =  game_board.await_move()
        color_pieces = game_board.get_piece_locations(piece_clicked)#ensures you do not move onto the same colord piece as the others
        if [movexy[1],movexy[0]] not in valid_moves:
            continue
        
        move = game_board.getPiece(movexy[1],movexy[0],TURN)
       
        if movexy == piece_clickedxy or move in color_pieces:
            # new_piece_clicked = move
            continue
        elif move != None:#move in possible_moves and 
            """deals with captures""" 
            TURN = game_board.handleMove(piece_clicked,movexy[1],movexy[0],piece_clickedxy[1],piece_clickedxy[0],TURN, captures=0)

        else:TURN = game_board.handleMove(piece_clicked,movexy[1],movexy[0],piece_clickedxy[1],piece_clickedxy[0],TURN, captures=-1)# -1 being nothing was captured in the move

        
        
    return


if __name__ == "__main__":
    main()
