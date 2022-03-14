"""
Test for my functions.
Here I only tested the functions that actually make sense to use assert on.
"""

from my_module.functions import weather, bottoms_shoes, colors_mix

# Unit test for weather function
def test_weather():
    assert callable(weather)
    assert type(weather(63)) == str
    assert weather(63) == 'chilly'
    assert weather(102) == None

# Unit test for bottoms_shoes function
def test_bottoms_shoes():
    assert callable(bottoms_shoes)
    assert type(bottoms_shoes('hot')) == tuple
    assert len(bottoms_shoes('hot')) == 2
    assert bottoms_shoes('warm') == (None, None)

# Unit test for colors_mix function
def test_colors_mix():
    assert callable(colors_mix)
    assert type(colors_mix('red')) == str
    assert type(colors_mix('RED')) == str
    assert colors_mix('violet') == 'color should be primary: black, white, red, blue or yellow'  
