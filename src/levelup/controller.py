from levelup.character import Character
from levelup.direction import Direction
from levelup.map import Map
from levelup.position import Position




class GameStatus:
    character_name: str = ""
    CURRENT_POS_ICON: str = "@"
    STARTING_POS_ICON: str = "S"
    EMPTY_POS_ICON: str = "."
    SEPARATOR: str = " "
    start_position: tuple = (-100,-100)
    current_position: tuple = (-100,-100)
    move_count: int = 0
    map: Map = None

    def __str__(self) -> str:
        message: str = "" 
        
        str = f"{self.character_name} is currently on {self.current_position} and moved {self.move_count} times."

        y: int = len(self.map.positions[0])

        while y > 0:
            y -= 1
            str += "\n"

            x: int = 0

            while x < len(self.map.positions[1]):
                if x == self.current_position[0] and y == self.current_position[1]:
                    str += self.CURRENT_POS_ICON
                elif x == self.start_position[0] and y == self.start_position[1]:
                    str += self.STARTING_POS_ICON
                else:
                    str += self.EMPTY_POS_ICON
                x += 1
                str += self.SEPARATOR

        return str

class GameController:
    status: GameStatus
    character: Character
    map: Map
    TREASURE_COORDINATES: tuple[int, int] = (8, 8)
    is_finished: bool = False

    def __init__(self):
        self.status = GameStatus()


    def start_game(self):
        self.map = Map()

        self.character.enter_map(self.map)
        # Status code is written for you
        self.status.map = self.map
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.start_position = self.status.current_position
        self.status.move_count = 0

    # Pre-written for you
    def create_character(self, character_name: str) -> None:
        self.character = Character(character_name)
        self.status.character_name = self.character.name

    def move(self, direction: Direction) -> None:
        self.character.move(direction)
        # Status code is written for you
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.move_count = self.status.move_count + 1

        if self.status.current_position == self.TREASURE_COORDINATES:
            print("\n\n\nYou found a PIZZA!!!\n\n\n")

            print("""
                     _____
              __--~~~     ~~~--__
           ,/'   m%%%%%%%=@%%m   `\.
         /'  m%%%o(_)%%o%%o%%%o%%m  `\\
       /'  %%@=%o%%%%o%%%o%%(_)o%%%%  `\\
     /'  %%%o%%%%%=@%%%(_)%%o%%%o%@=%%  `\\
    /  %(_)%%(_)%%%o%%%o%%%%=@(_)%%%o%%%  \\
   /  @=%%%o%%%%o%%%(_)%%o%%o%%%%o%%%o%%%  \\
  |  %%o%%%%=@%%%o%%%%@=%(_)%%=@%%(_)%o%%%  |
 |  %%%%(_)%%%%o%(_)o%%o%%%o%%%%o%%o%o@=%o%  |
 |  %%o%o%%o%%%%o%%o%%o%%%%=@%o(_)%%o%o%%%%  |
 |  %(_)%%%%(_)%=@%%%(_)o%%%o%%o%%@=%%(_)%%  |
 |  %%o%(_)%%%%%o%%%%%%=@%%(_)%%o%%%o%%%%%%  |
  |  %%o%%%%o%%%%(_)o%%%%o%o%%@=%(_)%%=@%%  |
   \  %@=%%o%(_)%%%%%o%(_)%%%o%%o%%o%%%%%  /
    \  %%(_)%%%=@%(_)%o%o%%(_)%o%(_)%@=%  /
     \. ~%%%o%%%%%o%o%=@%%o%%@=%%o%%o%% ,/
       \. ~o%%(_)%%%%%o%(_)%%o%(_)o%% ,/
         \_ ~%%o%=@%(_)%%o%%(_)%%~  ,/
           `\__~~~o%%%%o%%%%%~  __/'
               `~--.._____,,--~'
            """)
            input("\n\n\nPress enter when you've eaten your pizza....")
            print("\n\nYou need to wash that pizza down with some cold beer!\n\n")
            print("""
      .   *   ..  . *  *
    *  * @()Ooc()*   o  .
        (Q@*0CG*O()   ___
        |\\_________/|/ _ \\
        |  |  |  |  | / | |
        |  |  |  |  | | | |
        |  |  |  |  | | | |
        |  |  |  |  | | | |
        |  |  |  |  | | | |
        |  |  |  |  | \\_| |
        |  |  |  |  |\___/
        |\\_|__|__|_/|
         \\_________/
            """)

            self.is_finished = True
            

    ## ************************************************
    ## METHODS THAT EXIST JUST TO HELP WITH TESTING -- PREWRITTEN FOR YOU
    ## ************************************************
    def set_character_position(self, xycoordinates: tuple) -> None:
        x = xycoordinates[0]
        y = xycoordinates[1]
        self.character.current_position = Position(x,y)
        self.status.current_position = xycoordinates

    def set_current_move_count(self, move_count: int) -> None:
        self.status.move_count = move_count

    def get_total_positions(self) -> int:
        return self.map.num_positions
    
    def initalize_game_for_testing(self) -> None:
        self.create_character("")
        self.start_game()

    
