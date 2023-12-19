from platformer.platformer import PlatformerGame
import platformer.graphics as gr
from level import Level1




class Montezuma(PlatformerGame):
    window_width = 320
    window_height = 200
    levels_class_map = [[Level1]]

    def __init__(self):
        gr.SPRITES = "..\Images"
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
            self.set_player(0, 0, 30, 80)

    def game(self):
        pass

game = Montezuma()
game.run()


#for item in level:
 #  graph_engine.add_sprite(item['image'], item['x'], item['y'])