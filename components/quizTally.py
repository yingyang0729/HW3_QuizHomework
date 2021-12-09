from components import vars
from emoji import emojize
from colorama import Fore, Back

def total(value):

    if value <= 20:
        vars.character = vars.characters[0]

        print( "You are "  + vars.character)

        import emoji
        print(emoji.emojize('Your inner character is :rabbit:'))
        
        print(Fore.BLUE + Back.WHITE + 'You are gentle, quiet, modest and courteous. Moreover, you are conscientious, careful and have a high sense of responsibility. You always have a lot of people to help you and you are very popular. ')
        
        import emoji
        print(emoji.emojize('==========================================    :cherry_blossom:   :cherry_blossom:   :cherry_blossom:    ==========================================================='))

        print(Back.BLUE + Fore.WHITE +'==============================================Congratulations!============================================================================')
        
       
    if 20< value <= 40:
        vars.character = vars.characters[1]

        print("You are "  +  vars.character)

        import emoji
        print(emoji.emojize('Your inner character is  :cat:'))
        
        print(Fore.YELLOW  + 'You are perceptive and have an extraordinary insight into the human heart. You are clearly principled with firm bottom lines.You are a very charming person.')

        import emoji
        print(emoji.emojize('=============================================    :blossom: :blossom: :blossom:      =================================================================================='))
        
        print(Back.BLUE + Fore.WHITE +'=============================================Congratulations!==============================================================================')
        
        

    if 40< value <= 60:
        vars.character = vars.characters[2]

        print("You are "  +  vars.character)

        import emoji
        print(emoji.emojize('Your inner character is  :goat:'))
        print(Fore.GREEN + Back.WHITE  + 'You are very strong and persistent in your goals, but you do not change the pace of life easily. You have a complete plan of your own.  To the outside world, you are a very reliable person, very talented, and calm and witty.  With you, the other person moved very relaxed and comfortable.')

        import emoji
        print(emoji.emojize('===========================================    :four_leaf_clover:  :four_leaf_clover:   :four_leaf_clover:   ===================================================='))

        print(Back.BLUE + Fore.WHITE +'=============================================Congratulations!===============================================================')

    if 60< value <= 80:
        vars.character = vars.characters[3]

        print("You are "  +  vars.character)

        import emoji
        print(emoji.emojize('Your inner character is  :leopard:'))
        print(Fore.RED  + 'You were born to be a leader. You are very clear about your position, always ahead of others, have a strong sense of purpose to the dream, you are smart, smart, subtle. You easily attract attention in a crowd and have a strong personality. ')
        
        import emoji
        print(emoji.emojize('===========================================    :maple_leaf:  :maple_leaf:   :maple_leaf:    ===================================================='))

        print(Back.BLUE + Fore.WHITE +'=============================================Congratulations!===============================================================')
        
        
    