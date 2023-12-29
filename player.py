from platformer.game_object import GameObject
from platformer.graphics import KEY_LEFT, KEY_RIGHT, KEY_SPACE, KEY_UP, KEY_DOWN
from platformer.animation import Animation
from skull import Skull
from level import Tile
import platformer.graphics as gr

class Player(GameObject):
    speed_x = 3
    speed_y = 8
    sprite_file = 'GameObject.png'
    anim_speed = 3
    rope_speed = 2

    def __init__(self, world, pos_x, pos_y):

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
        self.tube_animation_frames = [
            (50, 20, 12, 19)
        ]
        self.jump_animation_frames = [
            (63, 20, 13, 19)
        ]
        self.x = pos_x
        self.y = pos_y
        self.sprite = Animation(self.sprite_file, self.walk_animation_frames, self.x, self.y, self.anim_speed)
        super().__init__(world, self.sprite, self.sprite.width, self.sprite.height, pos_x, pos_y)
        self.states = ['walk_left', 'walk_right', 'jump', 'stand', 'rope']
        self.set_state('stand')

    def setup_animation(self, frames, back=True):
        self.sprite.set_frames(frames)
        self.sprite.back = back

    def stand(self):
        self.setup_animation(self.walk_animation_frames[0:1])

    def walk_left(self):
        self.setup_animation(self.walk_animation_frames)
        self.velocity_x = -self.speed_x
        self.sprite.flip_x = True

    def walk_right(self):
        self.setup_animation(self.walk_animation_frames)
        self.velocity_x = self.speed_x
        self.sprite.flip_x = False

    def jump(self):
        self.setup_animation(self.jump_animation_frames)

    def rope(self):
        self.setup_animation(self.rope_animation_frames)

    def move(self, dir):
        x = self.x + self.width / 2
        y = self.y + self.height + dir * 2
        tile = self.world.get_tile(x, y)
        if tile == Tile.ROPE or tile == Tile.ROPE_TOP or tile is None:
            self.y += dir * self.rope_speed
            self.x = (self.x // gr.tile_width + 1) * gr.tile_width + gr.tile_width // 2 - self.sprite.width // 2
            self.set_state('rope')
            self.sprite.y = self.y
            self.sprite.x = int(self.x)
            if dir == -1 and self.world.get_tile(x, self.y + self.height) == Tile.ROPE_TOP:
                self.set_state('stand')
            if dir == 1 and self.world.get_tile(x, y + self.height//2) == Tile.EMPTY:
                self.y += self.height
                self.set_state('jump')

    def is_climbing(self):
        return self.state == 'rope'

    def update(self):
        if self.state != 'rope':
            super().update()
        else:
            self.run_state()
        is_on_ground = self.on_ground()
        self.sprite.start()

        if gr.key_pressed(KEY_SPACE) and is_on_ground and not self.is_climbing():
            self.velocity_y = -self.speed_y
            self.set_state('jump')
        elif gr.key_pressed(KEY_LEFT) and not self.is_climbing():
            self.set_state('walk_left')
        elif gr.key_pressed(KEY_RIGHT) and not self.is_climbing():
            self.set_state('walk_right')
        elif gr.key_pressed(KEY_UP):
            self.move(-1)
        elif gr.key_pressed(KEY_DOWN):
            self.move(1)
        else:
            if is_on_ground and self.state != 'rope':
                self.set_state('stand')
            self.sprite.stop()


    def handle_collision(self, other_object):
        if isinstance(other_object, Skull):
            if other_object in self.world.objects:
                other_object.death()
            print("Player collided with a skull!")