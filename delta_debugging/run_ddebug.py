
from ddebug import delta_debug
from sudoku import draw_sudoku, solve_sudoku


def test_sudoku(constraints):
    try:
        status, solution = solve_sudoku(constraints)
        return "PASS" if status == 'Optimal' else "FAIL"
    except:
        return "FAIL"


if __name__ == '__main__':
    constraints = [(1,1,9), (1,2,3), (8,8,7), (2,2,9)]
    #constraints = [(1,1,9), (1,2,3), (8,8,7), (4,2,9), (2,2,9)]
    #constraints = [(1,1,1), (2,1,2), (3,1,3), (4,2,1), (5,2,2), (6,2,3), (7,3,7), (8,3,8), (9,3,9)]
    minimal = delta_debug(constraints, test_sudoku)
    print(draw_sudoku(constraints))
    print('minimal failing subset:')
    print(draw_sudoku(minimal))
