import unittest
import random
from sorting2 import *

class RecursiveSortingTests(unittest.TestCase):
    def test_in_place_merge_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [2]
        arr4 = [0, 1, 2, 3, 4, 5]
        arr5 = random.sample(range(200), 50)
        arr5_copy = [x for x in arr5]

        merge_sort_in_place(arr1)
        self.assertEqual(arr1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        merge_sort_in_place(arr2)
        self.assertEqual(arr2, [])
        
        merge_sort_in_place(arr3)
        self.assertEqual(arr3, [2])

        merge_sort_in_place(arr4)
        self.assertEqual(arr4, [0, 1, 2, 3, 4, 5])

        merge_sort_in_place(arr5)
        self.assertEqual(arr5, sorted(arr5_copy))


if __name__ == '__main__':
    unittest.main()