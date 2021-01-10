import arcade as ac
import random
import time
import arcade.gui
from arcade.gui import UIManager
from arcade.gui.ui_style import UIStyle

SCREEN_WIDTH = 1460
SCREEN_HEIGHT = 720
SCREEN_TITLE = "TYPO"
# opening the external text file for the sentences
f=open('sentences.txt',mode='r',encoding='utf-8')
# split the text into a list of sentences
sentences=f.read().split('\n')
# global variable that will store the number of sentences inputted by the user
number=""
# the global variable that will show whether the user has inputted an error
error=False

#arcade gui button class that we are going to be using for all of the buttons in the game
class Button(ac.gui.UIFlatButton):
    #This function triggers when the buttons are pressed
    def on_click(self):
        #using conditionals to trigger different events when different buttons are pressed
        #play button
        if self.text.lower()=="play":
            ac.View().window.show_view(SetupView())
        #quit button
        elif self.text.lower()=='quit':
            ac.View().window.close()
        #start button
        elif self.text.lower()=="start":
            """This start button is placed in the Instruction window where the user set up the number of sentences. 
            By using the try block, I can check wether the user input is in the correct format.
            I want the number of sentences to be in a integer fromat and that's why I used the isdigit() method to check that.
            Once the correct format is inputted, then the event will be triggered
            """
            try:
                if number.isdigit()==True:
                    # if the user input is an integer, switch to the game view or scene.
                    ac.View().window.show_view(GameView())
                else:
                    # if the user input is not an integer, the global varibale error will be set to true. I will explain what this do late on.
                    global error
                    error=True
            except ValueError:
                #when a noninteger is inputted, python will cause an error, but I want the program to keep running. Hence the 'pass'.
                pass
                
        #back button
        elif self.text.lower()=="back":
            ac.View().window.show_view(MainMenu())
        
        #how to play button
        elif self.text.lower()=="how to play":
            ac.View().window.show_view(HowToPlay())
    

