from platformer.platformer import PlatformerGame
import platformer.graphics as gr
from level import Level1, Level2




class Montezuma(PlatformerGame):
    window_width = 320
    window_height = 200
    levels_class_map = [[Level1],
                        [Level2]]

    def __init__(self):
        gr.SPRITES = "..\Images"
        gr.init(self.window_width, self.window_height)
        super().__init__()
        self.states = {
            'intro': self.intro,
            'game': self.game
        }
        self.set_state('intro')

    def intro(self):
        if gr.key_pressed(gr.KEY_ECS):
            self.set_state('game')
            gr.clear()
            self.set_player(0, 0, 30, 80)

    def game(self):
        pass

game = Montezuma()
game.run()


#for item in level:
 #  graph_engine.add_sprite(item['image'], item['x'], item['y'])