import random
import time
import os


class Tile():

    def __init__(self, row, column) -> None:
        self.state = random.choice(['.','@'])
        self.row = row
        self.column = column
        self.neighbours = []


    def get_active_neighbours(self):
        
        tiles_on = 0

        for tile in self.neighbours:
            if tile.state == '@':
                tiles_on += 1
        
        return tiles_on


    def update(self):
        active_neighbours = self.get_active_neighbours()

        if self.state == '@':
            if active_neighbours < 2 or active_neighbours > 3:
                self.state = '.'

        if self.state == '.' and active_neighbours == 3:
            self.state = '@'


    def set_neighbours(self, neighbours):
        self.neighbours = neighbours
    

class Grid():
    
    def __init__(self, rows, columns) -> None:
        
        self.grid = []
        self.rows = rows
        self.columns = columns
        self.create_grid()

        self.get_neighbours()


    def create_grid(self):
        
        for row in range(self.rows):
            new_row = []

            for column in range(self.columns):
                new_row.append(Tile(row, column))

            self.grid.append(new_row)


    def print_grid(self):
        print(self.grid)


    def update_output(self):
        os.system("CLS")
        for row in self.grid:
            output_string = ""
            
            for tile in row:
                output_string += str(tile.state) + " "
            
            print(output_string)

    
    def update_grid(self):

        for row in self.grid:
            for tile in row:
                tile.update()


    def keep_boundry(self, number, boundry):
        if number > boundry:
            return 0
        elif number < 0:
            return boundry
        else:
            return number


    def get_neighbours(self):
        
        for row in self.grid:
            for tile in row:
                neighbours = []
                
                # above
                current_row = self.keep_boundry(tile.row-1, self.rows-1)
                for i in range(-1, 2):
                    current_column = self.keep_boundry(tile.column+i, self.columns-1)
                    neighbours.append(self.grid[current_row][current_column])

                # same
                current_row = tile.row
                for i in range(-1, 2, 2):
                    current_column = self.keep_boundry(tile.column+i, self.columns-1)
                    neighbours.append(self.grid[current_row][current_column])

                # below
                current_row = self.keep_boundry(tile.row+1, self.rows-1)
                for i in range(-1, 2):
                    current_column = self.keep_boundry(tile.column+i, self.columns-1)
                    neighbours.append(self.grid[current_row][current_column])
                
                tile.set_neighbours(neighbours)
                







if __name__ == "__main__":
    grid = Grid(25, 50)

    while True:
        grid.update_grid()
        grid.update_output()
        time.sleep(0.5)
