from levelup.position import Position
from typing import Tuple
from levelup.direction import Direction

class Map ():

    starting_position = Position(5,5)
    positions = [[0 for x in range(10)] for y in range(10)]
    size: Tuple[int, int] = (10, 10)

    # Exists for easy testing
    num_positions = size[0]*size[1]

    def __init__(self):
        for x_val in range(10):
             for y_val in range(10):
                self.positions[x_val][y_val] = Position(x_val, y_val)
        
    def is_position_valid(self, position :Position) -> bool:
        isValid = (position.x >= 0 and position.x <= 9 and position.y >= 0 and position.y <= 9)
        return isValid

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:

        x : int = current_position.x
        y : int = current_position.y

        if direction == Direction.NORTH:
            y += 1
        elif direction == Direction.SOUTH:
            y -= 1
        elif direction == Direction.EAST:
            x += 1
        elif direction == Direction.WEST:
            x -= 1 

        if self.is_position_valid(Position(x, y)):
            current_position = self.positions[x][y]

        return current_position

