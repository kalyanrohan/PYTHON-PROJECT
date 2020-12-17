import arcade as ac

#testing out the functions
SCREEN_WIDTH= 1280
SCREEN_HEIGHT= 720
SCREEN_TITLE= "Typo"

def main():
    ac.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,resizable=True)
    ac.set_background_color(ac.color.AERO_BLUE)
    ac.start_render()
    draw_rectangle(200,100)
    ac.finish_render()
    ac.run()

def draw_rectangle(x,y):
    ac.draw_rectangle_outline(x,y,y-200,x-100,ac.color.ALLOY_ORANGE)

main()