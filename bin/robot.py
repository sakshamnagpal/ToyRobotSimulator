class ToyRobot:
    def __init__(self):
        self.x_coordinate = None
        self.y_coordinate = None
        self.face = None
        self.placed = False

    def __str__(self):
        pass

    def get_x_value(self):
        return self.x_coordinate

    def get_y_value(self):
        return self.y_coordinate

    def get_face_value(self):
        return self.face

    def is_placed(self):
        pass

    def place(self, x, y, face):
        pass

    def move(self):
        pass

    def left(self):
        pass

    def right(self):
        pass
