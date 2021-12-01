from component import vars
from emoji import emojize

def total(value):

    if value <= 20:
        vars.character = vars.characters[0]

        print("It's"  +  vars.character)

        import emoji
        print(emoji.emojize('Python is :fire:'))

    if value <= 40:
        vars.character = vars.characters[0]

        print("It's"  +  vars.character)

        import emoji
        print(emoji.emojize('Python is :thumbs_up:'))

    if value <= 50:
        vars.character = vars.characters[0]

        print("It's"  +  vars.character)
        import emoji
        print(emoji.emojize('Python is :heartpulse:'))