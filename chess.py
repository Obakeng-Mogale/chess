import board

WINNER = None
game_board = board.Board()
default = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
game_board.read_FEN(default)
def main():
    while WINNER is None:
        game_board.draw_board()

        piece_clickedxy = None
        piece_clicked= None
        piece_clickedxy = game_board.await_move()
        piece_clicked = game_board.getPiece(piece_clickedxy[1],piece_clickedxy[0])

        """highlighting selected square"""
        game_board.refresh()
        game_board.draw_board(highlighted=piece_clickedxy)

        """does this till piece is not none"""
        if piece_clicked == None:
            continue
        print('here')
        movexy =  game_board.await_move()
        move = game_board.getPiece(movexy[1],movexy[0])
        game_board.handleMove(piece_clicked,movexy[1],movexy[0])
        
        # if move in game_board.getValidMoves(piece_clicked):
        #     game_board.handleMove()

        
        
    return


if __name__ == "__main__":
    main()
