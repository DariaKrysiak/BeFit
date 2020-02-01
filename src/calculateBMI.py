class CalculateBMI:
    lowest_index = 18.5
    highest_index = 24.9

    def calculateBMI(self, weight, height):
        return float(weight)/((float(height)/100)**2)

    def findCorrectWeigth(self, height):
        return str(round(self.highest_index * ((float(height)/100)**2), 1)), \
               str(round(self.lowest_index * ((float(height)/100)**2), 1))
