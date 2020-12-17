import arcade as ac
import random
import time
from functions import*

SCREEN_HEIGHT=720
SCREEN_WIDTH=1280
TITLE="TYPO"

class Typo(ac.Window):

    def __init__(self,width,height,title):
        super().__init__(width,height,title, resizable=True)
        self.set_location(200,50)
        
       
    

Typo(SCREEN_WIDTH,SCREEN_HEIGHT,TITLE)
ac.run()
