
# adopted from: Sudoku example in the PuLP documentation

from pulp import *
from pprint import pprint

# sudoku dimensions
rows = list(range(1, 10))
columns = list(range(1, 10))
numbers = list(range(1, 10))
partitions = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]


def create_model():
    """Returns a PuLP sudoku model and allocation variable"""
    model = LpProblem("SUDOKU", LpMinimize)

    # binary vector with three dimensions (X, Y, 1..9)
    allocation = LpVariable.dicts("square", (rows, columns, numbers), lowBound = 0, upBound = 1, cat = LpInteger)

    # target function
    model += 0, "Arbitrary Objective Function"

    # one number per cell:
    for x in rows:
        for y in columns:
            model += lpSum([allocation[x][y][num] for num in numbers]) == 1

    # nine numbers per row:
    for x in rows:
        model += lpSum([allocation[x][y][num] for y in columns for num in numbers]) == 9

    # nine numbers per column:
    for y in columns:
        model += lpSum([allocation[x][y][num] for x in rows for num in numbers]) == 9

    # each number once per row:
    for x in rows:
        for num in numbers:
            model += lpSum([allocation[x][y][num] for y in columns]) == 1

    # each number once per column:
    for y in columns:
        for num in numbers:
            model += lpSum([allocation[x][y][num] for x in rows]) == 1

    # each number once per square:
    for sq_x in partitions:
        for sq_y in partitions:
            for num in numbers:
                model += lpSum([allocation[x][y][num] for x in sq_x for y in sq_y]) == 1

    return model, allocation

def add_preset_numbers(model, allocation, constraints):
    """Set predefined numbers in the sudoku"""
    for x, y, num in constraints:
        model += allocation[x][y][num] == 1
    return model


def get_solution(allocation):
    solution = []
    for y in columns:
        row = []
        for x in rows:
            cell = []
            for num in numbers:
                v = value(allocation[x][y][num])
                if v:
                    cell.append(num)
            if len(cell) == 1:
                row.append(cell[0])
            elif len(cell) == 0:
                row.append('-')
            else:
                row.append(tuple(cell))
        solution.append(row)

    return solution


def get_cell(x, y, positions):
    result = ' - '
    for xx, yy, num in positions:
        if xx == x and yy == y:
            result = ' {} '.format(num)
    return result


def get_row(y, data):
    return '|{}{}{}|{}{}{}|{}{}{}|\n'.format(
        get_cell(1, y, data), get_cell(2, y, data), get_cell(3, y, data),
        get_cell(4, y, data), get_cell(5, y, data), get_cell(6, y, data),
        get_cell(7, y, data), get_cell(8, y, data), get_cell(9, y, data),
        )

def draw_sudoku(data):
    s = '-' * 31 + '\n'
    s += get_row(1, data) + get_row(2, data) + get_row(3, data)
    s += '-' * 31 + '\n'
    s += get_row(4, data) + get_row(5, data) + get_row(6, data)
    s += '-' * 31 + '\n'
    s += get_row(7, data) + get_row(8, data) + get_row(9, data)
    s += '-' * 31 + '\n'
    return(s)


def solve_sudoku(constraints):
    """
    Solves a Sudoku as a linear equation system.
    Returns a feasibility, solution tuple.
    """
    model, allocation = create_model()
    model = add_preset_numbers(model, allocation, constraints)
    model.solve()
    status = LpStatus[model.status]
    solution = get_solution(allocation)
    return status, solution


if __name__ == '__main__':
    constraints = []
    status, solution = solve_sudoku(constraints)
    pprint(solution)
    print("\nStatus:", status)

