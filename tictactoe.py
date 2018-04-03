from random import choice


class Board(object):

    def __init__(self):
        self.board = ['-'] * 9
        self._height = 3
        self._width = 3
        self.moves_made = 0

    def add_token(self, token, location):

        if self.board[location - 1] == '-':
            self.board[location - 1] = token
            self.moves_made += 1
        else:
            print('Lose a turn! That square was already taken.')

    def print_board(self):

        for i in range(0, 8, 3):
            print(self.board[i] + '|' + self.board[i + 1] + '|' + self.board[i + 2])
        print('')

    def is_full(self):

        if self.moves_made < len(self.board):
            return False

        return True


class AI(object):

    def make_move(self, board):

        valid_moves = []

        for i in range(len(board.board)):
            if board.board[i] == '-':
                valid_moves.append(i)

        if not valid_moves:
            raise Exception('No legal move exists.')

        move = choice(valid_moves)
        board.add_token('O', move + 1)


class TicTacToe(object):

    def __init__(self):
        self.current_game = Board()
        self.ai_player = AI()
        self.play_game()

    def is_win(self, letter):

        win = ((self.current_game.board[0] == letter and
                self.current_game.board[1] == letter and
                self.current_game.board[2] == letter) or
               (self.current_game.board[3] == letter and
                self.current_game.board[4] == letter and
                self.current_game.board[5] == letter) or
               (self.current_game.board[6] == letter and
                self.current_game.board[7] == letter and
                self.current_game.board[8] == letter) or
               (self.current_game.board[0] == letter and
                self.current_game.board[3] == letter and
                self.current_game.board[6] == letter) or
               (self.current_game.board[1] == letter and
                self.current_game.board[4] == letter and
                self.current_game.board[7] == letter) or
               (self.current_game.board[2] == letter and
                self.current_game.board[5] == letter and
                self.current_game.board[8] == letter) or
               (self.current_game.board[0] == letter and
                self.current_game.board[4] == letter and
                self.current_game.board[8] == letter) or
               (self.current_game.board[2] == letter and
                self.current_game.board[4] == letter and
                self.current_game.board[6] == letter))

        if not win and self.current_game.is_full():
            return None

        return win

    def play_game(self):

        print('Game locations:\n')
        print('1|2|3')
        print('4|5|6')
        print('7|8|9')

        while True:
            choice = input('Your turn. Choose a square > ')

            if choice in '1 2 3 4 5 6 7 8 9'.split():
                self.current_game.add_token('X', int(choice))
            self.current_game.print_board()

            status = self.is_win('X')
            if status is None:
                print('The game is tied!')
                break
            elif status:
                print('You win!')
                break

            print("Computer's turn > ")
            self.ai_player.make_move(self.current_game)
            self.current_game.print_board()

            status = self.is_win('O')
            if status is None:
                print('The game is tied!')
                break
            elif status:
                print('The computer won :(')
                break

new_game = TicTacToe()
