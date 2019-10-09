import ddt
import unittest

from fmin import fmin


@ddt.ddt
class CAPAProblemTest(unittest.TestCase):

    @ddt.unpack
    @ddt.data(
        {'array': [1]},
        {'array': [1, 2]},
        {'array': [2, 1]},
        {'array': [1, 2, 3]},
        {'array': [3, 2, 1]},
        {'array': [3, 2, 1, 2, 3]},
    )
    def test_fmin(self, array):
        result = fmin(array)
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
