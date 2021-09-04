from random import randrange, randint, choice
from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib import colors

total_states = 13  # total number of different colors that represent different states of cells
generations = 150
width = 151
height = 151

reds = ['black', 'grey', 'silver', 'gainsboro', 'indianred', 'firebrick', 'maroon', 'sienna',
        'saddlebrown', 'tomato', 'peru', 'red', 'coral']
greens = ['black', 'forestgreen', 'dimgray', 'gray', 'darkgrey', 'silver', 'gainsboro',
          'darkgreen', 'green', 'seagreen', 'darkslategrey', 'darkgray', 'slategray']
yellows = ['white', 'snow', 'mistyrose', 'seashell', 'peachpuff', 'linen', 'bisque', 'wheat',
           'moccasin', 'gold', 'khaki', 'navajowhite', 'beige']
blacks = ['white', 'black', 'dimgrey', 'dimgray', 'gray', 'grey', 'darkgrey', 'darkgray', 'silver',
          'lightgray', 'lightgrey', 'gainsboro', 'whitesmoke']


def visualize(final_matrix, generation):
    cmap = colors.ListedColormap(blacks)
    # cmap = colors.ListedColormap(['white', 'black'])              # for rule 942
    bounds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # bounds = [0, 1]                                               # for rule 942
    norm = colors.BoundaryNorm(bounds, cmap.N)

    plt.axis('off')
    plt.imshow(final_matrix, interpolation='nearest', origin='lower', cmap=cmap, norm=norm)
    plt.savefig('ca_cells_' + str(width) + '_gen_' + str(generation) + '_of_' + str(generations) + '.png')
    plt.show()
    return 1


def ca_stepping_stone_vonneumann_neighborhood(matrix):      # change state of cell to the state of a random neighbor
    for generation in range(0, generations):                # neighbors are only 4 pixels = top, bottom, left and right
        new_matrix = deepcopy(matrix)

        for row in range(0, height):
            for column in range(0, width):
                if randint(0, 1) == 1:                      # toss a coin to decide if the current cell changes state
                    rand_neighbor = choice(['top', 'bottom', 'left', 'right'])

                    if rand_neighbor == 'top' and row != 0:
                        new_matrix[row][column] = matrix[row - 1][column]

                    elif rand_neighbor == 'bottom' and row != height - 1:
                        new_matrix[row][column] = matrix[row + 1][column]

                    elif rand_neighbor == 'left' and column != 0:
                        new_matrix[row][column] = matrix[row][column - 1]

                    elif rand_neighbor == 'right' and column != width - 1:
                        new_matrix[row][column] = matrix[row][column + 1]

                    else:
                        new_matrix[row][column] = matrix[row][column]

        matrix = deepcopy(new_matrix)
        visualize(new_matrix, generation + 1)


def ca_rule_942(matrix):        # change cell to black if one or all neighbors are black
    for generation in range(0, generations):
        new_matrix = deepcopy(matrix)

        for row in range(0, height):
            for column in range(0, width):
                black_neighbors = 0
                total_neighbors_count = 4

                if (row == 0 and column == 0) or (row == height - 1 and column == width - 1):
                    total_neighbors_count -= 2

                if (row == 0 and (0 < column < width - 1)) or (column == 0 and (0 < row < height - 1)):
                    total_neighbors_count -= 1

                if row != 0 and matrix[row - 1][column] == 1:
                    black_neighbors += 1

                if row != height - 1 and matrix[row + 1][column] == 1:
                    black_neighbors += 1

                if column != 0 and matrix[row][column - 1] == 1:
                    black_neighbors += 1

                if column != width - 1 and matrix[row][column + 1] == 1:
                    black_neighbors += 1

                if black_neighbors == 1 or black_neighbors == total_neighbors_count:
                    new_matrix[row][column] = 1

        matrix = deepcopy(new_matrix)
        visualize(new_matrix, generation + 1)


def ca_cyclic(matrix):          # increment cell's state by 1 if at least one neighboring cell has a state difference +1
    for generation in range(0, generations):
        new_matrix = deepcopy(matrix)

        for row in range(0, height):  # change cell to black if one or all neighbors are black
            for column in range(0, width):
                next_state = (matrix[row][column] + 1) % total_states

                if (row != 0 and matrix[row - 1][column] == next_state) or \
                        (row != height - 1 and matrix[row + 1][column] == next_state) or \
                        (column != 0 and matrix[row][column - 1] == next_state) or \
                        (column != width - 1 and matrix[row][column + 1] == next_state):
                    new_matrix[row][column] = next_state

        matrix = deepcopy(new_matrix)
        visualize(new_matrix, generation + 1)


def main():
    matrix = []

    for i in range(0, width):  # initializing a randomized matrix of cells in different states/colors
        new_row = []

        for j in range(0, height):
            new_row.append(randrange(0, total_states))
            # new_row.append(0)                                                         # for rule 942

        matrix.append(new_row)
    # matrix[int(width/2)][int(height/2)] = 1                                           # for rule 942

    # ca_stepping_stone_vonneumann_neighborhood(matrix)
    # ca_rule_942(matrix)
    ca_cyclic(matrix)


main()
