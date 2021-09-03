from random import randrange, randint, choice
from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib import colors

total_states = 13  # total number of different colors that represent different states of cells
generations = 20
width = 50
height = 50

reds = ['black', 'grey', 'silver', 'gainsboro', 'indianred', 'firebrick', 'maroon', 'sienna',
        'saddlebrown', 'tomato', 'peru', 'red', 'coral']
greens = ['black', 'forestgreen', 'dimgray', 'gray', 'darkgrey', 'silver', 'gainsboro',
          'darkgreen', 'green', 'seagreen', 'darkslategrey', 'darkgray', 'slategray']
yellows = ['white', 'snow', 'mistyrose', 'seashell', 'peachpuff', 'linen', 'bisque', 'wheat',
           'moccasin', 'gold', 'khaki', 'navajowhite', 'beige']


def visualize(final_matrix, generation):
    cmap = colors.ListedColormap(reds)
    bounds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    plt.imshow(final_matrix, interpolation='nearest', origin='lower', cmap=cmap, norm=norm)
    plt.savefig('cells_' + str(width) + '_gen_' + str(generation) + '.png')
    plt.show()
    return 1


def ca_stepping_stone_vonneumann_neighborhood(matrix):       # neighbors are only 4 pixels = top, bottom, left and right
    for generation in range(0, generations):
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


def main():
    matrix = []

    for i in range(0, width):  # initializing a randomized matrix of cells in different states/colors
        new_row = []

        for j in range(0, height):
            new_row.append(randrange(0, total_states))

        matrix.append(new_row)

    ca_stepping_stone_vonneumann_neighborhood(matrix)


main()


def ca_cyclic():
    return 1
