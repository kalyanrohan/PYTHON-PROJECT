import arcade as ac
import random
import time
import arcade.gui
from arcade.gui import UIManager
import os

open('sentences.txt',mode='r',encoding='utf-8')


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "TYPO"
f=open('sentences.txt',mode='r',encoding='utf-8')
sentences=f.read().split('\n')

class Button(ac.gui.UIFlatButton,ac.View):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def __init__(self,text,center_x,center_y,width,height,align):
        super().__init__(text=text,center_x=x,center_y=y,width=250,height=100,align='center')
        
    
    def on_click(self):
        if self.text=='Play':
            instruction=InstructionView()
            instruction.se
        

    

class Input_box(ac.gui.UIGhostFlatButton):
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
        ac.draw_text(SCREEN_TITLE,(SCREEN_WIDTH//2-100),(SCREEN_HEIGHT//2)+150,ac.color.BLUE,72,align='center')

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




class InstructionView(ac.View):
    def on_show(self):
        ac.set_background_color(ac.color.ORANGE_PEEL)

    def on_draw(self):
        ac.start_render()
        ac.draw_text("Instructions Screen", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         ac.color.BLACK, font_size=50, anchor_x="center")
        ac.draw_text("Click to Play", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-75,
                         ac.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.se 
        self.window.show_view(game_view)
    
class GameView(ac.View):

    def __init__(self):
        super().__init__()

        self.time_taken = 0
        self.score=0
        self.text=random.choice(sentences)
        self.ui_manager=UIManager()
        self.input=ac.gui.UIInputBox(self.window.width//2,self.window.height//3,720)
        self.empty=''
        self.lives=3

    
    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        ac.set_background_color(ac.color.BLACK)

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()


    def setup(self):
        self.score=0
        self.lives=3
        x=self.window.width
        y=self.window.height
        self.ui_manager.purge_ui_elements()


        self.input.text= self.empty
        self.input.cursor_index = len(self.input.text)
        self.ui_manager.add_ui_element(self.input)


    def on_draw(self):
        x=self.window.width
        y=self.window.height
        ac.start_render()
        # Put the text on the screen.
        ac.draw_text(self.text,x//2,y//2,ac.color.WHITE,font_size=20,anchor_x='center')
        output_total = f"Total Score: {self.score}"
        ac.draw_text(output_total, 10, 10, ac.color.WHITE, 14)
        ac.finish_render()

    def on_update(self, delta_time):
        self.time_taken += delta_time
        while self.lives>0:
           if self.input.text==self.text:
               self.input.text==self.empty
               self.score+=1


        
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
    window = ac.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE,resizable=True)
    view = GameView()
    window.show_view(view)
    ac.run()
