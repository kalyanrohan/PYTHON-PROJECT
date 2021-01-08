import arcade as ac
import random
import time
import arcade.gui
from arcade.gui import UIManager
from arcade.gui.ui_style import UIStyle
import os
SCREEN_WIDTH = 1460
SCREEN_HEIGHT = 720
SCREEN_TITLE = "TYPO"
f=open('sentences.txt',mode='r',encoding='utf-8')
sentences=f.read().split('\n')
number=""


class Button(ac.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    def on_click(self):
        if self.text.lower()=="play":
            ac.View().window.show_view(InstructionView())
        elif self.text.lower()=='quit':
            ac.View().window.close()
        elif self.text.lower()=="start":
            ac.View().window.show_view(GameView())
        elif self.text.lower()=="back":
            ac.View().window.show_view(MainMenu())


class MyGhostFlatButton(arcade.gui.UIGhostFlatButton):

    def __init__(self, center_x, center_y, input_box):
        super().__init__(
            'Start',
            center_x=center_x,
            center_y=center_y,
            width=250,
            # height=20
        )
        self.input_box = input_box

    def on_click(self):
        """ Called when user lets off button """
        GameView().sentences=1
        ac.View().window.show_view(GameView())


class MainMenu(ac.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self.background=None
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
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        y=self.window.height//2
        x=self.window.width//2
        play_button=Button(text="Play",center_x=x,center_y=y,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(play_button)
        how_to_play_button= Button(text="How To Play", center_x=x,center_y=y-150,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(how_to_play_button)
        quit_button=Button(text="Quit",center_x=x,center_y=y-300,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(quit_button)


class InstructionView(ac.View):
    def __init__(self):
        super().__init__()
        self.number_of_sentences=ac.gui.UIInputBox(self.window.width//2,self.window.height//2,200)
        self.ui_manager=UIManager()
        self.start=None
        self.back=None
        self.input=""
    
    def on_show_view(self):
        ac.set_background_color(ac.color.ORANGE_PEEL)
        self.setup()
    
    
    def on_draw(self):
        ac.start_render()
        ac.draw_text("How many sentences?", self.window.width/2, self.window.height/2+150,ac.color.WHITE, font_size=50, anchor_x="center")    

    
    def setup(self):
        self.ui_manager.purge_ui_elements
        y=self.window.height//2
        x=self.window.width//2
        self.start= MyGhostFlatButton(center_x=x,center_y=y//2,input_box=self.number_of_sentences)
        self.ui_manager.add_ui_element(self.start)
        self.back=Button(text="Back",center_x=x,center_y=y//4,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(self.back)
        self.ui_manager.add_ui_element(self.number_of_sentences)
    
    def on_update(self,delta_time):
        global number
        number=self.number_of_sentences.text

    
    def on_hide_view(self):
        print(number)
        print(f"2{GameView().sentences}")
        self.ui_manager.unregister_handlers()
    

class HowToPlay(ac.View):
    def __init__(self):
        super().__init__()
        self.ui_manager=UIManager()


    def on_show_view(self):
        ac.set_background_color(ac.color.RED)
        self.setup()


    def on_hide_view(self):
        self.ui_manager.unregister_handlers()


    def setup(self):
        self.ui_manager.purge_ui_elements()
        y=self.window.height//2
        x=self.window.width//2
        back_button=Button(text="Back",center_x=x,center_y=y-300,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(back_button)
        play_button=Button(text="Play",center_x=x,center_y=y-150,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(play_button)
           
    def on_draw(self):
        ac.start_render()
        ac.draw_text("Insert How to Play",self.window.width/2,self.window.height/2,ac.color.WHITE,16)



class GameView(ac.View):
    
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.score=0
        self.text=random.choice(sentences)
        self.ui_manager=UIManager()
        self.input=ac.gui.UIInputBox(self.window.width//2,self.window.height//3,1200)
        self.empty=''
        self.sentences=int(number)
        self.wpm=0
        self.start=False
        self.accuracy=0
        self.char=0
        self.correct_input=0
        self.sfx=ac.load_sound(path='typingsfx.mp3',streaming=True)
        self.background = None

    def on_show_view(self):
        """ Called once when view is activated. """
        ac.set_background_color(ac.color.BLACK)
        self.setup()
        
    
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    def setup(self):
        print(self.sentences)
        self.score=0
        self.input.text= self.empty
        self.ui_manager.purge_ui_elements()
        self.input.cursor_index = len(self.input.text)
        self.input.set_style_attrs(font_size=14)
        self.ui_manager.add_ui_element(self.input)
        print(f'printed{self.sentences}')

    
    def on_draw(self):
        x=self.window.width
        y=self.window.height
        ac.start_render()
        # Put the text on the screen.
        ac.draw_text(self.text,x//2,y//2,ac.color.WHITE,font_size=16,anchor_x='center')
        output_total = f"Total Score: {self.score}"
        ac.draw_text(output_total, 10, 10, ac.color.WHITE, 14)
        


    
    def on_key_press(self,symbols,modifiers):
            self.start=True
            ac.play_sound(self.sfx,1.0)
            for i,c in enumerate(self.text):
                try:
                    if self.input.text[i]!=c:
                        self.input._set_color(ac.color.RED)
                        break
                    elif self.input.text[i]==c:
                        self.input._set_color(ac.color.GREEN)
                        continue
                except:
                    pass

    
    def on_update(self, delta_time):
        if self.start==True:
            self.time_taken += delta_time

            if len(self.input.text)==len(self.text) and self.text!=self.empty:
                for i,c in enumerate(self.text):
                    try:
                        if self.input.text[i]==c:
                            self.correct_input+=1

                    except:
                        pass
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
                game_over_view.correct_input=self.correct_input
                self.window.show_view(game_over_view)



class GameOverView(ac.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.wpm=0
        self.accuracy=0
        self.char=0
        self.correct_input=0
    def on_show(self):
        ac.set_background_color(ac.color.BLACK)
    def on_draw(self):
        ac.start_render()

        ac.draw_text("Game Over",SCREEN_WIDTH//2, 400, ac.color.WHITE, 54,anchor_x='center')
        ac.draw_text("Click to restart", SCREEN_WIDTH//2, 300, ac.color.WHITE, 24,anchor_x='center')
        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        ac.draw_text(f"Time taken: {time_taken_formatted}",SCREEN_WIDTH/2,200,ac.color.GRAY,font_size=15,anchor_x="center")
        ac.draw_text(f"words per minute (WPM): {self.wpm}",SCREEN_WIDTH/2,150,ac.color.GRAY,font_size=15,anchor_x='center')
        ac.draw_text(f"Accuracy: {self.accuracy}%",SCREEN_WIDTH/2,100,ac.color.GRAY,font_size=15,anchor_x='center')
        ac.draw_text(f"Characters: {self.char}",SCREEN_WIDTH/2,50,ac.color.GRAY,font_size=15,anchor_x='center')

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.show_view(InstructionView())



if __name__ == '__main__':
    window = ac.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE,resizable=True)
    view = MainMenu()
    window.show_view(view)
    ac.run()

