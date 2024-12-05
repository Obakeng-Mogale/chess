import board

WINNER = None
game_board = board.Board()
default = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
TURN = True #true being whites turn false being blacks turn
game_board.read_FEN(default)
current_selection = None
def search_checks():
    return "check"
    return "check mate"
    return "None"

def moves():
    global TURN

    return

def main():
    global TURN
    while WINNER is None:

        game_board.draw_board()

        piece_clickedxy = None
        piece_clicked= None
        piece_clickedxy = game_board.await_move()
        piece_clicked = game_board.getPiece(piece_clickedxy[1],piece_clickedxy[0],TURN)

        

        """does this till piece is not none"""
        if piece_clicked == None:
            continue

        game_board.refresh(piece_clickedxy)#ensures square is highlighted
        print('piece can move to', game_board.getValidMoves(piece_clicked))
        movexy =  game_board.await_move()
        color_pieces = game_board.get_piece_locations(piece_clicked)
        
        move = game_board.getPiece(movexy[1],movexy[0],TURN)
        if movexy == piece_clickedxy or move in color_pieces:
            # new_piece_clicked = move
            continue
        TURN = game_board.handleMove(piece_clicked,movexy[1],movexy[0],piece_clickedxy[1],piece_clickedxy[0],TURN)

        
        
    return


if __name__ == "__main__":
    main()
