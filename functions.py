import arcade as ac

#testing out the functions
SCREEN_WIDTH= 1280
SCREEN_HEIGHT= 720
SCREEN_TITLE= "Typo"

def main():
    ac.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,resizable=True)
    ac.set_background_color(ac.color.BLACK)
    ac.start_render()
    draw_rectangle(0,-100,640)
    ac.finish_render()
    ac.run()

#function to draw rectangles
def draw_rectangle(x,y,w,h=w/3):
    ac.draw_rectangle_outline(x+640,y+360,w,h,ac.color.WHITE_SMOKE)

main()