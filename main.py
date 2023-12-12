from enum import IntEnum

from platformer import PlatformerGame
from skull import Skull
import graphics as gr
from level import Level


Tile = IntEnum('Tile', ['EMPTY', 'BRICK', 'COL', 'ROPE_TOP', 'BRICK2', 'ROPE', 'PLATFORM',
                        'TRACK_L1', 'TRACK_1', 'TRACK_R1', 'TRACK_L2', 'TRACK_2', 'TRACK_R2'], start=0)

class LevelAllBricks(Level):
    def __init__(self):
        super().__init__(40, 25)
        self.fill([Tile.BRICK])


class Level1(LevelAllBricks):
    def __init__(self):
        super().__init__()
        self.fill([Tile.EMPTY], 0, 5, None, 10)
        self.fill([Tile.BRICK, Tile.BRICK2], 1, 4, 36, 1)
        self.fill([Tile.EMPTY], 1, 5, 4, 18)
        self.fill([Tile.COL], 1, 4, 1, 19)
        self.fill([Tile.EMPTY], 5, 5, 7, 17)
        self.fill([Tile.EMPTY], 12, 5, 2, 15)
        self.fill([Tile.EMPTY], 14, 5, 13, 13)
        self.fill([Tile.EMPTY], 27, 5, 2, 15)
        self.fill([Tile.EMPTY], 29, 5, 6, 17)
        self.fill([Tile.EMPTY], 35, 5, 4, 18)
        self.fill([Tile.COL], 38, 4, 1, 19)
        self.fill([Tile.EMPTY], 19, 18, 3, 7)
        self.tile_map[18][19] = Tile.BRICK2
        self.tile_map[18][20] = Tile.ROPE_TOP
        self.tile_map[18][21] = Tile.BRICK2
        self.fill([Tile.ROPE], 20, 19, 1, 6)
        #self.add_object(Skull(self, 90, 102))


# class Level2(LevelAllBricks):
#     def __init__(self):
#         super().__init__()
#         self.fill([Tile.EMPTY], 0, 4, None, 10)
#         #self.fill(0, 30, 5, 6, 11)
#         self.add_object(Skull(self, 90, 102))


class Montezuma(PlatformerGame):
    window_width = 320
    window_height = 200
    levels_class_map = [[Level1]]

    def __init__(self):
        gr.init(self.window_width, self.window_height)
        super().__init__()
        self.states = {
            'Intro': self.intro,
            'Game': self.game
        }
        self.set_state('Intro')

    def intro(self):
        if gr.key_pressed(gr.KEY_SPACE):
            self.set_state('Game')
            gr.clear()
            self.set_player(0, 0, 50, 70)

    def game(self):
        pass

game = Montezuma()
game.run()


#for item in level:
 #  graph_engine.add_sprite(item['image'], item['x'], item['y'])