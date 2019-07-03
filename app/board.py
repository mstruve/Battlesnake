class Board:

    def __init__(self, height, width, food, you_body):
        self.board = self.empty_board(height, width)
        self.board = self.add_food(food)
        self.board = self.add_you(you_body)

    def empty_board(self, height, width):
        board = []

        for h in range(height):
            row = []
            for w in range(width):
                row.append('.')
            board.append(row)
        return board

    def add_food(self, food):
        for f in food:
            x_coord = f['x']
            y_coord = f['y']
            self.board[y_coord][x_coord] = 'F'
        return self.board

    def add_you(self, you_body):
        for b in you_body:
            x_coord = b['x']
            y_coord = b['y']
            self.board[y_coord][x_coord] = 'Y'
        return self.board

    def print_board(self):

        x_label = 1
        print("  ", end =" ")
        for coord in self.board[0]:
            if x_label < 10:
                print(x_label, end ="  ")
            else:
                print(x_label, end=" ")
            x_label += 1
        print()

        y_label = 1
        for x in self.board:
            if y_label < 10:
                print(y_label, end ="  ")
            else:
                print(y_label, end =" ")

            for coord in x:
                print(coord, end ="  ")
            print()
            y_label += 1
