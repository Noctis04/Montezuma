from platformer.the_world import World
from enum import IntEnum
from vanishing_platform import VanishingPlatform
from moving_platform import MovingPlatform


class Level(World):
    tiles = 'tileMap1.png'
    def __init__(self, count_w, count_h):
        super().__init__()
        self.count_w = count_w
        self.count_h = count_h
        self.tile_map = [[0 for x in range(count_w)] for y in range(count_h)]

    def fill(self, cells, start_x=0, start_y=0, count_x=None, count_y=None):
        i = 0
        for y in range(start_y, start_y + count_y if count_y is not None else self.count_h):
            for x in range(start_x, start_x + count_x if count_x is not None else self.count_w):
                self.tile_map[y][x] = cells[i]
                i += 1
                if i == len(cells):
                    i = 0


Tile = IntEnum('Tile', ['EMPTY', 'BRICK', 'COL', 'ROPE_TOP', 'BRICK2', 'ROPE', 'PLATFORM',
                         'TRACK_L1', 'TRACK_1', 'TRACK_R1', 'TRACK_L2', 'TRACK_2', 'TRACK_R2',
                         'TRACK_L3', 'TRACK_3', 'TRACK_R3', 'STAIRS_TOP1', 'STAIRS_TOP2', 'STAIRS1', 'STAIRS2'], start=0)

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
        self.add_object(VanishingPlatform(self, 3, 20, 9))
        self.add_object(MovingPlatform(self, 29, 20, 8))
        #self.add_object(Skull(self, 90, 102))


class Level2(LevelAllBricks):
    def __init__(self):
        super().__init__()
        self.fill([Tile.EMPTY], 0, 5, None, 4)
        self.fill([Tile.BRICK], 12, 5, 17, 1)
        self.fill([Tile.EMPTY], 16, 4, 9, 2)
        self.fill([Tile.EMPTY], 17, 3, 7, 1)
        self.fill([Tile.ROPE], 20, 0, 1, 5)
