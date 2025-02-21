import unittest


def pascal_triangle(times) -> list:
    result_x = []
    for x in range(1, times+1):
        result_y = []
        for y in range(x):
            result_y.append(x)


        result_x.append(result_y)

    return result_x









class MyNewCase(unittest.TestCase):
    def test_something(self):
        actual = pascal_triangle(5)
        expected = [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
        self.assertEqual(expected, actual)


