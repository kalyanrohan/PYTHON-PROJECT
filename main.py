import arcade as ac
import random
import time

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "TYPO"

class MenuView(ac.View):
    def on_show(self):
        ac.set_background_color(ac.color.WHITE)

    def on_draw(self):
        ac.start_render()
        ac.draw_text("Menu Screen", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         ac.color.BLACK, font_size=50, anchor_x="center")
        ac.draw_text("Click to advance", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                         ac.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)

class InstructionView(ac.View):
    def on_show(self):
        ac.set_background_color(ac.color.ORANGE_PEEL)

    def on_draw(self):
        ac.start_render()
        ac.draw_text("Instructions Screen", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         ac.color.BLACK, font_size=50, anchor_x="center")
        ac.draw_text("Click to advance", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                         ac.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

def main():
    window = ac.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.total_score = 0
    menu_view = MenuView()
    window.show_view(menu_view)
    ac.run()


if __name__ == "__main__":
    main()
