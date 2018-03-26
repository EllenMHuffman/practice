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

    def __init__(self, mine_num, height=10, width=10):
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
        square = raw_input('row, col > ')
        row, col = int(square[0]), int(row[-1])

        if self.board[row][col]:
            print 'You already clicked that square. Choose another.'
        else:
            self.board[row][col].clicked = True

    def is_mine(self, row, col):
        """Returns True if specified row and col is a mine."""

        return self.board[row][col]._mine

    def is_clicked(self, row, col):
        """Returns True if specified square has been clicked."""

        return self.board[row][col].clicked
