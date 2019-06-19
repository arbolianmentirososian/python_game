from enum import Enum

class Terrain(Enum):
    
    GROUND = 5
    GRASS = 4
    STONE = 3
    FOREST = 2
    WATER = 1

    def return_info(self):
        return f'{self.name}: {self.value}'
