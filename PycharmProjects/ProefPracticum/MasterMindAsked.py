# The definition of ALL_COLORS is repeated here. That repitition can
# be avoided, but it would lead us to far at this point.
ALL_COLORS = ("red", "green", "blue", "yellow", "orange", "white")


def get_nb_black_white_matches(given, guess):
    """ Return the number of black and white matches of the guessed
    combination with respect to the given combination. The first
    element in the resulting tuple reflects the number of correct colors
    on their positions (black matches). The second element reflects
    the number of correct colors not on their position (white matches)."""
    i=0
    black_matches=0
    white_matches=0
    while i<len(given):
        if guess[i]==given[0] or guess[i]==given[1] \
                     or guess[i]==given[2] or guess[i]==given[3]:
            white_matches+=1
            if guess[i]==given[i]:
                white_matches+=-1
                black_matches+=1
        i+=1
    return (black_matches, white_matches)


import random

def create_combination(nb_elements):
    """ Return a random combination of colors involving the number of elements."""
    i=0
    given=[]
    while i < nb_elements:
        given.append(random.choice (ALL_COLORS))
        i += 1
    return given




# ! on the board, each row will consist of 4 circles representing 1 guess
# ! in total 10 rows should be drawn (as the user is given 10 guesses)
# ! You can create a circle by using the function:
# !     canvas.create_oval(x0, y0, x1, y1)
# ! It takes two pairs of coordinates: the top left and bottom right
# ! corners of the bounding rectangle. The (0,0) point is located in the
# ! top left corner of the canvas. We assume that each bounding square has
# ! a size of 30x30 and that all the circles are separated by 10 pixels
# ! from each other, and from the border (see picture in assignment).
# ! For example, the method call (with actual parameters) that generates
# ! the second circle of the third guess will look like:
# !         canvas.create_oval(50, 90, 80, 120)
# ! Later on in the program we modify the ovals to change color depending on
# ! the color that is selected by the person playing.
# ! In order to easily retrieve the correct oval, we expect that the function
# ! you implement here returns a nested list (i.e. a matrix) of
# ! the following form:
# !         [[circle1_guess1, circle2_guess1, ...],
# !          [circle1_guess2, ...],
# !          ...,
# !          [circle4_guess10]]
# ! The second circle of the third guess would for example be stored at:
# !          ovals[2][1] = canvas.create_oval(50, 90, 80, 120)
# ! Instead of approaching the nested list as a matrix, you can also
# ! treat it as a list of lists
# !          e.g. ovals[2].append(...)
# ! Note that the method create_oval has an implementation that
# ! takes 5 parameters. The fifth parameter has name 'fill' and allows
# ! you to assign a color (as a string) to it.
# ! Make sure that all the circles you draw get the fill color "grey".

def create_empty_circles(canvas, number_of_circles, max_number_of_moves):
    """ Return a matrix containing grey ovals that are correctly initialized
        at their required location."""
    
    i=0
    j=0
    ovals=[[circle1_guess1, circle2_guess1, circle3_guess1, circle4_guess1],\
           [circle1_guess2, circle2_guess2, circle3_guess2, circle4_guess2],\
           [circle1_guess3, circle2_guess3, circle3_guess3, circle4_guess3],\
           [circle1_guess4, circle2_guess4, circle3_guess4, circle4_guess4],\
           [circle1_guess5, circle2_guess5, circle3_guess5, circle4_guess5],\
           [circle1_guess6, circle2_guess6, circle3_guess6, circle4_guess6],\
           [circle1_guess7, circle2_guess7, circle3_guess7, circle4_guess7],\
           [circle1_guess8, circle2_guess8, circle3_guess8, circle4_guess8],\
           [circle1_guess9, circle2_guess9, circle3_guess9, circle4_guess9],\
           [circle1_guess10, circle2_guess10, circle3_guess10, circle4_guess10]]

    while j<10:
        ovals[i][j]=canvas.create_oval(10+i*40, 10+j*40, 40+i*40, 40+j*40)
        while i<4:
            i+=1
        j+=1


###############################################################################
# EXTRA

def any_color_in_combination(colors, given):
    """ Returns true if at least one color in colors is part of the
    given combination. False otherwise."""


def all_colors_in_combination(colors, given):
    """ Returns true if all the colors in colors are part of the
    given combination. False otherwise."""


def is_sublist_of(sublist, given):
    """ Returns whether the sublist is part of the given combination.
    The order of the sublist must also correspond to the order of the
    corresponding part in the given combination."""
