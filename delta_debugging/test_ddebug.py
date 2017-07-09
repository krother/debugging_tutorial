
from unittest import TestCase, main
from ddebug import get_partitions, delta_debug
from run_ddebug import test_sudoku
from sudoku import draw_sudoku
import random as r


class PartitionTests(TestCase):

    def test_get_partitions(self):
        data = "ABCDEFG"
        result = list(get_partitions(data, 2))
        result.sort()
        self.assertEqual(result, ["ABC", "DEFG"])
        result = list(get_partitions(data, 3))
        self.assertEqual(result, ["CDEFG", "ABEFG", "ABCD"])
        result = list(get_partitions(data, 4))
        self.assertEqual(result, ["BCDEFG", "ADEFG", "ABCFG", "ABCDE"])


class DeltaDebugTests(TestCase):

    def test_ddebug_nofail(self):
        constraints = [(1,1,1)]
        self.assertRaises(AssertionError, delta_debug, constraints, test_sudoku)

    def test_ddebug_sudoku(self):
        constraints = [(1,1,9), (1,2,3), (8,8,7), (2,2,9)]
        minimal = delta_debug(constraints, test_sudoku)
        self.assertEqual(minimal, [(1,1,9), (2,2,9)]) 

    def test_ddebug_sudoku_duplicate_pos(self):
        constraints = [(1,1,9), (1,1,8), (8,8,7), (2,2,5)]
        minimal = delta_debug(constraints, test_sudoku)
        self.assertEqual(minimal, [(1,1,9), (1,1,8)]) 

    def test_ddebug_sudoku_complex(self):
        constraints = [(1,1,1), (2,1,2), (3,1,3), (4,2,1), (5,2,2), (6,2,3), (7,3,7), (8,3,8), (9,3,9)]
        minimal = delta_debug(constraints, test_sudoku)


class RandomDeltaDebugTests(TestCase):

    def create_random_constraints(self):
        constraints = []
        for i in range(r.randint(1, 80)):
            x = r.randint(1, 9)
            y = r.randint(1, 9)
            n = r.randint(1, 9)
            constraints.append((x, y, n))
        return constraints


    def test_ddebug_sudoku_random(self):
        for i in range(10):
            constraints = self.create_random_constraints()
            if test_sudoku(constraints) == 'FAIL':
                print("run #", i)
                print(i, "#constraints:", len(constraints))
                minimal = delta_debug(constraints, test_sudoku)
                print(draw_sudoku(constraints))
                print(draw_sudoku(minimal))
                print(minimal)


if __name__ == '__main__':
    main()
