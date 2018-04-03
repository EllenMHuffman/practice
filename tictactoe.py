# from collections import defaultdict


class Board(object):

    def __init__(self):
        self.board = None
        self._height = 3
        self._width = 3
        self.moves_made = 0

        tictactoe_board = [['-'] * 3 for _ in range(3)]
        self.board = tictactoe_board

    def add_token(self, token, row, col):

        self.board[row][col] = token
        self.moves_made += 1

    def print_board(self):

        for i in range(self._height):
            print(self.board[i][0] + '|' + self.board[i][1] + '|' + self.board[i][2])
        print('')

    def is_full(self):

        if self.moves_made < (self._height * self._width):
            return False

        return True


class AI(object):

    def make_move(self, board):

        for i in range(board._height):
            for j in range(board._width):
                if board.board[i][j] == '-':
                    board.add_token('O', i, j)
                    return

        raise Exception('No legal move exists.')


class TicTacToe(object):

    def __init__(self):
        self.current_game = Board()
        self.ai_player = AI()
        self.play_game()

    def play_game(self):

        while True:
            choice = input('Choose a square (row, col) > ')
            row, col = int(choice[0]), int(choice[-1])

            self.current_game.add_token('X', row, col)
            self.current_game.print_board()

            if self.current_game.is_full():
                break

            self.ai_player.make_move(self.current_game)
            self.current_game.print_board()

            if self.current_game.is_full():
                break

new_game = TicTacToe()
