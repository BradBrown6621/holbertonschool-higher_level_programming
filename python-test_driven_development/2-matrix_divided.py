

def matrix_divided(matrix, div):
    """Function for matrix division"""
    typeerror = "matrix must be a matrix (list of lists) of integers/floats"
    elementsize = "Each row of the matrix must have the same size"
    new_matrix = matrix
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix:
        length = len(new_matrix[0])
        for row in range(0, len(matrix)):
            if isinstance(matrix[row], list):
                if len(matrix[row]) == length:
                    for col in range(0, len(matrix[row])):
                        element = new_matrix[row][col]
                        if isinstance(element, (float, int)):
                            element = round(element / div, 2)
                            new_matrix[row][col] = element
                        else:
                            raise TypeError(typeerror)
                else:
                    raise TypeError(elementsize)
            else:
                raise TypeError(typeerror)
        return new_matrix
    else:
        raise TypeError(typeerror)
