from collections import defaultdict
from random import sample


class Square(object):

    def __init__(self):
        """Creates minesweeper square with mine and clicked attributes."""
        self.clicked = False
        self.flagged = False
        self._mine = False

    def __repr__(self):
        return "<Sq clicked: {}>".format(self.clicked, self._mine)


class Board(object):

    def __init__(self, mine_num=20, height=10, width=10):
        """Creates a 10x10 board with specified number of mines."""
        self.board = defaultdict(dict)
        self.height = height
        self.width = width
        self.mine_num = mine_num
        self.square_qty = height * width

        mine_locs = sample(range(self.square_qty), mine_num)

        for i in range(height):
            for j in range(width):
                self.board[i][j] = Square()

        for mine in mine_locs:
            row = mine / height
            col = mine % width

            self.board[row][col]._mine = True

    def __repr__(self):
        return "<{}>".format(self.board)

    def _count_touching_mines(self, row, col):
        """Returns the number of mines surrounding given square."""
        neighbors = []
        mines_qty = 0

        for i in range(-1, 2):
            row_index = row + i
            if row_index >= 0 and row_index < self.height:
                if col > 0:
                    neighbors.append((row_index, col - 1))
                if col < self.width - 1:
                    neighbors.append((row_index, col + 1))
                neighbors.append((row_index, col))

        for neighbor in neighbors:
            if self.board[neighbor[0]][neighbor[1]]._mine:
                mines_qty += 1

        return mines_qty

    def click_square(self, row, col):
        """Updates clicked to True on game board for specified row and col."""

        if self.board[row][col].clicked:
            print self.board[row][col]
            print 'You already clicked that square. Choose another.'
        else:
            self.board[row][col].clicked = True

    def flag_square(self, row, col):
        """Flags a square with a question mark."""

        self.board[row][col].flagged = True

    def is_mine(self, row, col):
        """Returns True if specified row and col is a mine."""

        return self.board[row][col]._mine

    def display_board(self):
        """Visually represent state of board."""

        print ' ',
        for n in range(self.width):
            print ' {} '.format(n),
        print ''
        for i, row in enumerate(self.board):
            print i,
            for col in self.board[row]:
                if self.board[row][col].clicked:
                    if self.board[row][col]._mine:
                        print '[*]',
                    else:
                        mines = self._count_touching_mines(row, col)
                        print ' {} '.format(mines),
                elif self.board[row][col].flagged:
                    print '[?]',
                else:
                    print '[ ]',
            print '\n'


class Minesweeper(object):

    def __init__(self):
        self.keep_playing = True
        self.current_game = Board()
        self._click_qty = 0
        self.start_game()

    def start_game(self):
        """Initiates minesweeper game."""

        print 'Welcome to Minesweeper!'
        response = raw_input('Current board is 10x10 with 20 mines. Press enter to begin, or type CUSTOM to modify board. > ')

        if response.lower() == 'custom':
            rows = raw_input('How many rows? > ')
            cols = raw_input('How many columns? > ')
            mines = raw_input('How many mines? > ')

            try:
                self.current_game = Board(int(mines), int(rows), int(cols))
            except:
                print 'Not valid choices. Try again.'

        print '\nType SHOW BOARD at any time to see current status.\n'
        self.play_game()

    def is_win(self):
        """Check if all non-mine squares have been clicked."""

        self._click_qty += 1

        if self._click_qty == (self.current_game.square_qty -
                               self.current_game.mine_num):
            return True

        return False

    def play_game(self):
        """Continues play with user input."""

        self.current_game.display_board()

        while self.keep_playing:
            choice = raw_input('Choose a square (row, col) > ')
            print '\n'

            if choice[0] == 'q':
                print 'Thanks for playing!'
                self.keep_playing = False
                continue

            if choice.lower() == 'show board':
                self.current_game.display_board()
                continue

            if choice[:4].lower() == 'flag':
                try:
                    row, col = int(choice[5]), int(choice[-1])
                except ValueError:
                    print 'Not a valid choice.'
                    continue

                if row > self.current_game.height or col > self.current_game.width:
                    print 'Not a valid choice. Your board is {}x{}'.format(self.current_game.height, self.current_game.width)
                    continue

                self.current_game.flag_square(row, col)

            else:
                try:
                    row, col = int(choice[0]), int(choice[-1])
                except ValueError:
                    print 'Not a valid choice.'
                    continue

                if row > self.current_game.height or col > self.current_game.width:
                    print 'Not a valid choice. Your board is {}x{}'.format(self.current_game.height, self.current_game.width)
                    continue

                if self.current_game.is_mine(row, col):
                    print 'You landed on a mine :('
                    self.keep_playing = False

                self.current_game.click_square(row, col)

                if self.is_win():
                    print 'Congratulations! You won!'
                    self.keep_playing = False

            self.current_game.display_board()

new_game = Minesweeper()
