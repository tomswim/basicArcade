import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Welcome to Arcade OO"
RADIUS = 150


# Class
class Welcome(arcade.Window):
    # Main welcome window
    def __init__(self):
        # Initialize window

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
 
        # Set the background color 
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        #Called whenever you need to draw our window

        # Clear the screen and start drawing
        arcade.start_render()

        # Draw a blue circle
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE
        )



# Main code entry point
if __name__ == "__main__":
    app = Welcome()
    # Display everything
    arcade.run()