import logging
from typing import Callable
from levelup.controller import GameController
from levelup.direction import Direction

VALID_DIRECTIONS = [x.value for x in Direction]
VALID_COMMANDS = VALID_DIRECTIONS + ['q']
# This is prewritten for you. You should only have to change it to make the text copy match what your prompts should say
class GameApp:

    controller: GameController
    starting_pos = (-100,-100)

    def __init__(self):
        self.controller = GameController()

    def prompt(self, menu: str, validation_fn: Callable[[str], bool]) -> str:
        while True:
            response = input(f"\n{menu}\n> ")
            if validation_fn(response):
                break
            else:
                print(f"{response} is an invalid input. Try again.")    
        return response

    def create_character(self):
        print("\n")
        print("                                                  /\\")
        print("                                                 /  \\")
        print("                                                (    )")
        print("                                               (  | | )")
        print("                                                (  ^ )")
        print("                                                   |")
        print("                                            ______ |_____")
        print("                                                   |   ")
        print("                                                   |  ")
        print("                                                  / \\")
        print("                                                 /   \\")
        print("                                                /     \\")
        print("\n")
        character = self.prompt("Enter character name", lambda x: len(x) > 0)
        self.controller.create_character(character)
        print(f"Welcome, {self.controller.status.character_name}")

    def move_loop(self):
        while True:
            response = self.prompt(
                f"Where would you like to go? {VALID_DIRECTIONS}\n(or q to quit)",
                lambda x: x in VALID_COMMANDS,
            )
            if response == 'q':
                self.quit()
            direction = Direction(response)
            self.controller.move(direction)
            print(f"You moved {direction.name}")

            if self.controller.is_finished:
                print("")
                print("**********************************")
                print("*  CONGRATULATIONS! You’ve won!  *")
                print("**********************************")
                print("")
                print("You have made the IMPROBABLE ... POSSIBLE!\n")
                self.quit()
            else:
                print(self.controller.status)

                

    def start(self):
        self.welcome()
        self.create_character()
        self.controller.start_game()
        self.starting_pos = self.controller.status.current_position
        self.move_loop()

    def welcome(self):
        print("""
                               *******************************************************
                               *                                                     *             
                               *               Welcome to the Level Up Game          *
                               *                                                     *             
                               *                                                     *             
                               *                  A Game of Exploration              *
                               *                                                     *             
                               *******************************************************

        You have entered a world where you are an engineer at a large financial services corporation. You will 
        explore the sprawling corporate campus. If you are lucky, you’ll find the FREE LUNCH and go home a WINNER. 

        """)

        response = input("\nDo you want to play a game? y for Yes, n or q to quit\n")
        
        if response == 'q' or response == 'n':
            print("Goodbye!")
            quit()


    def quit(self):
        print(f"{self.controller.status.character_name} started on {self.starting_pos}, ended on {self.controller.status.current_position} and moved {self.controller.status.move_count} times.")
        quit()
