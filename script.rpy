# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character(_("Layla"), color="#ae5219")
define m = Character(("Kelly"), image="welch", color="#198eae")
define n = Character(("Kelly"), color="#198eae")
image side welch neutral = "welch neutral.png"
image side welch angry = "welch angry.png"
image side welch smug = "welch smug.png"
image side welch crying = "welch crying.png"
image side welch excited = "welch excited.png"
define p = Character("Punk")
 
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "cicadas.mp3"

    scene bg meadow
    with fade

    m neutral "It's the heat of the summer. It was exciting when exams were finally over, but..."
    n "This is a text with no image"
    m crying "This village is so boring. My parents really had to bring me to the boonies..."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene bg uni
    with fade

    show sylvie blue normal

    play music "jazz 1.mp3"

    # These display lines of dialogue.

    l "Good morning!"

    m smug "Hey Layla."

    show sylvie blue giggle
    with dissolve

    l "You look so down. Not excited for a new month?"

    m neutral "(Honestly, not really...)"

    l "We could always go to some place. Do you wanna go somewhere?"

    menu:
        m neutral "Might as well. let's go to..."

        "The canteen":
            jump canteen
        
        "Classroom":
            jump classroom

label canteen:

    show sylvie blue smile
    with dissolve

    l "Let's go!"

    scene bg club
    with fade

    "This is the canteen route."

    m excited "Oooh!"

    n ":OOOOO"

    n "..."
    
    m angry "{b}HEY!!{/b} Where's the tacos! I thought it was taco tuesday!"

    return

label classroom:

    show sylvie blue surprised
    with dissolve

    l "Sure, I'm surprised you're interested in going to class on a Saturday though."

    scene bg lecturehall
    with fade

    "This is the classroom route."
# This ends the game.

    return
