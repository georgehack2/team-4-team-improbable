from levelup.position import Position
from typing import Tuple
from levelup.direction import Direction

class Map ():

    starting_position = Position(0,0)
    positions = [[0 for x in range(10)] for y in range(10)]
    size: Tuple[int, int] = (10, 10)

    # Exists for easy testing
    num_positions = size[0]*size[1]

    def __init__(self):
        for x_val in range(10):
             for y_val in range(10):
                print("x_val", x_val, "y_val", y_val)
                self.positions[x_val][y_val] = Position(x_val, y_val)
        
    def is_position_valid(self, position :Position) -> bool:
        isValid = (position.x >= 0 and position.x <= 9 and position.y >= 0 and position.y <= 9)
        return isValid

    def calculate_new_position(self, current_position: Position, direction: Direction) -> Position:
        if direction == Direction.NORTH:
            current_position.y += 1
        elif direction == Direction.SOUTH:
            current_position.y -= 1
        elif direction == Direction.EAST:
            current_position.x -= 1
        elif direction == Direction.WEST:
            current_position.x += 1 
                
        return current_position

