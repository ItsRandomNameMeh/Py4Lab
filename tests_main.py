import unittest
from main import  sh_sort,  file_write


class TestGenerate(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sh_sort([1,3,2]),[1,2,3])
        self.assertEqual(sh_sort([1, 2, 3,4,5]), [1, 2, 3,4,5])
        self.assertEqual(sh_sort([2,1]), [1,2])

    def test_write(self):
        self.assertRaises(ValueError, file_write, -33)
        self.assertRaises(TypeError, file_write, "33")
        self.assertRaises(TypeError, file_write, [123])
        self.assertRaises(TypeError, file_write, False)
