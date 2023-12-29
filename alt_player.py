from platformer.game_object import GameObject
from platformer.graphics import KEY_LEFT, KEY_RIGHT, KEY_SPACE
from platformer.animation import Animation
from skull import Skull
import platformer.graphics as gr

class Player(GameObject):
    def __init__(self, world, pos_x, pos_y):
        super().__init__(world, None, 12, 19, pos_x, pos_y)
        self.setup_states(pos_x, pos_y)
        self.setup_animation()

        self.speed_x = 3
        self.speed_y = 8
        self.gravity = 7

    def setup_states(self, pos_x, pos_y):
        self.states = {
            'walk_left': [(13, 0, 12, 19), (0, 0, 11, 19), (26, 0, 11, 19)],
            'walk_right': [(13, 0, 12, 19), (0, 0, 11, 19), (26, 0, 11, 19)],
            'jump': [(63, 20, 13, 19)],
            'rope_up': [(27, 20, 11, 19), (38, 20, 11, 19)],
            'rope_down': [(27, 20, 11, 19), (38, 20, 11, 19)],
            'stairs_up': [(0, 20, 11, 19), (14, 20, 11, 19)],
            'stairs_down': [(0, 20, 11, 19), (14, 20, 11, 19)],
        }
        self.current_state = 'walk_right'

    def setup_animation(self):
        self.sprite = Animation('GameObject.png', self.states[self.current_state], self.x, self.y, 3, back=True)

    def update(self):
        is_moving_horizontal = gr.key_pressed(KEY_LEFT) or gr.key_pressed(KEY_RIGHT)

        if gr.key_pressed(KEY_SPACE) and not self.is_on_air:
            self.velocity_y = -self.speed_y
            self.current_state = 'jump'

        if gr.key_pressed(KEY_LEFT):
            self.velocity_x = -self.speed_x
            self.sprite.flip_x = True
            self.current_state = 'walk_left'
        elif gr.key_pressed(KEY_RIGHT):
            self.velocity_x = self.speed_x
            self.sprite.flip_x = False
            self.current_state = 'walk_right'

        if is_moving_horizontal:
            self.sprite.update()
        else:
            self.sprite.reset_frame()

        self.sprite.frames = self.states[self.current_state]
        super().update()

    def handle_collision(self, other_object):
        if isinstance(other_object, Skull):
            if other_object in self.world.objects:
                other_object.death()
            print("Player collided with a skull!")
