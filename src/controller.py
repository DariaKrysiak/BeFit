from src import weightCalculator


class Controller:

    def __init__(self):
        weight = self.getWeightFromUser()
        height = self.getHeightFromUser()
        calculator = weightCalculator.WeightCalculator()
        bmi = calculator.calculateBMI(weight, height)
        self.printBodyWeightAssessment(calculator, bmi)
        highest_correct_weight, lowest_correct_weight = calculator.calculateCorrectWeight(height)
        self.printCorrectWeight(height, highest_correct_weight, lowest_correct_weight)

    def getWeightFromUser(self):
        return input("Enter your weight [in kg]: ").replace(',', '.')

    def getHeightFromUser(self):
        return input("Enter your height [in cm]: ").replace(',', '.')

    def printBodyWeightAssessment(self, calculator, bmi):
        if calculator.lowest_index <= bmi < calculator.highest_index:
            print("Normal weight")
        elif bmi < calculator.lowest_index:
            print("Underweight")
        else:
            print("Overweight")

    def printCorrectWeight(self, height, highest_correct_weight, lowest_correct_weight):
        print("Healthy weight for your height (" + height + " cm) should be between: " + str(lowest_correct_weight)
              + " and " + str(highest_correct_weight) + " kgs.")
