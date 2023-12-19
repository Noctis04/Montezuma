from platformer.game_object import GameObject
from platformer.graphics import KEY_LEFT, KEY_RIGHT, KEY_UP
from platformer.animation import Animation
from skull import Skull  # Assuming the Skull class is defined in skull.py


class Player(GameObject):
    speed_x = 4
    speed_y = 8

    def __init__(self, world, key_pressed, pos_x, pos_y):
        self.setup_animation(pos_x, pos_y)
        super().__init__(world, self.sprite, 10, 19, pos_x, pos_y)
        self.key_pressed = key_pressed
        self.gravity = 7  # Gravity value

    def setup_animation(self, pos_x, pos_y):
        animation_frames = [
            (13, 0, 12, 19),
            (0, 0, 11, 19),
            (26, 0, 11, 19)
        ]
        self.sprite = Animation('GameObject.png', animation_frames, pos_x, pos_y, 1, back=True)

    def update(self):

        is_moving_horizontal = self.key_pressed(KEY_LEFT) or self.key_pressed(KEY_RIGHT)

        if self.key_pressed(KEY_UP) and not self.is_on_air:
            self.velocity_y = -self.speed_y

        if self.key_pressed(KEY_LEFT):
            self.velocity_x = -self.speed_x
            self.sprite.flip_x = True
        elif self.key_pressed(KEY_RIGHT):
            self.velocity_x = self.speed_x
            self.sprite.flip_x = False

        if is_moving_horizontal:
            self.sprite.update()
        else:
            self.sprite.reset_frame()

        super().update()

    def handle_collision(self, other_object):
        if isinstance(other_object, Skull):
            if other_object in self.world.objects:
                other_object.death()
            print("Player collided with a skull!")
