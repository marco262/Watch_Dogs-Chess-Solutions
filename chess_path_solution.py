import time
from copy import deepcopy

GOOD_PIECES = ['R', 'N', 'B', 'Q', 'K']
BAD_PIECES = ['p']
BOARD_WIDTH = 8

##board = [[' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' ']]

############# Chess boards 1-10 #############
##board = [[' ',' ',' ',' ',' ','p',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         ['p',' ',' ',' ',' ','p',' ',' '],
##         [' ',' ','p',' ','p',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         ['p',' ',' ',' ','p',' ',' ',' '],
##         [' ','p',' ',' ',' ',' ',' ',' '],
##         ['R',' ','B',' ',' ',' ',' ',' ']]

##board = [[' ',' ','p',' ','p',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ','p'],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ','Q','Q','p',' ',' '],
##         [' ','p',' ',' ',' ',' ',' ','p'],
##         [' ',' ','p',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ','p',' ',' ']]

##board = [[' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ','p','p',' ',' '],
##         [' ',' ',' ','p',' ',' ',' ',' '],
##         [' ',' ',' ','p',' ','p',' ',' '],
##         [' ',' ','p',' ',' ',' ',' ','p'],
##         [' ',' ',' ',' ','p',' ',' ',' '],
##         [' ','N',' ',' ',' ',' ','N',' ']]

##board = [[' ',' ',' ',' ',' ',' ',' ',' '],
##         ['p',' ',' ','p',' ','Q',' ',' '],
##         [' ',' ','p',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ','p',' ',' ','p',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ','Q','p',' ',' ',' ','p'],
##         [' ','p','p',' ',' ',' ',' ',' ']]

##board = [[' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ','p','p',' ',' ',' '],
##         [' ',' ','p',' ','p','p',' ',' '],
##         [' ',' ','p',' ','p','p',' ',' '],
##         [' ',' ',' ','p','p',' ',' ',' '],
##         [' ','N',' ',' ',' ',' ','N',' ']]

##board = [[' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ','p'],
##         [' ',' ',' ',' ','p',' ','p','p'],
##         [' ',' ','p',' ',' ',' ',' ','B'],
##         ['R',' ','p',' ','p',' ',' ',' '],
##         [' ',' ','p','p',' ',' ',' ','p'],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' ']]

##board = [[' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ','p',' ',' ',' '],
##         [' ',' ','p',' ','p',' ',' ','p'],
##         [' ',' ',' ',' ',' ','p',' ',' '],
##         [' ','p','p',' ',' ','p','p',' '],
##         [' ',' ',' ','p','p',' ',' ',' '],
##         [' ','N',' ',' ',' ','p','N',' ']]

##board = [[' ',' ',' ',' ','B',' ',' ',' '],
##         [' ',' ',' ','p',' ','p',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ',' ','p'],
##         [' ',' ','p',' ','p','p',' ','p'],
##         [' ',' ',' ',' ',' ','p',' ','p'],
##         [' ',' ',' ',' ',' ',' ',' ',' '],
##         [' ','p','p','R',' ','p',' ',' ']]

##board = [[' ',' ',' ',' ','p',' ',' ',' '],
##         [' ',' ','p',' ',' ',' ',' ',' '],
##         [' ',' ',' ','p',' ',' ',' ',' '],
##         [' ','p',' ','p','p','p',' ',' '],
##         [' ',' ','p',' ',' ','p',' ',' '],
##         [' ',' ','p',' ','p','p',' ','p'],
##         [' ',' ',' ','p',' ',' ',' ',' '],
##         [' ','N',' ',' ',' ',' ','N',' ']]

##board = [[' ','p',' ',' ',' ','p',' ',' '],
##         ['p',' ','p',' ',' ','p',' ',' '],
##         [' ',' ','N','p',' ','p',' ',' '],
##         [' ',' ',' ',' ','p',' ',' ',' '],
##         [' ',' ',' ',' ',' ',' ','p','p'],
##         [' ',' ','B',' ','p','R',' ',' '],
##         [' ',' ','p',' ',' ','p',' ',' '],
##         [' ',' ',' ','p',' ',' ',' ',' ']]
#############################################

