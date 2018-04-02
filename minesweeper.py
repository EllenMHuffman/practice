from random import sample


class Square(object):

    def __init__(self, mine):
        """Creates minesweeper square with mine and clicked attributes."""
        self.clicked = False
        self.flagged = False
        self._mine = mine

    def __repr__(self):
        return "<Square clicked: {} mine: {}>".format(self.clicked, self._mine)


class Board(object):

    def __init__(self, mine_num=20, height=10, width=10):
        """Creates a 10x10 board with specified number of mines."""
        self.board = [[None] * width for _ in range(height)]
        self.height = height
        self.width = width
        self.mine_num = mine_num
        self.square_count = height * width
        self.click_count = 0

        mine_locs = sample(range(self.square_count), mine_num)
        mine_coordinates = set()

        for mine in mine_locs:
            row = int(mine / height)
            col = int(mine % width)

            mine_coordinates.add((row, col))

        for i in range(height):
            for j in range(width):
                mine = False
                if (i, j) in mine_coordinates:
                    mine = True

                self.board[i][j] = Square(mine)

    def __repr__(self):
        return "<Board {}>".format(self.board)

    def _count_touching_mines(self, row, col):
        """Returns the number of mines surrounding given square."""
        mines_count = 0

        for i in range(-1, 2):
            row_index = row + i
            if row_index >= 0 and row_index < self.height:
                if col > 0:
                    if self.board[row_index][col - 1]._mine:
                        mines_count += 1
                if col < self.width - 1:
                    if self.board[row_index][col + 1]._mine:
                        mines_count += 1
                if self.board[row_index][col]._mine:
                    mines_count += 1

        return mines_count

    def click_square(self, row, col):
        """Updates clicked to True on game board for specified row and col."""

        if self.board[row][col].clicked:
            print('You already clicked that square. Choose another.')
        else:
            self.board[row][col].clicked = True
            self.click_count += 1

    def flag_square(self, row, col):
        """Flags a square with a question mark."""

        self.board[row][col].flagged = not self.board[row][col].flagged

    def is_mine(self, row, col):
        """Returns True if specified row and col is a mine."""

        return self.board[row][col]._mine

    def display_board(self):
        """Visually represent state of board."""

        print(' ', end='')
        for n in range(self.width):
            print(' {} '.format(n), end=''),
        print('\n', end='')
        for i, row in enumerate(self.board):
            print(i, end='')
            for j, col in enumerate(self.board[i]):
                if self.board[i][j].clicked:
                    if self.board[i][j]._mine:
                        print('[*]', end='')
                    else:
                        mines = self._count_touching_mines(i, j)
                        print(' {} '.format(mines), end='')
                elif self.board[i][j].flagged:
                    print('[?]', end='')
                else:
                    print('[ ]', end='')
            print('\n', end='')

    def reveal_mines(self):
        """Visually represent state of board to reveal all mines."""

        print(' ', end='')
        for n in range(self.width):
            print(' {} '.format(n), end=''),
        print('\n', end='')
        for i, row in enumerate(self.board):
            print(i, end='')
            for j, col in enumerate(self.board[i]):
                if self.board[i][j]._mine:
                    print('[*]', end='')
                elif self.board[i][j].clicked:
                    mines = self._count_touching_mines(i, j)
                    print(' {} '.format(mines), end='')
                else:
                    print('[ ]', end='')
            print('\n', end='')


class Minesweeper(object):

    def __init__(self):
        self.current_game = Board()
        self.start_game()

    def start_game(self):
        """Initiates minesweeper game."""

        print('Welcome to Minesweeper!')
        response = input('Current board is 10x10 with 20 mines. Press enter to begin, or type CUSTOM to modify board. > ')

        if response.lower() == 'custom':
            try:
                rows = int(input('How many rows? > '))
                cols = int(input('How many columns? > '))
                mines = int(input('How many mines? > '))
                self.current_game = Board(mines, rows, cols)
            except ValueError:
                print('Not valid choice. Default settings applied. \n')

        print('\nType SHOW BOARD at any time to see current status.\n')
        self.play_game()

    def is_win(self):
        """Check if all non-mine squares have been clicked."""

        if self.current_game.click_count == (self.current_game.square_count -
                                             self.current_game.mine_num):
            return True

        return False

    def validate_choice(self, choice):
        """Validates whether user's square choice is a valid selection."""
        try:
            row, col = choice.split(',')
            row, col = int(row), int(col)
        except ValueError:
            print('Not a valid choice.')

            return False

        if ((row > self.current_game.height or row < 0)
                or (col > self.current_game.width or col < 0)):

            print('Not a valid choice. Your board is {}x{}'.format(self.current_game.height, self.current_game.width))

            return False

        return True

    def play_game(self):
        """Continues play with user input."""

        self.current_game.display_board()

        while True:
            choice = input('Choose a square (row, col) > ')
            print('\n')

            if choice[0] == 'q':
                print('Thanks for playing!')
                break

            if choice.lower() == 'show board':
                self.current_game.display_board()
                continue

            if choice[:4].lower() == 'flag':
                if not self.validate_choice(choice[5:]):
                    continue
                row, col = int(choice[5]), int(choice[-1])
                self.current_game.flag_square(row, col)

            else:
                if not self.validate_choice(choice):
                    continue

                row, col = int(choice[0]), int(choice[-1])

                if self.current_game.is_mine(row, col):
                    print('You landed on a mine :(')
                    self.current_game.reveal_mines()
                    break

                self.current_game.click_square(row, col)

                if self.is_win():
                    print('Congratulations! You won!')
                    self.current_game.reveal_mines()
                    break

            self.current_game.display_board()

new_game = Minesweeper()
