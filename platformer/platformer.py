from platformer import graphics as gr
from platformer.state import State
from player import Player


class PlatformerGame(State):
    player_class = Player
    levels_class_map = []
    levels_map = []

    def __init__(self):
        """
        Инициализация игры.

        """
        super().__init__()  # Вызов конструктора родительского класса
        self.player = None
        self.world = None
        for row in self.levels_class_map:
            new_row = []
            for l in row:
                new_row.append(None)
            self.levels_map.append(new_row)

    def set_player(self, map_x, map_y, player_pos_x, player_pos_y):
        self.map_x = map_x
        self.map_y = map_y
        self.player = self.player_class(self.world, player_pos_x, player_pos_y)
        self.change_level()

    def check_change_level(self):
        """
        Проверки переходов между уровнями
        """
        if self.player is None:
            pass
        elif self.player.x > gr.window_width + self.player.width:
            self.map_x += 1
            self.change_level()
            self.player.x = 0
        elif self.player.x < - self.player.width:
            self.map_x -= 1
            self.change_level()
            self.player.x = gr.window_width - self.player.width
        elif self.player.y <= - self.player.height:
            self.map_y -= 1
            self.change_level()
            self.player.y = gr.window_height - self.player.height
        elif self.player.y > gr.window_height:
            self.map_y += 1
            self.change_level()
            self.player.y = 0

    def change_level(self):
        level = self.levels_map[self.map_y][self.map_x]
        if level is None:
            level = self.levels_map[self.map_y][self.map_x] = self.levels_class_map[self.map_y][self.map_x]()
        if self.world is not None:
            self.world.remove_object(self.player)
        gr.clear()
        self.world = level
        self.world.tile_width = gr.tile_width
        self.world.tile_height = gr.tile_height
        gr.set_tiles(level.tile_map, level.tiles)
        self.world.add_object(self.player)
        # исправление отрисовки при переходе между уровнями
        for game_object in self.world.objects:
            #if game_object.sprite is not None:
            gr.add_sprite(game_object.sprite)
        self.player.world = self.world
        self.world.player = self.player

    def run(self):
        """
        Запуск игрового цикла.

        """
        while True:
            if gr.process_events():
                break
            self.run_state()
            if self.world is not None:
                self.world.update()
            self.check_change_level()

            gr.draw_all()
        gr.quit()
