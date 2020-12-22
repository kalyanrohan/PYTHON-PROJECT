import arcade as ac
import random
import time
import arcade.gui
from arcade.gui import UIManager
import os

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "TYPO"

class MyFlatButton(ac.gui.UIFlatButton,ac.View):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)

        

class MyGhostFlatButton(ac.gui.UIGhostFlatButton):
    """
    For this subclass, we create a custom init, that takes in another
    parameter, the UI text box. We use that parameter and print the contents
    of the text entry box when the ghost button is clicked.
    """

    def __init__(self, center_x, center_y, input_box):
        super().__init__(
            'GhostFlatButton',
            center_x=center_x,
            center_y=center_y,
            width=250,
            # height=20
        )
        self.input_box = input_box

    def on_click(self):
        """ Called when user lets off button """
        print(f"Click ghost flat button. {self.input_box.text}")


class MainMenu(ac.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        ac.start_render()

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        ac.set_background_color(ac.color.AERO_BLUE)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()

        y=self.window.height//2
        x=self.window.width//2

        play_button=MyFlatButton('PLAY',center_x=x,center_y=y,width=250,height=100,align="center")
        self.ui_manager.add_ui_element(play_button)

        htp_button=MyFlatButton('How to Play',center_x=x,center_y=y-100,width=250,height=100,align="center")
        self.ui_manager.add_ui_element(play_button)

class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", SCREEN_WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH/2, HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

class GameView(ac.View):
    def __init__(self):
        super().__init__()

        self.time_taken = 0

        
    def on_show(self):
        ac.set_background_color(ac.color.AMAZON)

        # Don't show the mouse cursor
        self.window.set_mouse_visible(True)

    def on_draw(self):
        ac.start_render()
        # Draw all the sprites.

        # Put the text on the screen.
        output = f"Score: 100"
        ac.draw_text(output, 10, 30, ac.color.WHITE, 14)
        output_total = f"Total Score: {100}"
        ac.draw_text(output_total, 10, 10, ac.color.WHITE, 14)

    def on_update(self, delta_time):
        self.time_taken += delta_time

        # Call update on all sprites (The sprites don't do much in this
        # example though.)

        
class GameOverView(ac.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show(self):
        ac.set_background_color(ac.color.BLACK)

    def on_draw(self):
        ac.start_render()
        """
        Draw "Game over" across the screen.
        """
        ac.draw_text("Game Over", 240, 400, ac.color.WHITE, 54)
        ac.draw_text("Click to restart", 310, 300, ac.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        ac.draw_text(f"Time taken: {time_taken_formatted}",SCREEN_WIDTH/2,200,ac.color.GRAY,font_size=15,
        anchor_x="center")

        output_total = f"Total Score: 100"
        ac.draw_text(output_total, 10, 10, ac.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)



if __name__ == '__main__':
    window = ac.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
    view = MainMenu()
    window.show_view(view)
    ac.run()
