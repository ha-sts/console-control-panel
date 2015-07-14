#!/usr/bin/env python

### IMPORTS ###
import curses
import time

### GLOBALS ###
screenHeight = 24
screenWidth = 80

### FUNCTIONS ###

### CLASSES ###

### MAIN ###
def main():
    # Initiallize running variables
    running = True
    count = 0
    
    # Create the initial window.
    stdscr = curses.initscr()
    
    # Setup the display.  Make sure to catch all exceptions and revert to a normal terminal.
    try:
        curses.noecho()
        curses.cbreak()
        stdscr.keypad( 1)
        while True:
            stringDisplay = "The current count: %d" % ( count, )
            stdscr.addstr( 0, 0, stringDisplay)
            count = ( count + 1 ) % 100
            stdscr.refresh()
            time.sleep( 0.1)
    except Exception as ex:
        # Should do some sort of logging here.
        pass
    finally:
        # Return the terminal to a sane mode.
        stdscr.keypad( 0)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

if __name__ == '__main__':
    main()
