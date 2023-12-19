from platformer.game_object import GameObject
from platformer.animation import Animation
from platformer import graphics as gr


class Skull (GameObject):
    speed_x = 2

    def __init__(self, world, pos_x, pos_y):
        self.animation_frames = [
            (67, 76, 14,  10),
            (77, 78, 14, 12),
            (92, 79, 12, 11),
            (0, 77, 13, 13),
            (14, 76, 11, 15),
            (25, 77, 13, 13),
            (39, 80, 13, 10),
            (53, 76, 13, 13),
            ]
        self.sprite = Animation('GameObject.png', self.animation_frames, pos_x, pos_y, 2, back=True)
        super().__init__(world, self.sprite, 14, 10, pos_x, pos_y, fly=True)
        self.states = {
            'left': self.move_left,
            'right': self.move_right
        }
        self.set_state('right')


    def move_left(self):
        self.move(self.speed_x, 10, 'right')

    def move_right(self):
        self.move(-self.speed_x, -10, 'left')

    def move(self, speed, dx, new_state):
        self.velocity_x = speed
        if not self.on_ground() or self.x == 0 or self.x == gr.window_width:
            self.x -= dx
            self.set_state(new_state)
            self.sprite.back = not self.sprite.back

   
    def death(self):
        self.world.remove_object(self)
        gr.remove_sprite(self)