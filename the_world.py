import graphics as gr

class World:
    count_w = 0
    count_h = 0
    tile_width = 0
    tile_height = 0

    def __init__(self):
        self.tile_map = []
        self.objects = []

    def add_object(self, game_object):
        """
        Добавить игровой объект в мир.
        """
        #game_object.sprite_id = gr.add_sprite(game_object.sprite)
        self.objects.append(game_object)

    def remove_object(self, game_object):
        """
        Удалить игровой объект из мира.
        """
        if game_object in self.objects:
            self.objects.remove(game_object)

    def update(self):
        """
        Обновить состояние всех объектов в мире.
        """
        for game_object in self.objects:
            game_object.update()

    def get_tile(self, x, y):
        if x >= 0 and y >= 0 and x < self.count_w * self.tile_width and y < self.count_h * self.tile_height:
            return self.tile_map[int(y / self.tile_height)][int(x / self.tile_width)]
        else:
            return None