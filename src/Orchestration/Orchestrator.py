from src.Game_Data import Game_Data
from src.GUI import Starter_Window

GD = 0

def orchestrate():

    # start window, get initial game data, assign to GD obj
    Game_Data.set_initial_data(Starter_Window.open_window())

    # main loop
    while True:
        pass
