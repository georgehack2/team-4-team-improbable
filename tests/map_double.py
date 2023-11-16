from levelup.map import Map
from levelup.position import Position
from levelup.direction import Direction

class MapDouble (Map):

    STUBBED_X = 3
    STUBBED_Y = 4

    def __init__(self):
        self.starting_position = Position(self.STUBBED_X, self.STUBBED_Y)
        print("x is", self.starting_position.x)

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        # What should we return here so our character tests will work in isolation?
        return self.starting_position
