import sys
from tkinter import *

import state
import A_Star_methods
import A_Star_Search

# Maximum and default grid size
MAX_N, DEFAULT_N = 60, 40
# The "default" colour for an unfilled grid cell
UNFILLED = '#fff'

ALREADY_EXPLORED = 11

MAXEXPLORED = 40


class GridApp:
    """The main class representing a grid of coloured cells."""
    # The colour palette
    colours = (UNFILLED, 'green', 'red', 'black', 'red', 'red', 'red',
               'magenta', 'cyan', 'yellow')
    ncolours = len(colours)

    def __init__(self, master, n, width=700, height=700, pad=2):
        """Initialize a grid and the Tk Frame on which it is rendered."""

        # Making array
        self.gridArray = [[0 for j in range(DEFAULT_N)] for i in range(DEFAULT_N)]
        self.currentState = state.StateClass()
        self.goalState = state.StateClass()
        self.currentStateFlag = False
        self.goalStateFlag = False
        self.currentStateCount = 0
        self.goalStateCount = 0

        # Number of cells in each dimension.
        self.n = n
        # Some dimensions for the App in pixels.
        self.width, self.height = width, height
        palette_height = 22
        # Padding stuff: xsize, ysize is the cell size in pixels (without pad).
        npad = n + 1
        self.pad = pad
        xsize = (width - npad * pad) / n
        ysize = (height - npad * pad) / n
        # Canvas dimensions for the cell grid and the palette.
        c_width, c_height = width, height
        p_pad = 2
        p_width = p_height = palette_height - 2 * p_pad

        # The main frame onto which we draw the App's elements.
        frame = Frame(master)
        frame.pack()

        # The palette for selecting colours.
        self.palette_canvas = Canvas(master, width=c_width,
                                     height=palette_height)
        self.palette_canvas.pack()

        # Add the colour selection rectangles to the palette canvas.
        self.palette_rects = []
        for i in range(self.ncolours):
            x, y = p_pad * (i + 1) + i * p_width, p_pad

            rect = self.palette_canvas.create_rectangle(x, y,
                                                        x + p_width, y + p_height, fill=self.colours[i])
            self.palette_rects.append(rect)
        # ics is the index of the currently selected colour.
        self.ics = 0
        self.select_colour(self.ics)

        # The canvas onto which the grid is drawn.
        self.w = Canvas(master, width=c_width, height=c_height)
        self.w.pack()

        # Add the cell rectangles to the grid canvas.
        self.cells = []
        for iy in range(n):
            for ix in range(n):
                xpad, ypad = pad * (ix + 1), pad * (iy + 1)
                x, y = xpad + ix * xsize, ypad + iy * ysize
                rect = self.w.create_rectangle(x, y, x + xsize,
                                               y + ysize, fill=UNFILLED)
                self.cells.append(rect)

        # Load and save image buttons
        b_load = Button(frame, text='play', command=self.play_game)
        b_load.pack(side=RIGHT, padx=pad, pady=pad)
        # Add a button to clear the grid
        b_clear = Button(frame, text='clear', command=self.clear_grid)
        b_clear.pack(side=LEFT, padx=pad, pady=pad)

        def palette_click_callback(event):
            """Function called when someone clicks on the palette canvas."""
            x, y = event.x, event.y

            # Did the user click a colour from the palette?
            if p_pad < y < p_height + p_pad:
                # Index of the selected palette rectangle (plus padding)
                ic = x // (p_width + p_pad)
                # x-position with respect to the palette rectangle left edge
                xp = x - ic * (p_width + p_pad) - p_pad
                # Is the index valid and the click within the rectangle?
                if ic < self.ncolours and 0 < xp < p_width:
                    self.select_colour(ic)

        # Bind the palette click callback function to the left mouse button
        # press event on the palette canvas.
        self.palette_canvas.bind('<ButtonPress-1>', palette_click_callback)

        def w_click_callback(event):
            """Function called when someone clicks on the grid canvas."""
            x, y = event.x, event.y

            # Did the user click a cell in the grid?
            # Indexes into the grid of cells (including padding)
            ix = int(x // (xsize + pad))
            iy = int(y // (ysize + pad))
            xc = x - ix * (xsize + pad) - pad
            yc = y - iy * (ysize + pad) - pad
            if ix < n and iy < n and 0 < xc < xsize and 0 < yc < ysize:
                i = iy * n + ix
                self.w.itemconfig(self.cells[i], fill=self.colours[self.ics])

                index = i
                # placing hurdles
                if self.ics == 2 or self.ics == 4 or self.ics == 5 or self.ics == 6:
                    self.gridArray[int(index / DEFAULT_N)][int(index % DEFAULT_N)] = 2
                else:
                    self.gridArray[int(index / DEFAULT_N)][int(index % DEFAULT_N)] = self.ics

                # source
                if self.gridArray[int(index / DEFAULT_N)][int(index % DEFAULT_N)] == 1:
                    self.currentState.x = int(index % DEFAULT_N)
                    self.currentState.y = int(index / DEFAULT_N)
                    self.currentState.cost = 0
                    self.currentState.parent = None
                    self.currentState.isVisited = True
                    self.currentStateFlag = True
                    self.currentStateCount += 1
                    print("current", self.currentState.x, self.currentState.y)
                # destination
                if self.gridArray[int(index / DEFAULT_N)][int(index % DEFAULT_N)] == 9:
                    self.goalState.x = int(index % DEFAULT_N)
                    self.goalState.y = int(index / DEFAULT_N)
                    self.goalState.heuristic = 0
                    self.goalState.parent = None
                    self.goalState.cost = 0
                    self.goalStateFlag = True
                    self.goalStateCount += 1
                    print("goal", self.goalState.x, self.goalState.y)

                    # Bind the grid click callback function to the left mouse button

        # press event on the grid canvas.
        self.w.bind('<ButtonPress-1>', w_click_callback)

    def select_colour(self, i):
        """Select the colour indexed at i in the colours list."""

        self.palette_canvas.itemconfig(self.palette_rects[self.ics],
                                       outline='black', width=1)
        self.ics = i
        self.palette_canvas.itemconfig(self.palette_rects[self.ics],
                                       outline='black', width=5)

    def _get_cell_coords(self, i):
        """Get the <letter><number> coordinates of the cell indexed at i."""

        # The horizontal axis is labelled A, B, C, ... left-to-right;
        # the vertical axis is labelled 1, 2, 3, ... bottom-to-top.
        iy, ix = divmod(i, self.n)
        return '{}{}'.format(chr(ix + 65), self.n - iy)

    def clear_grid(self):
        """Reset the grid to the background "UNFILLED" colour."""

        for cell in self.cells:
            self.w.itemconfig(cell, fill=UNFILLED)

        for i in range(DEFAULT_N):
            for j in range(DEFAULT_N):
                self.gridArray[i][j] = 0

        self.currentStateFlag = False
        self.goalStateFlag = False
        self.currentStateCount = 0
        self.goalStateCount = 0

    def play_game(self):

        if self.currentStateFlag and self.goalStateFlag:
            if self.currentStateCount > 1 or self.goalStateCount > 1:
                print("Source and Destination should be 1. Press clear to reset")
            else:

                self.currentState.heuristic = A_Star_methods.calculateHeuristic(self.currentState, self.goalState)

                GoalFound = A_Star_Search.Algorithm(self.currentState, self.goalState, self.gridArray)

                if GoalFound is None:
                    print("Ops Path Not found")

                while GoalFound is not None:
                    # print("x: ", GoalFound.x, " - y: ", GoalFound.y)
                    self.gridArray[GoalFound.y][GoalFound.x] = 8
                    GoalFound = GoalFound.parent

                for i in range(DEFAULT_N):
                    for j in range(DEFAULT_N):
                        index = (i * DEFAULT_N + j)
                        if ALREADY_EXPLORED <= self.gridArray[i][j] <= MAXEXPLORED + 1:
                            colr = 3
                        else:
                            colr = self.gridArray[i][j]

                        self.w.itemconfig(self.cells[index], fill=self.colours[colr])
        else:
            print("Start or Goal state not defined")

    # def updatePath(self):
    #     for i in range(DEFAULT_N):
    #         for j in range(DEFAULT_N):
    #             index = (i * DEFAULT_N + j)
    #             colr = self.gridArray[i][j]
    #             self.w.itemconfig(self.cells[index], fill=self.colours[7])
    #             self.w.after(1000, self.updatePath)


# Get the grid size from the command line, if provided
try:
    n = int(sys.argv[1])
except IndexError:
    n = DEFAULT_N
except ValueError:
    print('Usage: {} <n>\nwhere n is the grid size.'.format(sys.argv[0]))
    sys.exit(1)
if n < 1 or n > MAX_N:
    print('Minimum n is 1, Maximum n is {}'.format(MAX_N))
    sys.exit(1)

# Set the whole thing running
root = Tk()
grid = GridApp(root, n, 700, 700, 2)
root.mainloop()
