class WeightCalculator:
    lowest_index = 18.5
    highest_index = 25

    def calculateBMI(self, weight, height):
        return float(weight)/((float(height)/100)**2)

    def calculateCorrectWeight(self, height):
        return str(round(self.highest_index * ((float(height)/100)**2), 1)), \
               str(round(self.lowest_index * ((float(height)/100)**2), 1))
