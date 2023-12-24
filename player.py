from platformer.game_object import GameObject
from platformer.graphics import KEY_LEFT, KEY_RIGHT, KEY_UP
from platformer.animation import Animation
from skull import Skull
import platformer.graphics as gr

class Player(GameObject):
    speed_x = 3
    speed_y = 8

    def __init__(self, world, pos_x, pos_y):
        self.states = ['walk_left', 'walk_right', 'jump', 'rope_up', 'rope_down', 'stairs_up', 'stairs_down']
        self.setup_animation(pos_x, pos_y)
        super().__init__(world, self.sprite, self.sprite.width, self.sprite.height, pos_x, pos_y)
        self.gravity = 7  # Gravity value

    def setup_animation(self, pos_x, pos_y):
        self.walk_animation_frames = [
            (13, 0, 12, 19),
            (0, 0, 11, 19),
            (26, 0, 11, 19),
        ]
        self.stairs_animation_frames = [
            (0, 20, 11, 19),
            (14, 20, 11, 19),
        ]
        self.rope_animation_frames = [
            (27, 20, 11, 19),
            (38, 20, 11, 19),
        ]
        self.jump_animation_frames = [(63, 20, 13, 19) ]
        self.sprite = Animation('GameObject.png', self.walk_animation_frames, pos_x, pos_y, 3, back=True)

    def update(self):

        is_moving_horizontal = gr.key_pressed(KEY_LEFT) or gr.key_pressed(KEY_RIGHT)

        if gr.key_pressed(KEY_UP) and not self.is_on_air:
            self.velocity_y = -self.speed_y

        if gr.key_pressed(KEY_LEFT):
            self.velocity_x = -self.speed_x
            self.sprite.flip_x = True
        elif gr.key_pressed(KEY_RIGHT):
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
