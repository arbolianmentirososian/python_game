from terrain import Terrain
from dragon import Dragon

class Scene:

    def __init__(self, x_size=50, y_size=50, terrain=Terrain(5), players=None):
        self.x_size = x_size
        self.y_size = y_size
        self.terrain = terrain
        self.speed_of_movement = terrain.value
        if players is None:
            self.players = []
        else:
            self.players = player

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def show_players(self):
        for index, player in enumerate(self.players):
            print(f'No: {index + 1}:  {player}')

    def __str__(self):
        return f'Size: {self.x_size}x{self.y_size}, {self.terrain.name}, Players: {len(self.players)}'


ground = Scene()
print(ground)
dragon = Dragon('Drogo')
ground.add_player(dragon)
dragon2 = Dragon('Drogo2')
ground.add_player(dragon2)
dragon3 = Dragon('Drogo3')
ground.add_player(dragon3)
ground.show_players()
print(ground)
