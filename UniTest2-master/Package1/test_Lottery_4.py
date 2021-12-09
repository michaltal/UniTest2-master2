from unittest import TestCase
from Package1.Lottery import Lottery


class TestLottery(TestCase):

    def setUp(self):
        print('setUp')
        self.lottery = Lottery()

    def tearDown(self):
        print("tearDown")

    def test_rand_numbers(self):
        lotteryTest1 = Lottery()
        lotteryTest1.rand_numbers()
        res = self.lottery.rand_numbers()
        self.assertTrue(self.lottery.rand_numbers())

    def test_valid_numbers(self):
        assert False


    def test_valid_range(self):
        assert False


