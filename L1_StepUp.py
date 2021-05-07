from karel.stanfordkarel import *

"""
File: StepUp.py
--------------------
Karel should pick up the beeper and put it on the ledge
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
    step_up()
    put_beeper()
    while front_is_clear():
        move()

def step_up():
    turn_left()
    move()
    turn_right()
    move()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program('StepUp.w')
