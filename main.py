import arcade as ac
import random
import time

SCREEN_HEIGHT=720
SCREEN_WIDTH=1280
TITLE="TYPO"

class Typo(ac.Window):

    def __init__(self,width,height,title):
        super().__init__(width,height,title, resizable=True)
        self.set_location(200,50)

        ac.set_background_color(ac.color.BLACK_LEATHER_JACKET)

        self.enemy_list= None
        self.enemy= None

    # def setup(self):
    #     self.enemy_list= ac.SpriteList()
    #     self.enemy=ac.AnimatedWalkingSprite()

    #     self.enemy.stand_right_textures= []
    #     self.enemy.stand_right_textures.append(ac.load_texture())

    def main():
    """ Main method """
        window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        start_view = GameView()
        window.show_view(start_view)
        start_view.setup()
        arcade.run()
    

    def on_draw(self):
        ac.start_render()
        ac.draw_rectangle_outline(SCREEN_WIDTH/2,SCREEN_HEIGHT/4,SCREEN_WIDTH/2,100,ac.color.WHITE)
        ac.finish_render
    

    def on_update(self,delta_time):
        pass
    

    def on_key_press(self):
        pass

    def on_key_release(self):
        pass
    

       
    

Typo(SCREEN_WIDTH,SCREEN_HEIGHT,TITLE)
ac.run()
