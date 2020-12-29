import arcade as ac
import random
import time
import arcade.gui
from arcade.gui import UIManager
from arcade.gui.ui_style import UIStyle
import os
open('sentences.txt',mode='r',encoding='utf-8')
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "TYPO"
f=open('sentences.txt',mode='r',encoding='utf-8')
sentences=f.read().split('\n')


class Button(ac.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        if self.text.lower()=="play":
            ac.View().window.show_view(InstructionView())
        elif self.text.lower()=='quit':
            ac.View().window.close()
        
class MainMenu(ac.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        ac.start_render()
        ac.draw_text(SCREEN_TITLE,(SCREEN_WIDTH//2-100),(SCREEN_HEIGHT//2)+150,ac.color.WHITE,72,align='center')
    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        ac.set_background_color(ac.color.BLUEBERRY)
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    def setup(self):
        """ Set up this view. """
        self.ui_manager.purge_ui_elements()
        y=self.window.height//2
        x=self.window.width//2
        play_button=Button(text="Play",center_x=x,center_y=y,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(play_button)
        quit_button=Button(text="Quit",center_x=x,center_y=y-150,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(quit_button)


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
        game_view.setup()
        self.window.show_view(game_view)
    

class GameView(ac.View):
    
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.score=0
        self.text=random.choice(sentences)
        self.ui_manager=UIManager()
        self.input=ac.gui.UIInputBox(self.window.width//2,self.window.height//3,1000)
        self.empty=''
        self.sentences=2
        self.wpm=0
        self.start=False
        self.accuracy=0
        self.char=0
        self.wrong_input=0
        self.correct_input=0

    def on_show_view(self):
        """ Called once when view is activated. """
        self.setup()
        ac.set_background_color(ac.color.BLACK)
    
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def setup(self):
        self.score=0
        x=self.window.width
        y=self.window.height
        self.ui_manager.purge_ui_elements()
        self.input.set_style_attrs(font_size=14)
        self.input.text= self.empty
        self.input.cursor_index = len(self.input.text)
        self.ui_manager.add_ui_element(self.input)
    
    def on_draw(self):
        x=self.window.width
        y=self.window.height
        ac.start_render()
        # Put the text on the screen.
        ac.draw_text(self.text,x//2,y//2,ac.color.WHITE,font_size=16,anchor_x='center')
        output_total = f"Total Score: {self.score}"
        ac.draw_text(output_total, 10, 10, ac.color.WHITE, 14)
        ac.finish_render()
    
    def on_key_press(self,symbol,modifiers):
            self.start=True
    
    def on_update(self, delta_time):
        if self.start==True:
            self.time_taken += delta_time
            for i,c in enumerate(self.text):
                try:
                    if self.input.text[i]==c:
                        self.correct_input+=1
                except:
                    pass

            if len(self.input.text)==len(self.text) and self.text!=self.empty:
                self.score+=1
                self.char+=len(self.text)
                self.input.text=self.empty
                self.text=self.empty
                self.sentences-=1
            
            if self.text==self.empty and self.sentences!=0:
                self.text=random.choice(sentences)
                GameView().on_draw()
            
            if self.sentences==0:
                self.wpm=(self.char/5)//(self.time_taken/60)
                self.accuracy=(self.correct_input/self.char)*100
                game_over_view = GameOverView()
                game_over_view.time_taken = self.time_taken
                game_over_view.wpm=self.wpm
                game_over_view.accuracy=self.accuracy
                game_over_view.char=self.char
                game_over_view.wrong_input=self.correct_input
                self.window.set_mouse_visible(True)
                self.window.show_view(game_over_view)


class GameOverView(ac.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.wpm=0
        self.accuracy=0
        self.char=0
        self.wrong_input=0
    def on_show(self):
        ac.set_background_color(ac.color.BLACK)
    def on_draw(self):
        ac.start_render()
        """
        Draw "Game over" across the screen.
        """
        ac.draw_text("Game Over",SCREEN_WIDTH//2, 400, ac.color.WHITE, 54,anchor_x='center')
        ac.draw_text("Click to restart", SCREEN_WIDTH//2, 300, ac.color.WHITE, 24,anchor_x='center')
        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        ac.draw_text(f"Time taken: {time_taken_formatted}",SCREEN_WIDTH/2,200,ac.color.GRAY,font_size=15,anchor_x="center")
        ac.draw_text(f"words per minute (WPM): {self.wpm}",SCREEN_WIDTH/2,150,ac.color.GRAY,font_size=15,anchor_x='center')
        ac.draw_text(f"Accuracy: {self.wrong_input}%",SCREEN_WIDTH/2,100,ac.color.GRAY,font_size=15,anchor_x='center')
        ac.draw_text(f"Characters: {self.char}",SCREEN_WIDTH/2,50,ac.color.GRAY,font_size=15,anchor_x='center')

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)



if __name__ == '__main__':
    window = ac.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE,resizable=True)
    view = MainMenu()
    window.show_view(view)
    ac.run()