from src import calculateBMI


class Controller:

    def __init__(self):
        weight = self.getWeightFromUser()
        height = self.getHeightFromUser()
        calculator = calculateBMI.CalculateBMI()
        calculator.calculateBMI(weight, height)
        calculator.findCorrectWeigth(height)

    def getWeightFromUser(self):
        return input("Podaj swoją wagę w kilogramach: ").replace(',', '.')

    def getHeightFromUser(self):
        return input("Podaj swój wzrost w metrach: ").replace(',', '.')
