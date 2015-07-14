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
    c = ''
    
    # Create the initial window.
    stdscr = curses.initscr()
    
    # Setup the display.  Make sure to catch all exceptions and revert to a normal terminal.
    try:
        curses.noecho()
        curses.cbreak()
        stdscr.keypad( 1)
        while running:
            if c == ord( 'u'):
                # Increment the count and display
                count = ( count + 1 ) % 100
                stringDisplay = "The current count: %02d" % ( count, )
                stdscr.addstr( 10, 0, stringDisplay)
            elif c == ord( 'd'):
                # Decrement the count and display
                count = ( count - 1 ) % 100
                stringDisplay = "The current count: %02d" % ( count, )
                stdscr.addstr( 10, 0, stringDisplay)
            elif c == ord( 'q'):
                running = False
            # Display the menu
            stdscr.addstr( 0, 0, "<systemName> Control Panel") # Display title
            stdscr.addstr( 1, 0, "  <hostName> - 0.10 0.01 0.00 - connected") # Realtime information
            stdscr.addstr( 3, 0, "Please choose an option:")
            stdscr.addstr( 4, 4, "u - Increment Counter")
            stdscr.addstr( 5, 4, "d - Decrement Counter")
            stdscr.addstr( 6, 4, "q - Quit")
            # Refresh the screen
            stdscr.refresh()
            # Wait for a character and perform an action based on input character.
            c = stdscr.getch()
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
