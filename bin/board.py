class GameBoard:
    def __init__(self, size):
        self.board = [["_"] * size] * size
        self.size = size

    def __str__(self):
        pass

    def get_size(self):
        return self.size

    def reset_board_size(self, size):
        pass

    def change_size(self, size: int):
        pass
