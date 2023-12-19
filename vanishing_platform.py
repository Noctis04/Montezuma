import level
from platformer.game_object import GameObject
import platformer.graphics as gr

class VanishingPlatform(GameObject):
    visible_frames = 60
    invisible_frames = 60
    def __init__(self, world, x, y, width):
        super().__init__(world, None, width, 0, x, y, 0, 0, fly=True)
        self.current_frame = 0
        self.states = {
            'visible': self.is_visible,
            'invisible': self.is_invisible
        }
        self.set_state('visible')


    def is_visible(self):
        self.world.fill([level.Tile.PLATFORM], self.x, self.y, self.width, 1)
        if self.current_frame == self.visible_frames:
            self.current_frame = 0
            self.set_state('invisible')
    def is_invisible(self):
        self.world.fill([level.Tile.EMPTY], self.x, self.y, self.width, 1)
        if self.current_frame == self.visible_frames:
            self.current_frame = 0
            self.set_state('visible')

    def update(self):
        super().update()
        self.current_frame += 1
