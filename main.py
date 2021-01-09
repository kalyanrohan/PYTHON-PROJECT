import arcade as ac
import random
import time
import arcade.gui
from arcade.gui import UIManager
from arcade.gui.ui_style import UIStyle

SCREEN_WIDTH = 1460
SCREEN_HEIGHT = 720
SCREEN_TITLE = "TYPO"
f=open('sentences.txt',mode='r',encoding='utf-8')
sentences=f.read().split('\n')
number=""
error=False


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
            try:
                if number.isdigit()==True:
                    ac.View().window.show_view(GameView())
                else:
                    global error
                    error=True
            except ValueError:
                pass
                
        elif self.text.lower()=="back":
            ac.View().window.show_view(MainMenu())
        
        elif self.text.lower()=="how to play":
            ac.View().window.show_view(HowToPlay())
    

class MainMenu(ac.View):
    """
    Main view. Really the only view in this example. """
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()
        self.background_image=ac.sprite.Sprite('computer-overhead-dribbb_1.gif',center_x=self.window.width//2,center_y=self.window.height//1.4,scale=0.3)
    def on_draw(self):
        """ Draw this view. GUI elements are automatically drawn. """
        ac.start_render()
        ac.draw_text(SCREEN_TITLE,(self.window.width//2-100),self.window.height//1.2,ac.color.WHITE,72,align='center')
        self.background_image.draw()
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
        ac.draw_text("Please enter the number of sentences.", self.window.width/2, self.window.height/2+200,ac.color.WHITE, font_size=50, anchor_x="center")    
        if error==True:
            ac.draw_text("Please enter an integer!.", self.window.width/2, self.window.height/2+150,ac.color.RED, font_size=30, anchor_x="center")    


    def setup(self):
        self.ui_manager.purge_ui_elements
        y=self.window.height//2
        x=self.window.width//2
        self.start= Button(text="Start",center_x=x,center_y=y//1.5,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(self.start)
        self.back=Button(text="Back",center_x=x,center_y=y//4,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(self.back)
        self.ui_manager.add_ui_element(self.number_of_sentences)
    
    def on_update(self,delta_time):
        global number
        number=self.number_of_sentences.text

    
    def on_hide_view(self):
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
        ac.draw_text("How to Play",self.window.width/2,self.window.height/2+270,ac.color.WHITE,40,align="center",anchor_x="center")
        ac.draw_text("1. Enter the number of sentences that you want.",self.window.width/2,self.window.height/2+200,ac.color.WHITE,30,align="center",anchor_x="center")
        ac.draw_text("2. Start Typing in the box to start the game.",self.window.width/2,self.window.height/2+150,ac.color.WHITE,30,align="center",anchor_x="center")
        ac.draw_text("3. If the color of the box becomes red, then you have made a TYPO! \nIf the box turns green then, you are good.",self.window.width/2,self.window.height/2+75,ac.color.WHITE,30,align="center",anchor_x="center")
        ac.draw_text("4. You can see your typo percentage below,",self.window.width/2,self.window.height/2,ac.color.WHITE,30,align="center",anchor_x="center")


class GameView(ac.View):
    
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.typo=0
        self.wrong_input=0
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
        self.typo=0
        self.wrong_input=0
        self.char=len(self.text)
        self.input.text= self.empty
        self.ui_manager.purge_ui_elements()
        self.input.cursor_index = len(self.input.text)
        self.input.set_style_attrs(font_size=14)
        self.ui_manager.add_ui_element(self.input)

    
    def on_draw(self):
        x=self.window.width
        y=self.window.height
        ac.start_render()
        # Put the text on the screen.
        ac.draw_text(self.text,x//2,y//2,ac.color.WHITE,font_size=16,anchor_x='center')
        typo = f"Typo: {self.typo}%"
        ac.draw_text(typo, 10, 10, ac.color.WHITE, 14)
        
    
    def on_key_press(self,symbols,modifiers):
            self.start=True
            ac.play_sound(self.sfx,1.0)
            for i,c in enumerate(self.text):
                try:
                    if self.input.text[i]!=c:
                        if symbols!=65288:
                            self.wrong_input+=1
                            self.input._set_color(ac.color.RED)
                        break
                    elif self.input.text[i]==c:
                        self.input._set_color(ac.color.GREEN)
                        
                except:
                    pass

    
    def on_update(self, delta_time):
        if self.start==True:
            self.time_taken += delta_time
            self.typo=self.wrong_input/self.char*100
            if len(self.input.text)==len(self.text) and self.text!=self.empty:
                for i,c in enumerate(self.text):
                    try:
                        if self.input.text[i]==c:
                            self.correct_input+=1
                    except:
                        pass
                self.input.text=self.empty
                self.text=self.empty
                self.sentences-=1
            
            if self.text==self.empty and self.sentences!=0:
                self.text=random.choice(sentences)
                GameView().on_draw()
                self.input._set_color(ac.color.WHITE)
                self.char+=len(self.text)

            if self.sentences==0:
                self.wpm=(self.char/5)//(self.time_taken/60)
                self.accuracy=(self.correct_input//self.char)*100
                game_over_view = GameOverView()
                game_over_view.time_taken = self.time_taken
                game_over_view.wpm=self.wpm
                game_over_view.accuracy=self.accuracy
                game_over_view.char=self.char
                game_over_view.correct_input=self.correct_input
                game_over_view.typo=self.typo
                self.window.show_view(game_over_view)



class GameOverView(ac.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.wpm=0
        self.accuracy=0
        self.char=0
        self.correct_input=0
        self.typo=0
        self.emerald=ac.sprite.Sprite('Emerald Gem05.png',center_x=self.window.width//2,center_y=self.window.height//2)
        self.ruby=ac.sprite.Sprite('Ruby Gem_5.png',center_x=self.window.width//2,center_y=self.window.height//2)
        self.sapphire=ac.sprite.Sprite('Sapphire Gem05.png',center_x=self.window.width//2,center_y=self.window.height//2)
        self.topaz=ac.sprite.Sprite('Topaz Gem10.png',center_x=self.window.width//2,center_y=self.window.height//2)
        self.rainbow=ac.sprite.Sprite('round_gem.png',center_x=self.window.width//2,center_y=self.window.height//1.75,scale=0.25)
        self.blue_gem=ac.sprite.Sprite('Aquamarine Gem05.png',center_x=self.window.width//2,center_y=self.window.height//2)
    def on_show(self):
        ac.set_background_color(ac.color.BLACK)
    
    def rank(self,text):
        ac.draw_text(text,self.window.width/2,self.window.height//1.45,ac.color.NEON_CARROT,font_size=15,anchor_x='center',align='center')

    def on_draw(self):
        ac.start_render()
        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        ac.draw_text("Game Over",self.window.width//2, self.window.height//1.25, ac.color.WHITE, 54,anchor_x='center')
        ac.draw_text(f"Typo Rate: {self.typo}",self.window.width/2,self.window.height//3,ac.color.RED,font_size=15,anchor_x="center")
        ac.draw_text("Click to restart", self.window.width//2, self.window.height//2.5, ac.color.WHITE, 24,anchor_x='center')
        ac.draw_text(f"Time taken: {time_taken_formatted}",self.window.width/2,self.window.height//3.5,ac.color.GREEN,font_size=15,anchor_x="center")
        ac.draw_text(f"words per minute (WPM): {self.wpm}",self.window.width/2,self.window.height//4.5,ac.color.BLUEBONNET,font_size=15,anchor_x='center')
        ac.draw_text(f"Accuracy: {self.accuracy}%",self.window.width/2,self.window.height//6,ac.color.YELLOW,font_size=15,anchor_x='center')
        ac.draw_text(f"Characters: {self.char}",self.window.width/2,self.window.height//9.5,ac.color.NEON_CARROT,font_size=15,anchor_x='center')
        if 20<self.typo<=30:
            self.emerald.draw()
        elif 10<self.typo<=20:
            self.topaz.draw()
        elif 5<self.typo<=10:
            self.ruby.draw()
        elif 3<self.typo<=5:
            self.sapphire.draw()
        elif 0<self.typo<=5:
            self.blue_gem.draw()
        elif self.typo==0.0:
            self.rainbow.draw()
            GameOverView().rank("Rank: Pure Diamond \n You are a god.")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.show_view(InstructionView())



if __name__ == '__main__':
    window = ac.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE,resizable=False)
    view = MainMenu()
    window.show_view(view)
    ac.run()

