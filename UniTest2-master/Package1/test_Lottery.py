from unittest import TestCase, mock
from unittest.mock import patch
from Package1.Lottery import Lottery


class TestLottery(TestCase):

    def setUp(self):
        print('setUp')
        self.lottery = Lottery()

    def tearDown(self):
        print('tearDown')

    def test_rand_numbers(self):
        self.assertTrue(self.lottery.rand_numbers())
        self.assertTrue(len(self.lottery.rand_numbers()) != 0)
        # self.assertIn('3', self.lottery.rand_numbers())

    # using mock as a decorator
    @mock.patch('Package1.Lottery.Lottery.rand_numbers', return_value=[10, 31, 11, 20, 67, 20])
    def test_valid_numbers_False(self, mock_rand_numbers):
        # Tests a case in which a number is duplicated
        self.assertFalse(self.lottery.valid_numbers())
        print(self.lottery.numbers)

    @mock.patch('Package1.Lottery.Lottery.rand_numbers', return_value=[10, 31, 11, 20, 67, 21])
    def test_valid_numbers_True(self, mock_rand_numbers):
        # Tests a case in which all numbers are unique
        self.assertTrue(self.lottery.valid_numbers())
        print(self.lottery.numbers)

    def test_valid_range_out_of_range(self):
        # using mock as a context manager
        with patch('Package1.Lottery.Lottery.rand_numbers') as mock_rand_num:
            mock_rand_num.return_value = [0, 31, 11, 12, 12, 20]
            print("out of range values", mock_rand_num.return_value)
            self.assertFalse(self.lottery.valid_range())
            mock_rand_num.return_value = [46, 31, 11, 12, 12, 20]
            print("out of range values", mock_rand_num.return_value)
            self.assertFalse(self.lottery.valid_range())

    def test_valid_range_in_range(self):
        # using mock as a context manager
        with patch('Package1.Lottery.Lottery.rand_numbers') as mock_rand_num:
            mock_rand_num.return_value = [1, 31, 11, 12, 45, 20]
            print("in range values", mock_rand_num.return_value)
            self.assertTrue(self.lottery.valid_range())
