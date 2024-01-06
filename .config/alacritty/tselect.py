#!/usr/bin/python3
import sys
import argparse
import curses

# Create ArgumentParser object
parser = argparse.ArgumentParser()
# Define the options and their corresponding arguments
parser.add_argument('-s', '--string', help='Specify name of .yaml file in themes directory')
parser.add_argument('-n', '--number', type=int, help='Specify a 0-indexed int argument for theme in directory')
parser.add_argument('-c', '--cycle', action='store_true', help='Cycle through options with arrow keys')
# Parse arguments
args = parser.parse_args()
# If invalid usage, print help
if not args.string and not type(args.number) == int and not args.cycle:
    parser.print_usage()
    sys.exit(1)

selectedidx = 0

def settheme(idx: int, curs=None):
    # Read the content of the alacritty file
    with open('alacritty.yml', 'r') as f:
        alacritty_content = f.readlines()
    
    # Iterate through the lines and replace the required one
    for i in range(len(alacritty_content)):
        if alacritty_content[i].startswith('  - ~/.config/alacritty/themes/themes/'):
            alacritty_content[i] = f'  - ~/.config/alacritty/themes/themes/{theme_list[selectedidx]}\n'
            if curs: 
                curs.clear()
                curs.addstr(0, 0, f"Setting theme to {theme_list[selectedidx]} ({selectedidx})")
            else:
                print(f"Setting theme to {theme_list[selectedidx]} ({selectedidx})")
    # Write content back to the file
    with open('alacritty.yml', 'w') as f:
        f.writelines(alacritty_content)

# Read in themes
with open('themelist.txt', 'r') as f:
    theme_list = [line.strip() for line in f]
if type(args.number) == int:
    if args.number < 0 or args.number >= len(theme_list):
        print(f"index argument {args.number} out of range: 0-{len(theme_list)-1}")
        sys.exit(1)
    else:
        selectedidx = args.number
elif not args.cycle: # string arg provided
    if args.string not in theme_list:
        print(f"string file argument {args.string} not found")
        sys.exit(1)
    else:
        selectedidx = theme_list.index(args.string)
if not args.cycle: 
    settheme(selectedidx)
else: 
    # Initialize the curses library
    stdscr = curses.initscr()

    try:
        # setup the curses environment
        stdscr.nodelay(False) # wait for the user input
        stdscr.keypad(True) # enable special Key values such as curses.KEY_LEFT etc
        settheme(0, stdscr)
        with open('favs', 'w+') as favoritesfile:
            while True:
                # get the character
                char = stdscr.getch()
                if char == curses.KEY_LEFT:
                    selectedidx = (selectedidx-1) if selectedidx > 0 else len(theme_list)-1
                    settheme(selectedidx, curs=stdscr)
                elif char == curses.KEY_RIGHT:
                    selectedidx = (selectedidx+1) if selectedidx < len(theme_list)-1 else 0
                    settheme(selectedidx, curs=stdscr)
                elif char == 27: # Escape key
                    # Clean up the library when done
                    curses.nocbreak()
                    stdscr.keypad(False)
                    curses.echo()
                    curses.endwin()
                    sys.exit(1)
                elif char == 32: # Space bar
                    favoritesfile.write(f"{theme_list[selectedidx]} ({selectedidx})\n")
    finally:
        # Clean up the library when done
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
