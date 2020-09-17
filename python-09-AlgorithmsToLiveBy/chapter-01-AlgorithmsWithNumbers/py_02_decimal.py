"""
decimal system

memorization
- sum of 3 digitals is less than two digital.
- decimal: 999, 9 + 9 + 9 = 27

each single digital addition is less than overflow? 


! what?
decimal system
it is everywhere in ordinary life

! why?
i have no f*cking idea

! how?
decimal system
|-- basic arithmetic   
|-- modular arithmetic
|-- primality testing
|-- cryptography
|-- uinversal hashing



"""

from unittest import mock
import unittest

class MyDecimal:
    def __init__(self, number: int):
        _uid = '.'
        if _uid in str(number):
            raise ValueError('number must be integer')
        else:
            self.number = number

    def sum_any_three_single_digit_numbers(self):
        """P21, basic property of decimal numbers is
        the sum of any three single-digit numbers is at most two digits long.
        """
        _uid = '-'
        _strNum = str(self.number)
        if _uid in _strNum:
            return sum([int(i) for i in _strNum[1:]])
        else:
            return sum([int(i) for i in _strNum])

    def multiplication(self):
        pass

class TestMyDecimal(unittest.TestCase):
    def test_method_negative_integers(self):
        md = MyDecimal(-190)
        self.assertEqual(10, md.sum_any_three_single_digit_numbers())
    def test_method_positive_integers(self):
        md = MyDecimal(999)
        self.assertEqual(27, md.sum_any_three_single_digit_numbers())
    @unittest.skip
    def test_method_float(self):
        md = MyDecimal(10.4)
        self.assertRaises(ValueError, md.sum_any_three_single_digit_numbers())
    @mock.patch('__main__.MyDecimal', autospec=True)
    def test_init(self, mock_init):
        _ = MyDecimal(10.4)
        mock_init.assert_called_with(10.4)



if __name__ == "__main__":
    unittest.main()
