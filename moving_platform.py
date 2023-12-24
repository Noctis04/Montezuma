import level
from vanishing_platform import VanishingPlatform
from platformer.graphics import tile_width, tile_height

class MovingPlatform(VanishingPlatform):
    speed = 5
    def __init__(self, world,x, y, width):
        super().__init__(world, x, y, width)
        self.states = ['platform1', 'platform2']
        self.set_state('platform1')

    def draw(self, t1, t2, t3):
        self.world.fill([t1], self.x, self.y, 1, 1)
        self.world.fill([t2], self.x + 1, self.y, self.width - 2, 1)
        self.world.fill([t3], self.x + self.width - 1, self.y, 1, 1)
    def platform1(self):
        self.draw(level.Tile.TRACK_L1, level.Tile.TRACK_1, level.Tile.TRACK_R1)
        if self.current_frame == self.speed:
            self.current_frame = 0
            self.set_state('platform2')

    def platform2(self):
        self.draw(level.Tile.TRACK_L2, level.Tile.TRACK_2, level.Tile.TRACK_R2)
        if self.current_frame == self.speed:
            self.current_frame = 0
            self.set_state('platform1')

    def update(self):
        super().update()
        player = self.world.player
        x = player.x + player.width / 2
        y = int(player.y + player.height)
        cell_x = x // tile_width
        cell_y = y // tile_height
        if cell_x >= self.x and cell_x < self.x + self.width and cell_y == self.y and self.current_frame == 1:
            self.world.player.x += tile_width
