def square(val):
    return val * val


def square_matrix_simple(matrix=[]):
    return [list(map(square, row)) for row in matrix]
