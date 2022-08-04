# Name: Cassidy Unpingco
# Date: 12/03/21
# Description: a class called HasamiShogiGame that represents a board game with a BLACK and RED player.
# Each player has 9 pieces and their objective is to capture all but one of their opponents pieces.

class HasamiShogiGame:
    """
    a class named HasamiShogiGame for playing an
    abstract board game called hasami shogi. The
    winning objective is to capture all but one of
    the opponent's men. Each player has nine men.
    Black always starts first.
    """

    def __init__(self):
        """
        Takes no parameters. This is the constructor to initialize data members and all data members are private.
        """
        self._board = [['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
                       ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]

        self._game_state = 'UNFINISHED'
        self._active_player = 'BLACK'
        self._winner = False
        self._num_captured_pieces = {
            'RED':0,
            'BLACK':0
        }
        self._pieces = ['R','B','.']

    def the_board(self, row,col):
        """
        the board method that calls rows and columns of the self._board based on inputs. This method is utilized
        in get_square_occupant method.
        """
        return self._board[row][col]



    def set_the_board(self, arg_pos, character):
        """
        set_the_board is a method that updates the board
        """
        result = self.change_algnote(arg_pos)
        self._board[result[0]][result[1]] = character


    def get_board(self):
        """
        get method that returns self._board private data member without accessing it directly within the code
        """
        return self._board

    def update_board(self, start_alg, new_alg, piece):
        """
        update_board method updates the HasamiShogi board based on player movement.
        """
        start_alg = self.change_algnote(start_alg)
        new_alg = self.change_algnote(new_alg)
        # UP
        if new_alg[0] < start_alg[0]:
            if (self.is_inbounds(new_alg)) and (self.is_inbounds(start_alg)) != ".":
                self.set_the_board(new_alg, piece)

        # DOWN
        if new_alg[0]> start_alg[0]:
            if (self.is_inbounds(new_alg)) and (self.is_inbounds(start_alg)) != ".":
                self.set_the_board(new_alg, piece)
        # RIGHT
        if new_alg[1] > start_alg[1]:
            if (self.is_inbounds(new_alg)) and (self.is_inbounds(start_alg)) != ".":
                self.set_the_board(new_alg, piece)
        # LEFT
        if new_alg[1] < start_alg[1]:
            if (self.is_inbounds(new_alg)) and (self.is_inbounds(start_alg)) != ".":
                self.set_the_board(new_alg, piece)

    def print_board(self):
        """
        This method would print the current Hasami Shogi game board
        """
        alpha ='abcdefghi'
        alpha1=chr((ord('abcdefghi'[0])))
       # for x in alpha:
        #    print(x)

        pieces={
            'RED': 'R', 'BLACK':'B', None:'.'
        }
        for index in range(0,10):
            if index == 0:
                print(" ",  end= '')
            elif index !=9:
                print('  ', index, end=' ',)
            else:
                print("  ",index," ", end= "\n")
        for index, row in enumerate(self._board):
            for x in alpha:
                print(x, index, row)
            return


        # for row in range(0, len(self.get_board())):
        #     print(''.join(self.get_board()[row]))
    def get_game_state(self):
        """
        A method called get_game_state that takes
        no parameters and returns 'UNFINISHED', 'RED_WON' or 'BLACK_WON'.
        """
        return self._game_state

    def set_game_state(self, new_state):
        """
        setter method called set_game_state that changes the current game state to one of the three options:
        new_state ='RED_WON, 'BLACK_WON', or 'UNFINISHED
        """
        self._game_state = new_state

    def get_active_player(self):
        """
        A method called get_active_player that takes no parameters and
        returns whose turn it is - either 'RED' or 'BLACK'.
        """
        return self._active_player

    def set_active_player(self, color):
        """
        setter method called set_active_player that takes one parameter, color.
        Color = 'BLACK' or 'RED'
        """

        self._active_player = color

    def get_winner(self):
        """
        get method for private member _winner, returns winner
        """
        return self._winner

    def set_winner(self, winner):
        """
        set method for private member _winner, changes winner.
        """
        self._winner = winner

    def get_num_captured_pieces(self, color): #finished code
        """
        A method called get_num_captured_pieces that takes one parameter,
        'RED' or 'BLACK', and returns the number of pieces of that color
        that have been captured.
        color - represents number of red or black pieces removed from the board
        """
        if color == 'RED':
            flat_list = [index for item in self._board for index in item]
            count = len([elem for elem in flat_list if elem == 'R'])
            self._num_captured_pieces.update({'RED': 9 - count })
            return self._num_captured_pieces['RED']
        elif color == 'BLACK':
            flat_list = [index for item in self._board for index in item]
            count = len([elem for elem in flat_list if elem == 'B'])
            self._num_captured_pieces.update({'BLACK': 9 - count})
            return self._num_captured_pieces['BLACK']

    def remove_captured_piece(self, square_info):
        """
        I still need to have the pieces be removed once a capture is valid from a player move
        """
        self.custodial_capture(square_info)

        if square_info == ('a1' or 'a9' or 'i1' or 'i9'):
            self.corner_capture(square_info)
            
    def custodial_capture(self, square_info):
        self.capture_up(square_info)
        #self.capture_down(square_info)
        self.capture_right(square_info)
        # self.capture_left(square_info)

    def capture_down(self, square_info):
        """
        from square_info and up --- delete until i find myself again
        scan and if next is other player,
        then continue until end of board OR
        find another piece i own
        1) go from start (start_square)
        2) go up one (next_square)
        3) if next_square == yourself, then return
        4) if next_square out of bounds, then return
        4) if next_square == empty, then return
        5) if next_square == enemy, then move square and repeat #5
            a) until you encounter yourself
            b) if true, then delete everything between next_square and start_square
        """
        start_square = square_info
        next_square = self.get_next_down_location(start_square)
        if next_square == '.' or next_square[0] == '`' or next_square[1] == ':':
            return
        if self.get_square_occupant(next_square) != self.get_active_player():
            while self.get_square_occupant(next_square) != self.get_active_player()[0]:
                next_square = self.get_next_down_location(next_square)
                if next_square == '.' or next_square[0] == '`' or next_square[1] == ':':
                    return
                if self.get_square_occupant(next_square) == self.get_active_player():
                    target_square = next_square
                    # self.delete_up_between(square_info, next_square) # delete every in between non-inclusive
                    next_square = start_square
                    while next_square != target_square:
                        next_square = self.get_next_down_location(next_square)
                        if self.get_square_occupant(next_square) != self.get_active_player():
                            self.set_the_board(next_square, '.')


    def capture_up(self, square_info):
        """
        from square_info and up --- delete until i find myself again
        scan and if next is other player,
        then continue until end of board OR
        find another piece i own
        1) go from start (start_square)
        2) go up one (next_square)
        3) if next_square == yourself, then return
        4) if next_square out of bounds, then return
        4) if next_square == empty, then return
        5) if next_square == enemy, then move square and repeat #5
            a) until you encounter yourself
            b) if true, then delete everything between next_square and start_square
        """
        start_square = square_info
        next_square = self.get_next_up_location(start_square)
        if next_square[0] == '`' or next_square[1] == ':' or next_square is None:
            return
        if self.get_square_occupant(next_square) != self.get_active_player():
            while self.get_square_occupant(next_square) != self.get_active_player()[0]:
                next_square = self.get_next_up_location(next_square)
                if next_square[0] == '`' or next_square[1] == ':' or next_square is None:
                    return
                if self.get_square_occupant(next_square) == self.get_active_player():
                    target_square = next_square
                    # self.delete_up_between(square_info, next_square) # delete every in between non-inclusive
                    next_square = start_square
                    while next_square != target_square:
                        next_square = self.get_next_up_location(next_square)
                        if self.get_square_occupant(next_square) != self.get_active_player():
                            self.set_the_board(next_square, '.')

    def capture_left(self, square_info):
        """
        from square_info and up --- delete until i find myself again
        scan and if next is other player,
        then continue until end of board OR
        find another piece i own
        1) go from start (start_square)
        2) go up one (next_square)
        3) if next_square == yourself, then return
        4) if next_square out of bounds, then return
        4) if next_square == empty, then return
        5) if next_square == enemy, then move square and repeat #5
            a) until you encounter yourself
            b) if true, then delete everything between next_square and start_square
        """
        start_square = square_info
        next_square = self.get_next_left_location(start_square)
        if next_square[0] == ':' or next_square[1] == '`' or next_square is None:
            return
        if self.get_square_occupant(next_square) != self.get_active_player():
            while self.get_square_occupant(next_square) != self.get_active_player()[0]:
                next_square = self.get_next_left_location(next_square)
                if next_square[0] == ':' or next_square[1] == '`' or next_square is None:
                    return
                if self.get_square_occupant(next_square) == self.get_active_player():
                    target_square = next_square
                    # self.delete_up_between(square_info, next_square) # delete every in between non-inclusive
                    next_square = start_square
                    while next_square != target_square:
                        next_square = self.get_next_left_location(next_square)
                        if self.get_square_occupant(next_square) != self.get_active_player():
                            self.set_the_board(next_square, '.')

    def capture_right(self, square_info):
        """
        from square_info and up --- delete until i find myself again
        scan and if next is other player,
        then continue until end of board OR
        find another piece i own
        1) go from start (start_square)
        2) go up one (next_square)
        3) if next_square == yourself, then return
        4) if next_square out of bounds, then return
        4) if next_square == empty, then return
        5) if next_square == enemy, then move square and repeat #5
            a) until you encounter yourself
            b) if true, then delete everything between next_square and start_square
        """
        start_square = square_info
        next_square = self.get_next_right_location(start_square)
        if next_square[0] == '`' or next_square[1] == ':' or next_square is None:
            return
        if self.get_square_occupant(next_square) != self.get_active_player():
            while self.get_square_occupant(next_square) != self.get_active_player()[0]:
                next_square = self.get_next_right_location(next_square)
                if next_square[0] == '`' or next_square[1] == ':' or next_square is None:
                    return
                if self.get_square_occupant(next_square) == self.get_active_player():
                    target_square = next_square
                    # self.delete_up_between(square_info, next_square) # delete every in between non-inclusive
                    next_square = start_square
                    while next_square != target_square:
                        next_square = self.get_next_right_location(next_square)
                        if self.get_square_occupant(next_square) != self.get_active_player():
                            self.set_the_board(next_square, '.')

    def corner_capture(self):
        """
        define corner capture rules
        """
        #bottom_right
        for occupant in range (-1,1):
            for RED in self._board:
                if self.get_square_occupant('i9') == 'RED':
                    if (self.get_square_occupant('h9') == 'BLACK') and (self.get_square_occupant('i8') == 'BLACK'):
                        self.set_the_board(self.change_algnote('i9'),'.')
        if self.get_square_occupant('i9') == 'BLACK':
            if self.get_square_occupant('h9') == 'RED' and self.get_square_occupant('i8') == 'RED':
                self.set_the_board(self.change_algnote('i9'),'.')
        # top right
        if self.get_square_occupant('a9') == 'RED':
            if self.get_square_occupant('b9') == 'BLACK' and self.get_square_occupant('a8') == 'BLACK':
                self.set_the_board(self.change_algnote('a9'), '.')
        if self.get_square_occupant('i9') == 'BLACK':
            if self.get_square_occupant('b9') == 'RED' and self.get_square_occupant('a8') == 'RED':
                self.set_the_board(self.change_algnote('a9'), '.')
        # bottom left
        if self.get_square_occupant('i1') == 'RED':
            if self.get_square_occupant('h1') == 'BLACK' and self.get_square_occupant('i2') == 'BLACK':
                self.set_the_board(self.change_algnote('i1'), '.')
        if self.get_square_occupant('i1') == 'BLACK':
            if self.get_square_occupant('h1') == 'RED' and self.get_square_occupant('i2') == 'RED':
                self.set_the_board(self.change_algnote('i1'),  '.')
        # top left
        if self.get_square_occupant('a1') == 'RED':
            if self.get_square_occupant('b1') == 'BLACK' and self.get_square_occupant('a2') == 'BLACK':
                self.set_the_board(self.change_algnote('a1'), '.')
        if self.get_square_occupant('a1') == 'BLACK':
            if self.get_square_occupant('b1') == 'RED' and self.get_square_occupant('a2') == 'RED':
                self.set_the_board(self.change_algnote('a1'), '.')

    def get_pieces(self, color):
        """
        A method called get_pieces that returns the player pieces.
        """
        if color == 'RED':
            return 'R'
        if color == 'BLACK':
            return 'B'
        if color == None:
            return '.'

    def change_cords(self, row, column):
        """
        This method takes two parameters to covert the lists of lists to a algebraic notation position
        to handle movement in the game, with row being first.
        row - represents the row (a-i)
        column - represents 1-9 positions within the list of lists
        """
        row_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        column_nums = [str(num) for num in range(0,9)]
        rows = row_letters[row]
        column_coord = column_nums[column]
        change_coords = [rows + column_coord]
        return change_coords

    def change_algnote(self, alg_note):
        """
        This method takes one parameter to covert the algebraic notation position back to a coordinate tuple
        to handle movement in the game, with row being first.
        """
        row_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        rows = alg_note[0]
        column = alg_note[1]
        if rows in row_letters:
            row = row_letters.index(rows)
            col = int(column)-1
            coord_pos1 = row
            coord_pos2 = col
            return coord_pos1,coord_pos2
    def change_algnote_board_pass(self, alg_note):
        """
        helper function that passes algnote to the board

        """
        row_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        rows = alg_note[0]
        column = alg_note[1]
        if rows in row_letters:
            row = row_letters.index(rows)
            col = int(column) - 1
            coord_pos1 = row
            coord_pos2 = col
        return self.the_board(coord_pos1,coord_pos2)

    def make_move(self, start_square, target_square):
        """
        A method called make_move that takes two parameters - strings that
        represent the square moved from and the square moved to. For example,
        make_move('b3', 'b9').
        If the square being moved from does not contain a piece belonging to the player whose turn it is,
        or if the indicated move is not legal,
        or if the game has already been won, then it should just return False.
        Otherwise it should make the indicated move,
        remove any captured pieces,
        update the game state if necessary,
        update whose turn it is, and return True.
        start_square = is the position of the piece currently
        target_square = is the position the player want to move their piece to
        """

        self.attempt_record_move(start_square,target_square)

    def attempt_record_move(self,start_square, target_square):
        """
        attempt_record_move tries to make move and then record
        All have to be true, else return False
        1) check if start_square is occupied
        2) check if start square has current active player
        3) check game status
        4) check target square not occupied
        5) check if move direction valid
        6) check path to target square no collisions

        Now, if all above are true, then
        1) record move
        2) update captures (remove pieces)
        3) update game status
        4) switch players
        """
        if self.get_square_occupant(start_square) is None:
            return False
        if self.get_square_occupant(start_square) != self.get_active_player():
            return False
        if self.get_game_state() != 'UNFINISHED':
            return False
        if self.get_square_occupant(target_square) is not None:
            return False
        if self.get_direction(start_square, target_square) == 'INVALID':
            return False
        if self.is_collision(start_square, target_square, self.get_direction(start_square, target_square)):
            return False

        # print(self.get_active_player()[0])
        self.set_the_board(target_square, self.get_active_player()[0])
        self.set_the_board(start_square, '.')
        self.remove_captured_piece(target_square)
        self.update_state()
        self.switch_player()

    def update_state(self): # finished code
        #if 1 or 0 red pieces then 'BLACK_WON'
        if self.get_num_captured_pieces('RED') == (8 or 9):
            self.set_game_state('BLACK_WON')
            return self.get_game_state()
        elif self.get_num_captured_pieces('BLACK') == (8 or 9):
            self.set_game_state('RED_WON')
            return self.get_game_state()
        else:
            return False

    def get_square_occupant(self, square_info): #finished code
        """
        A method called get_square_occupant that takes one parameter, a string
        representing a square (such as 'i7'), and returns 'RED', 'BLACK', or
        None, depending on whether the specified square is occupied by a red
        piece, a black piece, or neither.
        """
        result = self.change_algnote_board_pass(square_info)
        if result == 'B':
            return 'BLACK'
        elif result == 'R':
            return 'RED'
        else:
            return None

    def switch_player(self): #finished code
        """
        A method called switch player that takes two parameters
        Active player- is the current player that has made a valid move and now cannot make a valid move
        Next player – is the player that before active player made a move could not make a valid move now post active
        player move can make a valid move
        """

        if self.get_active_player() == 'BLACK':
            return (True and self.set_active_player('RED'))
        elif self.get_active_player() == 'RED':
            return (True and self.set_active_player('BLACK'))

    def direction_valid(self, direction):
        """
        returns true or false if direction is valid
        """
        if direction == "INVALID":
            return False
        if direction == None:
            return False
        return True

    def is_inbounds(self, num):
        """
        checks if inbounds
        num- algebraic notation a10 or a1
        """
        return num < 9 and num >= 0

    def get_direction(self, square_string_1, square_string_2):

        """
        returns direction of move to help verify it is allowed
        """
        self.change_algnote(square_string_1)
        self.change_algnote(square_string_2)
        # DOWN
        if (square_string_1[1] == square_string_2[1]) and (square_string_1[0] < square_string_2[0]):
            return 'DOWN'
        # UP
        if (square_string_1[1] == square_string_2[1]) and (square_string_1[0] > square_string_2[0]):
            return 'UP'
        # LEFT
        if (square_string_1[0] == square_string_2[0]) and (square_string_1[1] > square_string_2[1]):
            return 'LEFT'
        # RIGHT
        if (square_string_1[0] == square_string_2[0]) and (square_string_1[1] < square_string_2[1]):
            return 'RIGHT'
        else:
            return "INVALID"

    def is_collision(self, start_square, target_square, direction):
        """
        #checks if there's a collision with another piece
       #row- a-i
       #col – 1-9
       Remap
       All have to be true to
       From start to target iterate based on direction, and make sure nothing is in between
        """

        # get_square_occupant(square_location)
        # UP ---> square_info e.g. location = a1
        #           increment the location in the UP direction
        #           get_square_occupant(at_new_location)

        if direction == 'UP': # up
            next_square = self.get_next_up_location(start_square)
            while self.get_square_occupant(next_square) == None:
                if next_square == target_square:
                    return False
                next_square = self.get_next_up_location(next_square)
                if self.get_square_occupant(next_square) != None:
                    return True
        if direction == 'DOWN': # down
            next_square = self.get_next_down_location(start_square)
            while self.get_square_occupant(next_square) == None:
                if next_square == target_square:
                    return False
                next_square = self.get_next_down_location(next_square)
                if  self.get_square_occupant(next_square) != None:
                    return True
        if direction == 'LEFT': # left
            next_square = self.get_next_left_location(start_square)
            while self.get_square_occupant(next_square) == None:
                if next_square == target_square:
                    return False
                next_square = self.get_next_left_location(next_square)
                if  self.get_square_occupant(next_square) != None:
                    return True
        if direction == 'RIGHT': # right
            next_square = self.get_next_right_location(start_square)
            while self.get_square_occupant(next_square) == None:
                if next_square == target_square:
                    return False
                next_square = self.get_next_right_location(next_square)
                if  self.get_square_occupant(next_square) != None:
                    return True

        return False

    def get_next_up_location(self, square_info):
        # up
        return chr(ord(square_info[0]) - 1) + square_info[1]

    def get_next_down_location(self, square_info):
        # down
        return chr(ord(square_info[0]) + 1) + square_info[1]

    def get_next_right_location(self, square_info):
        # right
        return square_info[0] + chr(ord(square_info[1]) + 1)

    def get_next_left_location(self, square_info):
        # left
        return square_info[0] + chr(ord(square_info[1]) - 1)


#print(game.get_game_state())
#print(game.get_active_player())
#print(game.get_num_captured_pieces('BLACK'))
#game.print_board()
#game.set_active_player('RED')
#print(game.get_active_player())
#print(game.get_square_occupant('a2'))
#print(game.change_algnote('a1'))
#print(game.get_pieces('RED'))
#print(game.update_pieces('RED',7))
#print(game.get_pieces('BLACK'))
#print(game.get_num_captured_pieces('RED'))
game = HasamiShogiGame()
game.print_board()




