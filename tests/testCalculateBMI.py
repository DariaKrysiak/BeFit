import unittest
from src import weightCalculator


class TestCalculateBMI(unittest.TestCase):

    calculator = weightCalculator.WeightCalculator()
    correct_weight = 55
    correct_height = 155
    correct_bmi = 22.89

    def calculateTestBMI(self):
        return round(self.calculator.calculateBMI(self.correct_weight, self.correct_height), 2)

    def test_calculateBMICorrectValue(self):
        self.assertEqual(self.calculateTestBMI(), self.correct_bmi)

    def test_calculateBMINegativeWeight(self):
        self.correct_weight = -55
        with self.assertRaises(NameError):
            self.calculateTestBMI()

    def test_calculateBMINegativeHeight(self):
        self.correct_height = -155
        with self.assertRaises(NameError):
            self.calculateTestBMI()

    def test_calculateBMIWrongTypeWeight(self):
        self.correct_weight = 'dd'
        with self.assertRaises(ValueError):
            self.calculateTestBMI()

    def test_calculateBMIWrongTypeHeight(self):
        self.correct_height = 'dd'
        with self.assertRaises(ValueError):
            self.calculateTestBMI()
