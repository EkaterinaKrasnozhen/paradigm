from Game import Game
from View import View

game = Game()
view = View()
game.dash.print_maps()

while game.game_over == False: # назначаем условие выхода из цикла
    step_x = view.get_step(game.player) # получаем ход игрока 1
    game.player = '2' # передаем ход игроку 2
    step_0 = view.get_step(game.player)# получаем ход игрока 2
    game.player = '1'# передаем ход игроку 1
    game.step(step_x, game.symbol_x)# добавляем в карту ход игрока 1
    game.step(step_0, game.symbol_0)# добавляем в карту ход игрока 2
    game.dash.print_maps()# отрисовываем карту с учетом последних ходов
    win = game.win()# проверяем условие выхода из цикла
    if win != "":
        game.game_over = True
    else:
        game.game_over = False
    
print("Победил", win)