#This class shows the main menu of the game. This
class MainMenu(ac.View):
    """
    This shows the main menu and the elements in this view. For the views, I used the arcade.view() model instead of the arcade.window()
    in order to switch to different scenes or views.
    """
    def __init__(self):
        super().__init__()
        # this ui manager is from the arcade module and it controls our UI such as buttons.
        self.ui_manager = UIManager()
        #drawing the background image
        self.background_image=ac.sprite.Sprite('computer-overhead-dribbb_1.gif',center_x=self.window.width//2,center_y=self.window.height//1.4,scale=0.3)
    
    """The on_draw method is called whenever we draw text,sprites and etc to the current view."""
    def on_draw(self):
        ac.start_render()
        # drawing the title
        ac.draw_text(SCREEN_TITLE,(self.window.width//2-100),self.window.height//1.2,ac.color.WHITE,72,align='center')
        # drawing the bg image
        self.background_image.draw()
    
    """ Called once when view is activated. """
    def on_show_view(self):
        #calling the setup function whenever we switch to this view to setup our view.
        self.setup()
        #setting the bg color
        ac.set_background_color(ac.color.BLUEBERRY)
    
    """ Called once when view is deactivated. """
    def on_hide_view(self):
        #removes the handlers of this view when we switch to another view from this view.
        self.ui_manager.unregister_handlers()
    
    """ Everything under this function will run everytime we switch to this view  """
    def setup(self):
        #Removes all UIElements which were added to the UIManager()
        self.ui_manager.purge_ui_elements()
        # Loads the background image
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")
        y=self.window.height//2
        x=self.window.width//2
        #play button gui
        play_button=Button(text="Play",center_x=x,center_y=y,width=200,height=100,align='center')
        #using the inbuilt method in the UIManager() to add gui elements
        self.ui_manager.add_ui_element(play_button)
        #how to playy button gui
        how_to_play_button= Button(text="How To Play", center_x=x,center_y=y-150,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(how_to_play_button)
        #quit button gui
        quit_button=Button(text="Quit",center_x=x,center_y=y-300,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(quit_button)


""""This is the view for setting up the number of sentences for the game"""
class SetupView(ac.View):
    def __init__(self):
        super().__init__()
        # We use an input box from the arcade module to get the user's input
        self.number_of_sentences=ac.gui.UIInputBox(self.window.width//2,self.window.height//2,200)
        # same ui manager as the above. Note that we will be using the same thing for all of the views.
        self.ui_manager=UIManager()
        #initializing our start button
        self.start=None
        #initializing our back button
        self.back=None
        
    """ Called once when view is activated. """
    def on_show_view(self):
        #setting the bg color
        ac.set_background_color(ac.color.ORANGE_PEEL)
        #calling the setup function when this view activates
        self.setup()
    
    """The on_draw method is called whenever we draw text,sprites and etc to the current view."""
    def on_draw(self):
        ac.start_render()
        # Draw text
        ac.draw_text("Please enter the number of sentences.", self.window.width/2, self.window.height/2+200,ac.color.WHITE, font_size=50, anchor_x="center")    
        # If a non integer is entered, it will result in an error. The following text will only be drawn once there is an error.
        if error==True:
            ac.draw_text("Please enter an integer!.", self.window.width/2, self.window.height/2+150,ac.color.RED, font_size=30, anchor_x="center")    


    """ Everything under this function will run everytime we switch to this view  """
    def setup(self):
        #Removes all UIElements which were added to the UIManager()
        self.ui_manager.purge_ui_elements
        
        y=self.window.height//2
        x=self.window.width//2
        #set the start button
        self.start= Button(text="Start",center_x=x,center_y=y//1.5,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(self.start)
        #set the back button
        self.back=Button(text="Back",center_x=x,center_y=y//4,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(self.back)
        #adding the input box
        self.ui_manager.add_ui_element(self.number_of_sentences)
    
    """ All the logic, changes and input is written under here. 
    delta_time is a built in parameter that allows for real time changes to occur.  """
    def on_update(self,delta_time):
        global number
        # Storing the input from the user in the global variable called number.
        number=self.number_of_sentences.text

    """ Called once when view is deactivated. """
    def on_hide_view(self):
        #removes the handlers of this view when we switch to another view from this view.
        self.ui_manager.unregister_handlers()
    

""" This class is ued to show the guide of the game"""
class HowToPlay(ac.View):
    def __init__(self):
        super().__init__()
        self.ui_manager=UIManager()
        self.emerald=ac.sprite.Sprite('Emerald Gem05.png',center_x=self.window.width//1.5,center_y=self.window.height//3)
        self.ruby=ac.sprite.Sprite('Ruby Gem_5.png',center_x=self.window.width//4.5,center_y=self.window.height//10.5)
        self.sapphire=ac.sprite.Sprite('Sapphire Gem05.png',center_x=self.window.width//4.5,center_y=self.window.height//4.5)
        self.topaz=ac.sprite.Sprite('Topaz Gem10.png',center_x=self.window.width//1.5,center_y=self.window.height//4.5)
        self.blue_gem=ac.sprite.Sprite('Aquamarine Gem05.png',center_x=self.window.width//4.5,center_y=self.window.height//3)

    """ Called once when view is activated. """
    def on_show_view(self):
        ac.set_background_color(ac.color.RED)
        self.setup()

    """ Called once when view is deactivated. """
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    """ Everything under this function will run everytime we switch to this view  """
    def setup(self):
        #Removes all UIElements which were added to the UIManager()
        self.ui_manager.purge_ui_elements()
        
        y=self.window.height//2
        x=self.window.width//2
        # add back button
        back_button=Button(text="Back",center_x=x,center_y=y-300,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(back_button)
        # add play button
        play_button=Button(text="Play",center_x=x,center_y=y-150,width=200,height=100,align='center')
        self.ui_manager.add_ui_element(play_button)
    
    """The on_draw method is called whenever we draw text,sprites and etc to the current view."""       
    def on_draw(self):
        ac.start_render()
        # drawing the guide text and sprites to the view
        ac.draw_text("How to Play",self.window.width/2,self.window.height/2+270,ac.color.WHITE,40,align="center",anchor_x="center")
        ac.draw_text("1. Enter the number of sentences that you want.",self.window.width/2,self.window.height/2+200,ac.color.WHITE,30,align="center",anchor_x="center")
        ac.draw_text("2. Start Typing in the box to start the game.",self.window.width/2,self.window.height/2+150,ac.color.WHITE,30,align="center",anchor_x="center")
        ac.draw_text("3. If the color of the box becomes red, then you have made a TYPO! \n If the box turns green then, you have inputted everything correctly.",self.window.width/2,self.window.height/2+75,ac.color.WHITE,30,align="center",anchor_x="center")
        ac.draw_text("4. You can see your typo percentage bottom left, The lower it is, the better. \n There are tiers or ranks for your typing skill and this is based on the typo rate \n or percentage and the speed of your typing (WPM)",self.window.width/2,self.window.height/2-50,ac.color.WHITE,30,align="center",anchor_x="center")
        self.emerald.draw()
        self.ruby.draw()
        self.blue_gem.draw()
        self.topaz.draw()
        self.sapphire.draw()
        ac.draw_text("SSS Tier",self.window.width//4.5+100,self.window.height//3,ac.color.WHITE,20,align="center",anchor_x="center")
        ac.draw_text("S Tier",self.window.width//4.5+100,self.window.height//4.5,ac.color.WHITE,20,align="center",anchor_x="center")
        ac.draw_text("A Tier",self.window.width//4.5+100,self.window.height//10.5,ac.color.WHITE,20,align="center",anchor_x="center")
        ac.draw_text("B Tier",self.window.width//1.5+100,self.window.height//3,ac.color.WHITE,20,align="center",anchor_x="center")
        ac.draw_text("C Tier",self.window.width//1.5+100,self.window.height//4.5,ac.color.WHITE,20,align="center",anchor_x="center")

""" The main game. This is where the user plays."""
class GameView(ac.View):
    
    def __init__(self):
        super().__init__()
        #initializing all the necessary attributes
        self.time_taken = 0
        self.typo=0
        self.wrong_input=0
        # the sentences that the user will be typing in. It is randomly generated from an external .txt file
        self.text=random.choice(sentences)
        self.ui_manager=UIManager()
        # the user will be typing in the sentences inside this UI Input Box from the arcade module.
        self.input=ac.gui.UIInputBox(self.window.width//2,self.window.height//3,1200)
        self.empty=''
        #the number of sentences will be the input from the user on the SetupView(). We change to int as the input is stored in a str.
        self.sentences=int(number)
        self.wpm=0
        self.start=False
        self.accuracy=0
        self.char=0
        self.correct_input=0
        # loading the typing sfx
        self.sfx=ac.load_sound(path='typingsfx.mp3',streaming=True)
        self.background = None
        self.start_text=""

    """ Called once when view is activated. """
    def on_show_view(self):
        ac.set_background_color(ac.color.BLACK)
        self.setup()
        
    """ Called once when view is deactivated. """
    def on_hide_view(self):
        self.ui_manager.unregister_handlers()
    
    """ Everything under this function will run everytime we switch to this view  """
    def setup(self):
        self.typo=0
        self.wrong_input=0
        self.start_text="Start Typing to Start!"
        self.char=len(self.text)
        self.input.text= self.empty
        self.ui_manager.purge_ui_elements()
        self.input.cursor_index = len(self.input.text)
        self.input.set_style_attrs(font_size=14)
        self.ui_manager.add_ui_element(self.input)

    """The on_draw method is called whenever we draw text,sprites and etc to the current view."""
    def on_draw(self):
        x=self.window.width
        y=self.window.height
        ac.start_render()
        # Put the sentence that the user should type on the screen.
        ac.draw_text(self.text,x//2,y//2,ac.color.WHITE,font_size=16,anchor_x='center')
        typo = f"Typo: {self.typo}%"
        # drawing the rate of typo to the bottom of the view
        ac.draw_text(typo, 10, 10, ac.color.WHITE, 14)
        # a guide text to tell the users how to start the game. This will be gone once the game starts.
        ac.draw_text(self.start_text,x//2,y//1.5,ac.color.WHITE,font_size=16,anchor_x='center')
        
    """ This function will be called when the user inputs any kind of keystroke """
    def on_key_press(self,symbols,modifiers):
            # once the user starts typing, we start the game
            self.start=True
            # deleting the guide text
            self.start_text=""
            # whenever there is a keystroke, the sfx will play
            ac.play_sound(self.sfx,1.0)
            
            # iterating the sentences and user input.
            for i,c in enumerate(self.text):
                # using the try block to allow iteration of multiple inputs and tries
                try:
                    # checking whether the character inputted is not the same with the one in the sentence
                    if self.input.text[i]!=c:
                        # excluding the backspace key so that it doesn't trigger any events. Backspace key is stored as 65288
                        if symbols!=65288:
                            """ if backspace is not entered and the input doesn't match, we will add 1 to the wrong_input
                            and set the input box color to red to indicate that a mistake have been made.
                            """
                            self.wrong_input+=1
                            self.input._set_color(ac.color.RED)
                        # we break the loop
                        break
                    # the loop then continues once the user enters the correct character.
                    elif self.input.text[i]==c:
                        # whenever the input is correct, the box will stay green.
                        self.input._set_color(ac.color.GREEN)   
                except:
                    pass

    """ All the logic, changes and input is written under here. 
    delta_time is a built in parameter that allows for real time changes to occur.  """
    def on_update(self, delta_time):
        # all of the code will only run when the user enters a keystroke.
        if self.start==True:
            # to make life easier, instead of using the time module, I use delta time which is a running clock in seconds.
            self.time_taken += delta_time
            # I will keep udpating the rate of typo. I use the percentage of wrong input from the total input or characters.
            self.typo=self.wrong_input/self.char*100
            
            # when the user enters the same number of characters as the sentence and the sentence is not empty
            if len(self.input.text)==len(self.text) and self.text!=self.empty:
                # I will use the same iteration to go through the sentence and input text
                for i,c in enumerate(self.text):
                    # using the try block to allow iteration of multiple inputs and tries
                    try:
                        # check whether the input matches the characters in the sentence.
                        if self.input.text[i]==c:
                            # if it matches we add one to correct input
                            self.correct_input+=1
                    # dont want any error so.....
                    except:
                        pass
                # reset the input box to an empty string
                self.input.text=self.empty
                # reset the text
                self.text=self.empty
                # subtrac one from the number of sentences
                self.sentences-=1
            # when everything is resetted
            if self.text==self.empty and self.sentences!=0:
                # we randomize again the sentence
                self.text=random.choice(sentences)
                # drawing the next sentence
                GameView().on_draw()
                # resetting the color of the input box
                self.input._set_color(ac.color.WHITE)
                # adding the length of characters of the sentence to the total number of characters
                self.char+=len(self.text)

            # when the game is over
            if self.sentences==0:
                # calculating the speed of typing
                self.wpm=(self.char/5)//(self.time_taken/60)
                # calculating the accuracy of typing
                self.accuracy=(self.correct_input//self.char)*100
                game_over_view = GameOverView()
                # setting the attributes' values for the game_over_view with the already calculated attribute from the game view.
                game_over_view.time_taken = self.time_taken
                game_over_view.wpm=self.wpm
                game_over_view.accuracy=self.accuracy
                game_over_view.char=self.char
                game_over_view.correct_input=self.correct_input
                game_over_view.typo=self.typo
                # change view to the game over view
                self.window.show_view(game_over_view)



class GameOverView(ac.View):
    def __init__(self):
        super().__init__()
        # since we have set the values to be the same as the one in the game view, they will later on change accordingly.
        self.time_taken = 0
        self.wpm=0
        self.accuracy=0
        self.char=0
        self.correct_input=0
        self.typo=0
        # setting up the sprites for the rank
        self.emerald=ac.sprite.Sprite('Emerald Gem05.png',center_x=self.window.width//2,center_y=self.window.height//2)
        self.ruby=ac.sprite.Sprite('Ruby Gem_5.png',center_x=self.window.width//2,center_y=self.window.height//2)
        self.sapphire=ac.sprite.Sprite('Sapphire Gem05.png',center_x=self.window.width//2,center_y=self.window.height//2)
        self.topaz=ac.sprite.Sprite('Topaz Gem10.png',center_x=self.window.width//2,center_y=self.window.height//2)
        self.rainbow=ac.sprite.Sprite('round_gem.png',center_x=self.window.width//2,center_y=self.window.height//1.75,scale=0.25)
        self.blue_gem=ac.sprite.Sprite('Aquamarine Gem05.png',center_x=self.window.width//2,center_y=self.window.height//2)
    
    """ Called once when view is activated. """
    def on_show(self):
        ac.set_background_color(ac.color.BLACK)
    
    """ function used to type the rank easier since all of them have the same format """
    def rank(self,text):
        ac.draw_text(text,self.window.width/2,self.window.height//1.45,ac.color.NEON_CARROT,font_size=15,anchor_x='center',align='center')

    """The on_draw method is called whenever we draw text,sprites and etc to the current view."""
    def on_draw(self):
        ac.start_render()
        # rounding off the numbers to two decimal places
        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        typo_formatted = f"{round(self.typo, 2)} %"
        
        # drawing the necessary text to show the results
        ac.draw_text("Game Over",self.window.width//2, self.window.height//1.25, ac.color.WHITE, 54,anchor_x='center')
        ac.draw_text(f"Typo Rate: {typo_formatted}",self.window.width/2,self.window.height//3,ac.color.RED,font_size=15,anchor_x="center")
        ac.draw_text("Click to restart", self.window.width//2, self.window.height//2.5, ac.color.WHITE, 24,anchor_x='center')
        ac.draw_text(f"Time taken: {time_taken_formatted}",self.window.width/2,self.window.height//3.5,ac.color.GREEN,font_size=15,anchor_x="center")
        ac.draw_text(f"words per minute (WPM): {self.wpm}",self.window.width/2,self.window.height//4.5,ac.color.BLUEBONNET,font_size=15,anchor_x='center')
        ac.draw_text(f"Accuracy: {self.accuracy}%",self.window.width/2,self.window.height//6,ac.color.YELLOW,font_size=15,anchor_x='center')
        ac.draw_text(f"Characters: {self.char}",self.window.width/2,self.window.height//9.5,ac.color.NEON_CARROT,font_size=15,anchor_x='center')
        
        # if typo rate is smaller or equal to 30 and typing speed smaller or equal to 40 but not 0 
        if self.typo<=30.00 and 40>=self.wpm>0:
            # draw the emerald sprite
            self.emerald.draw()
            # draw the respective texts
            GameOverView().rank("Rank: Emerald \n Not bad, You are actually decent.")
        # if typo rate is smaller or equal to 20 and typing speed smaller or equal to 60 but not 0 
        elif self.typo<=20.00 and 60>=self.wpm>0:
            # draw the topaz sprite
            self.topaz.draw()
            GameOverView().rank("Rank: Topaz \n What emerald????")
         # if typo rate is smaller or equal to 10 and typing speed smaller or equal to 70 but not 0 
        elif self.typo<=10.00 and 70>=self.wpm>0:
            # draw the ruby sprite
            self.ruby.draw()
            GameOverView().rank("Rank: Ruby \n Hey slow down there Mcqueen. You have good typing skills ngl.")
         # if typo rate is smaller or equal to 5 and typing speed smaller or equal to 80 but not 0
        elif self.typo<=5.00 and 80>=self.wpm>0:
            # draw the sapphire sprite
            self.sapphire.draw()
            GameOverView().rank("Rank: Sapphire \n I wonder what are the things that you do to have these speedy fingers.")
         # if typo rate is smaller or equal to 3 and typing speed smaller or equal to 100 but not 0
        elif self.typo<=3.00 and 100>=self.wpm>0:
            # draw the blue_gem sprite
            self.blue_gem.draw()
            GameOverView().rank("Rank: Blue Gem \n Ok time to dropout and join a pro team.")
         # if typo rate is equal to 0 and typing speed greater or equal to 120
        elif self.typo==0.00 and self.wpm>=120:
            # draw the rainbow sprite
            self.rainbow.draw()
            GameOverView().rank("Rank: Diamond Fingers \n Ayy what this god doing down on earth yeeeeeee. Congrats you have found the missing gem!")
        
    # changing the view to the Setup View when the mouse is clicked
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        self.window.show_view(SetupView())


# running the program
if __name__ == '__main__':
    window = ac.Window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE,resizable=False)
    view = HowToPlay()
    window.show_view(view)
    ac.run()

f.close()
