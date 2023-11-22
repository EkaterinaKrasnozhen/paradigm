class View:
    def get_step(self, player) -> int:
        step = int(input(f" Ваш ход игрок {player}: "))
        return step
        