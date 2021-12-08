from components import vars
from emoji import emojize
from colorama import Fore, Back

def total(value):

    if value <= 20:
        vars.character = vars.characters[0]

        print( "You are a "  + vars.character)

        import emoji
        print(emoji.emojize('Your inner character is :rabbit:'))
        
        print(Fore.BLUE + Back.WHITE + 'You are gentle, quiet, modest and courteous. Moreover, you are conscientious, careful and have a high sense of responsibility. You always have a lot of people to help you and you are very popular. ')
        
        print(Back.BLUE + Fore.WHITE +'==============================================Congratulations!============================================================================')
        
        import emoji
        print(emoji.emojize('==========================================    :cherry_blossom:   :cherry_blossom:   :cherry_blossom:    ==========================================================='))

    if 20< value <= 40:
        vars.character = vars.characters[1]

        print("You are a "  +  vars.character)

        import emoji
        print(emoji.emojize('Your inner character is  :cat:'))
        
        print(Fore.YELLOW  + 'You are perceptive and have an extraordinary insight into the human heart. You are clearly principled with firm bottom lines.You are a very charming person.')
        
        print(Back.BLUE + Fore.WHITE +'=============================================Congratulations!==============================================================================')
        
        import emoji
        print(emoji.emojize('=============================================    :blossom: :blossom: :blossom:      =================================================================================='))

    if 40< value <= 60:
        vars.character = vars.characters[2]

        print("You are a "  +  vars.character)

        import emoji
        print(emoji.emojize('Your inner character is  :leopard:'))
        print(Fore.RED  + 'You were born to be a leader. You are very clear about your position, always ahead of others, have a strong sense of purpose to the dream, you are smart, smart, subtle. You easily attract attention in a crowd and have a strong personality. ')
        
        print(Back.BLUE + Fore.WHITE +'========================================================Congratulations!===============================================================')
        
        import emoji
        print(emoji.emojize('=====================================================    :maple_leaf:  :maple_leaf:   :maple_leaf:    ===================================================='))

       
        # run the pillow function to show an image
        # pillow.show(vars.images[0])