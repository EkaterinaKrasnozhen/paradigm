from sem3.tic_tac_toe.Dash import Dash
from sem3.tic_tac_toe.Victories import Victories


class Game:
    def __init__(self) -> None:
        self.game_over = False
        self.player = '1'
        self.dash = Dash()
        self.victories = Victories()
        self.symbol_x = '+'
        self.symbol_0 = '0'
        
    def step(self, step, symbol):
        index = self.dash.maps.index(step)
        self.dash.maps[index] = symbol
        
    def win(self) -> str:
        win = ""
        for i in self.victories.victories:
            if self.dash.maps[i[0]] == "+" and self.dash.maps[i[1]] == "+" and self.dash.maps[i[2]] == "+":
                win = "X"
            if self.dash.maps[i[0]] == "O" and self.dash.maps[i[1]] == "O" and self.dash.maps[i[2]] == "O":
                win = "O"          
        return win