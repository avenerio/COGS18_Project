"""A collection of function for doing my project."""

import random

def greeting():
    """Greets user and asks for the inputs that will be used all throughour the project. """
    
    # Get name, temperature, top and color from the user
    name = input('Hi, What is your name? ')
    temperature = input('What is the temperature in farenheit? ')
    top = input('What kind of top do you want to wear? ')
    color = input('What color is the top? ')
    
    return name, int(temperature), top, color

#Function on weather
def weather(temperature):
    """Given a temperature value it decides if the weather is going to feel chilly, hot or cold. 
    
    Parameters
    ----------
    temperature : int
        The number to be compared. 
    
    Returns
    -------
    output : str
        The way that the weather is going to feel like. 
    """
    
    # Use if/elif/else statements to know how the temperature is going to feel like
    if temperature > 60 and temperature < 72:
        temp = 'chilly'
    elif temperature >= 72 and temperature < 100:
        temp = 'hot'
    elif temperature <= 60:
        temp = 'cold'
    else:
        temp = None
        
    return temp

#Function on type of bottoms
#I can use random function to choose any of the choices in either of the lists

def bottoms_shoes(temp):
    """Given the temperature returns the bottoms and shoes for it. 
    
    Parameters
    ----------
    temp : str
        The temperature to be compared to check what kind of bottoms. 
    
    Returns
    -------
    choice_1 : str
        The bottoms that the student should use. 
    choice_2 : str
        The shoes that the student should use.
    """

    bottoms_chilly = ['jeans', 'long overalls']
    bottoms_hot = ['shorts', 'skirt', 'short overalls']
    bottoms_cold = ['leggings', 'leather pants', 'joggers']
    shoes_chilly = ['sneakers', 'loafers']
    shoes_cold = ['ankle boots', 'over the knee boots', 'knee high boots']
    shoes_hot = ['sandals', 'slides']
    
    # The if/elif/else loop, using random from ramdon package chooses a bottom from the list that temp belongs to.
    if temp == 'chilly':
        choice_1 = random.choice(bottoms_chilly)
        choice_2 = random.choice(shoes_chilly)
    elif temp == 'hot':
        choice_1 = random.choice(bottoms_hot)
        choice_2 = random.choice(shoes_hot)
    elif temp == 'cold':
        choice_1 = random.choice(bottoms_cold)
        choice_2 = random.choice(bottoms_cold)
    else:
        choice_1 = None
        choice_2 = None
    
    return choice_1, choice_2

#Function on mix of colors
#How about two colors come back

def colors_mix(color):
    """Given a primary color it randomly chooses a color that matches. 
    
    Parameters
    ----------
    color : str
        The color of the top the student wants to wear. 
    
    Returns
    -------
    choice : str
        The color that matches the given color of the top. 
    """
    
    lst_primary = ['black', 'white', 'red', 'yellow', 'blue']
    white_mix = ['black', 'red', 'yellow', 'blue', 'cyan', 'orange', 'pink','violet', 'indigo','chartreuse', 'orange']
    black_mix = ['white', 'red', 'yellow', 'blue', 'cyan', 'orange', 'pink','violet', 'indigo','chartreuse', 'orange']
    red_mix = ['cyan', 'orange', 'pink']
    blue_mix = ['yellow', 'violet', 'indigo']
    yellow_mix = ['blue', 'chartreuse', 'orange']
    
    # Makes the string all lowercase
    color = color.lower()
    
    #The first if/elif/else loop checks that the lowercase primary color is in our list to then assign a color that matches
    if color in lst_primary:
        # Then this loop uses random from the random package to choose a color from our list
        if color == 'black':
            choice = random.choice(black_mix)
        elif color == 'white':
            choice = random.choice(white_mix)
        elif color == 'red':
            choice = random.choice(red_mix)
        elif color == 'blue':
            choice = random.choice(blue_mix)
        elif color == 'yellow':
            choice = random.choice(yellow_mix)
        else:
            choice = None        
    else:
        choice = 'color should be primary: black, white, red, blue or yellow'
        
    return choice

#final function 
#should say goodbye 

def farewell():
    
    name, temperature, top, color = greeting()
    feels_like_temp = weather(temperature)
    outfit = bottoms_shoes(feels_like_temp)
    final_color = colors_mix(color)
    
    print('Hello ' + name + ' your outfit is ' + outfit[0] + ' and ' + outfit[1])
    print('The color that matches with ' + color + ' is ' + final_color)
    
farewell()