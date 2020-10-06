# Conways Game of Life

import copy
import random
import time

WIDTH = 60
HEIGHT = 20

# List of list for cells
next_cells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  # Add a living cell
        else:
            column.append(' ')  # Add a dead cell
    next_cells.append(column)

while True:
    print('\n\n\n\n\n')  # Separate each step with newlines
    current_cells = copy.deepcopy(next_cells)

    # Print current_cells to the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')  # Print the # or the space
        print()  # Newline at end of row

    # Calculate the next step's cell based on the current step's cell
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            # Count the number of livin neighbors
            num_neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1  # Top neighbor alive
            if current_cells[x][above_coord] == '#':
                num_neighbors += 1  # Top-right neighbor alive
            if current_cells[left_coord][y] == '#':
                num_neighbors += 1  # Left neighbor is alive
            if current_cells[right_coord][y] == '#':
                num_neighbors += 1  # Right neighbor is alive
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1  # Bottom-left neighbor alive
            if current_cells[x][below_coord] == '#':
                num_neighbors += 1  # Bottom neighbor alive
            if current_cells[right_coord][below_coord] == '#':
                num_neighbors += 1  # Bottom-right neighbor alive

            # Set cells based on Conway's Game of Life rules:
            if current_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_neighbors == 3:
                # Dead cells with 3 neighbors become alive
                next_cells[x][y] = '#'
            else:
                # Everything else dies or stays dead
                next_cells[x][y] = ' '

    time.sleep(1)