board = [[' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ','p',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ','p',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ','p'],
         [' ',' ',' ','p',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ','p',' ',' '],
         [' ',' ',' ','Q',' ',' ',' ','p']]

def GetGoodPieces(board):
    '''Returns a list of 2-tuple coordinates of all "good" pieces'''
    gp = []
    for y_pos,y in enumerate(board):
        for x_pos,x in enumerate(y):
            if x in GOOD_PIECES:
                gp.append([y_pos,x_pos])
    return gp


def FindCapturablePieces(board, start_x, start_y, piece):
    '''
    @param list(list(str)) board: 2D array of current board state
    @param int start_x: column of the piece that will do the capturing
    @param int start_y: row of the piece that will do the capturing
    @param str piece: The character representation of the piece,
        used to determine which capturing strategy.

    Helper function that, when given a board and a white chess piece,
    will return the coordinates of all black pieces that it can capture.
    Supports Rooks, Knights, Bishops, Queens, and Kings, but not pawns.

    @return list: All board positions that contain capturable
        pieces for the given piece.
    '''
    capturable_pieces = []
    # If piece is Rook or Queen, test straight lines
    # It's important that we iterate in each direction
    # so that we don't get false positives on pieces that
    # are blocked.
    if piece in ['R', 'Q']:
        y,x = start_y,start_x
        # Up
        while True:
            y += 1
            if y >= len(board):
                break
            if board[y][x] in BAD_PIECES:
                capturable_pieces.append((y,x))
                break
            elif board[y][x] in GOOD_PIECES:
                break
        y,x = start_y,start_x
        # Down
        while True:
            y -= 1
            if y < 0:
                break
            if board[y][x] in BAD_PIECES:
                capturable_pieces.append((y,x))
                break
            elif board[y][x] in GOOD_PIECES:
                break
        y,x = start_y,start_x
        # Left
        while True:
            x -= 1
            if x < 0:
                break
            if board[y][x] in BAD_PIECES and x >= 0:
                capturable_pieces.append((y,x))
                break
            elif board[y][x] in GOOD_PIECES:
                break
        y,x = start_y,start_x
        # Right
        while True:
            x += 1
            if x >= len(board[y]):
                break
            if board[y][x] in BAD_PIECES:
                capturable_pieces.append((y,x))
                break
            elif board[y][x] in GOOD_PIECES:
                break

    # If piece is Bishop or Queen, test diagonals
    if piece in ['B', 'Q']:
        y,x = start_y,start_x
        # 1st quadrant diagonal
        while True:
            y += 1
            x += 1
            if y >= len(board) or x >= len(board[y]):
                break
            if board[y][x] in BAD_PIECES:
                capturable_pieces.append((y,x))
                break
            elif board[y][x] in GOOD_PIECES:
                break
        y,x = start_y,start_x
        # 2nd quadrant diagonal
        while True:
            y += 1
            x -= 1
            if y >= len(board) or x < 0:
                break
            if board[y][x] in BAD_PIECES:
                capturable_pieces.append((y,x))
                break
            elif board[y][x] in GOOD_PIECES:
                break
        y,x = start_y,start_x
        # 3rd quadrant diagonal
        while True:
            y -= 1
            x -= 1
            if y < 0 or x < 0:
                break
            if board[y][x] in BAD_PIECES:
                capturable_pieces.append((y,x))
                break
            elif board[y][x] in GOOD_PIECES:
                break
        y,x = start_y,start_x
        # 4th quadrant diagonal
        while True:
            y -= 1
            x += 1
            if y < 0 or x >= len(board[y]):
                break
            if board[y][x] in BAD_PIECES:
                capturable_pieces.append((y,x))
                break
            elif board[y][x] in GOOD_PIECES:
                break

    # If piece is a Knight, test all 8 moves
    if piece == 'N':
        y,x = start_y,start_x
        for y in (start_y-2, start_y+2):
            if 0 <= y < len(board):
                for x in (start_x-1, start_x+1):
                    if 0 <= x < len(board[y]):
                        if board[y][x] in BAD_PIECES:
                            capturable_pieces.append((y,x))
        for y in (start_y-1, start_y+1):
            if 0 <= y < len(board):
                for x in (start_x-2, start_x+2):
                    if 0 <= x < len(board[y]):
                        if board[y][x] in BAD_PIECES:
                            capturable_pieces.append((y,x))

    # If piece is a King, test all 8 moves   
    if piece == 'K':
        y,x = start_y,start_x
        for y in (start_y-1, start_y, start_y+1):
            if 0 <= y < len(board):
                for x in (start_x-1, start_x, start_x+1):
                    if 0 <= x < len(board[y]):
                        if board[y][x] in BAD_PIECES:
                            capturable_pieces.append((y,x))
        
    return capturable_pieces


def BoardCleared(board):
    '''Boolean check if there are no pawns left on the board'''
    for y in board:
        if 'p' in y:
            return False
    return True


def Coord2ChessPos(y,x):
    '''
    @params int y,x
    Converts coords used in this script to chess board notation
    This script uses top-down 0-7, then left to right 0-7 coordinates.
    Chess positions are left to right A-H, then bottom-up 1-8
    E.g. 2, 8 -> 'H6'
    @return str
    '''
    return chr(0x41+x)+str(BOARD_WIDTH-y)


def FindPathOnBoard(board, good_pieces, output_str=""):
    '''
    @param list(list(str)) board: 2D array of current board state
    @param list(2-list(int)) good_pieces: The positions of the pieces
        to be checked for ability to capture.
    @param str output_str: My homemade notation for describing the move
        progressions.

    Recursive algorithm that brute forces all possible solutions to the
    given chess board. Taking in a list of all white (good) pieces, it
    then iterates through each good piece and finds all possible moves for
    that piece that results in capturing a pawn.
    If the good piece has a move where it can capture a pawn, this script
    creates a copy of the board and the good pieces list, and alters them
    to emulate that move, then passes the altered board and pieces states
    back to itself, along with an updated solution string.
    If the function starts and the board is cleared, it adds its current
    solution string to the global list of possible solutions.
    If there are no capturable pieces for the current good piece, this
    function moves quietly onto the next good piece.
    If none of the good pieces can capture a pawn in the current board state,
    then the algorithm has found a bad branch and backs out to the previous
    recursion.

    Side-effects: Appends solutions to a global solution list

    @return None
    '''
    global solutions
    if BoardCleared(board):
        solutions.append(output_str)
        return
    for piece_index,coords in enumerate(good_pieces):
        y_pos = coords[0]
        x_pos = coords[1]
        piece = board[y_pos][x_pos]
        cap_pieces = FindCapturablePieces(board, x_pos, y_pos, piece)
        if len(cap_pieces) > 0:
            for cp_y,cp_x in cap_pieces:
                board_copy = deepcopy(board)
                good_pieces_copy = good_pieces[:]
                # Erase white piece
                board_copy[y_pos][x_pos] = ' '
                # Replace black piece with white piece
                board_copy[cp_y][cp_x] = piece
                good_pieces_copy[piece_index] = [cp_y, cp_x]
                next_succ = "{}{}>{} ".format(
                    piece, Coord2ChessPos(y_pos, x_pos),
                    Coord2ChessPos(cp_y, cp_x)
                    )
                FindPathOnBoard(board_copy, good_pieces_copy, output_str+next_succ)

                    
def FindBestSolution(solutions):
    '''
    @param list(str): a space-separated list of all possible solutions, where
        each step takes the form of "[piece][start coord]>[end coord] E.g. KA1>B3

    Not all solutions are created equal. Some solutions can require moving a single
    piece to completion. Some require moving one piece for half time, and another
    for the other half. Solutions that require "switching" pieces the least are
    preferred.
    This function goes through each part of each solution. It keeps track of how
    many times the starting coord of the next step differs from the ending coord
    of the previous step. This represents when the player switches from moving
    one piece to another.
    All solutions are added to a dictionary, organized by the number of switches.
    The dictionary is then sorted and only the solutions with the lowest number
    of switches are returned.

    @return list: Solutions with the least number of switches
    '''
    if not solutions:
        return []
    solution_dict = {}
    for solution in solutions:
        num_switches = 0
        last_space = ""
        for part in solution.split(' '):
            start = part[1:3]
            end = part[4:]
            if not last_space == start:
                num_switches += 1
            last_space = end
        solution_list = solution_dict.get(num_switches, [])+[solution]
        solution_dict[num_switches] = solution_list
    keys = sorted(solution_dict.keys())
    return solution_dict[keys[0]]


def main():
    t1 = time.time()
    good_pieces = GetGoodPieces(board)
    FindPathOnBoard(board, good_pieces)
    t2 = time.time()
    print "Time to solution:",t2-t1
    print "\n".join(FindBestSolution(solutions))

if __name__ == "__main__":
    solutions = []
    main()
