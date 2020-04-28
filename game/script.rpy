# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image bg start = "a1.png"
define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg start

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show a3 at left

    # These display lines of dialogue.

    e "Hi There"

    e "Finally you come to (game name). This is my story"

    e "It in my Fate to see you. Because my story is incomplete without you"

    e "My the small program of this (game name). Which resid in your small space of (RAM SIZE) RAM"

    e "Would you like help to reach my destination gate and end of (game name)"


    # This ends the game.

    return
