# Project 1: Mad Libs Adventure Game
#Mad Libs Game

def generate_mad_libs():
    print("Welcome to my Mad Libs Adventure Game!")

    # User inputs necessary for the story
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    noun2 = input("Enter another noun: ")
    adjective2 = input("Enter another adjective: ")

    # Story Overview
    story = f'''
    Once upon a time in {place}, there was a {adjective} {noun} that loved to {verb}.
    One day, it met a {adjective2} {noun2}, and they became best friends.
    '''

    print("\nHere is your Mad Libs Story!")
    print(story)

# Call the function
generate_mad_libs()
