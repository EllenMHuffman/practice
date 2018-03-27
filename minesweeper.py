from collections import defaultdict
from random import sample


class Square(object):

    def __init__(self):
        """Creates minesweeper square with mine and clicked attributes."""
        self.clicked = False
        self._mine = False

    def __repr__(self):
        return "<Sq clicked: {} mine: {}>".format(self.clicked, self._mine)


class Board(object):

    def __init__(self, mine_num=20, height=10, width=10):
        """Creates a 10x10 board with specified number of mines."""
        self.board = defaultdict(dict)
        self.height = height
        self.width = width

        square_qty = height * width
        mine_locs = sample(range(square_qty), mine_num)

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

        for i in range(row - 1, row + 2):
            if i >= 0 and i <= self.height:
                if col > 0:
                    neighbors.append((i, col - 1))
                if col < self.width:
                    neighbors.append((i, col + 1))
                neighbors.append((i, col))

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

    def is_mine(self, row, col):
        """Returns True if specified row and col is a mine."""

        return self.board[row][col]._mine


class Minesweeper(object):

    def __init__(self):
        self.keep_playing = True
        self.current_game = Board()
        self.start_game()

    def start_game(self):
        """Initiates minesweeper game."""

        print 'Welcome to Minesweeper!'
        response = raw_input('Current board is 10x10 with 20 mines. Press enter to begin, or type CUSTOM to modify board. > ')

        if response.lower() == 'custom':
            pass   # NEED TO UPDATE WITH CUSTOMIZE OPTIONS

        print '\nType SHOW BOARD at any time to see current status.\n'
        self.play_game()

    def play_game(self):
        """Continues play with user input."""

        while self.keep_playing:
            choice = raw_input('Choose a square (row, col) > ')

            if choice[0] == 'q':
                print 'Thanks for playing!'
                self.keep_playing = False
                continue

            if choice.lower() == 'show board':
                print self.current_game.board
                continue
            try:
                row, col = int(choice[0]), int(choice[-1])
            except ValueError:
                print 'Not a valid choice.'
                continue

            if row > self.current_game.height or col > self.current_game.width:
                print 'Not a valid choice. Your board is {}x{}'.format(self.current_game.height, self.current_game.width)

            if self.current_game.is_mine(row, col):
                print 'You chose a mine :('
                self.keep_playing = False

            self.current_game.click_square(row, col)

new_game = Minesweeper()
