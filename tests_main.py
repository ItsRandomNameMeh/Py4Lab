import unittest
from main import  sh_sort,  file_write


class TestGenerate(unittest.TestCase):
    def setUp(self):
        #
        self.first_case_test = [1, 3, 2]
        self.second_case_test = [1,2,3,4,5]
        self.third_case_test = [2,1]
        self.assertEqual(sh_sort(self.first_case_test),[1, 2, 3])
        self.assertEqual(sh_sort(self.second_case_test), [1, 2, 3, 4, 5])
        self.assertEqual(sh_sort(self.third_case_test), [1, 2])
        #
        self.int_error = -33
        self.string_error = "33"
        self.array_error = [123]
        self.bool_error = False
        self.assertRaises(ValueError, file_write, self.int_error)
        self.assertRaises(TypeError, file_write, self.string_error)
        self.assertRaises(TypeError, file_write, self.array_error)
        self.assertRaises(TypeError, file_write, self.bool_error)