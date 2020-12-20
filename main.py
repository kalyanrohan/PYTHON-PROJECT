import arcade as ac
import random
import time

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "TYPO"


class MyGame(ac.Window):
    """
    Main application class.
    """


    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        ac.set_background_color(ac.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
                """
        Render the screen.
        """
        ac.start_render()
        # start_x and start_y make the start point for the text. We draw a dot to make it easy too see
        # the text in relation to its start x and y.
        start_x = 50
        start_y = 450
        ac.draw_point(start_x, start_y, ac.color.BLUE, 5)
        ac.draw_text("Simple line of text in 12 point", start_x, start_y, ac.color.BLACK, 12)

        start_x = 50
        start_y = 150
        ac.draw_point(start_x, start_y, ac.color.BLUE, 5)
        ac.draw_text("Garamond Text", start_x, start_y, ac.color.BLACK, 15, font_name='GARA')

        start_x = 50
        start_y = 400
        ac.draw_point(start_x, start_y, ac.color.BLUE, 5)
        ac.draw_text("Text anchored 'top' and 'left'.",start_x, start_y, ac.color.BLACK, 12, anchor_x="left", anchor_y="top")

        start_y = 350
        ac.draw_point(start_x, start_y, ac.color.BLUE, 5)
        ac.draw_text("14 point multi line text",start_x, start_y, ac.color.BLACK, 14, anchor_y="top")

        start_y = 450
        start_x = 300
        width = 200
        height = 20
        ac.draw_point(start_x, start_y, ac.color.BLUE, 5)
        ac.draw_lrtb_rectangle_outline(start_x, start_x + width,start_y + height, start_y,ac.color.BLUE, 1)
        ac.draw_text("Centered Text.",start_x, start_y, ac.color.BLACK, 14, width=200, align="center")

        start_y = 250
        start_x = 300
        ac.draw_point(start_x, start_y, ac.color.BLUE, 5)
        ac.draw_text("Text centered on a point",start_x, start_y, ac.color.BLACK, 14, width=200, align="center",
        anchor_x="center", anchor_y="center")

        start_y = 150
        start_x = 300
        ac.draw_point(start_x, start_y, ac.color.BLUE, 5)
        ac.draw_text("Text rotated on a point", start_x, start_y,ac.color.BLACK, 14, width=200, align="center", anchor_x="center",
        anchor_y="center", rotation=self.text_angle)

        start_y = 150
        start_x = 20
        ac.draw_point(start_x, start_y, ac.color.BLUE, 5)
        ac.draw_text("Sideways text", start_x, start_y,ac.color.BLACK, 14, width=200, align="center",
        anchor_x="center", anchor_y="center", rotation=90.0)

        start_y = 20
        start_x = 50
        ac.draw_point(start_x, start_y, ac.color.BLUE, 5)
        ac.draw_text(f"Time elapsed: {self.time_elapsed:7.1f}",start_x, start_y, ac.color.BLACK, 14)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://ac.academy/ac.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    ac.run()


if __name__ == "__main__":
    main()
