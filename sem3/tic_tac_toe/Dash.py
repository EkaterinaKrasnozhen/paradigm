
class Dash:
    def __init__(self):
        self.maps = [1,2,3,
                     4,5,6,
                     7,8,9] 
       
    def print_maps(self):
        print(self.maps[0], end = " ")
        print(self.maps[1], end = " ")
        print(self.maps[2])
    
        print(self.maps[3], end = " ")
        print(self.maps[4], end = " ")
        print(self.maps[5])
    
        print(self.maps[6], end = " ")
        print(self.maps[7], end = " ")
        print(self.maps[8])
        
        


if __name__ == '__main__':        
    dash_board = Dash()
    dash_board.print_maps()