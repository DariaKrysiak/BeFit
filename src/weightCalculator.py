class WeightCalculator:
    lowest_index = 18.5
    highest_index = 25

    def calculateBMI(self, weight, height):
        weight = float(weight)
        height = float(height)
        if weight <= 0:
            raise NameError("The weight should be higher than 0.")
        if height <= 0:
            raise NameError("The height should be higher than 0.")
        return weight/((height/100)**2)

    def calculateCorrectWeight(self, height):
        height = float(height)
        return str(round(self.highest_index * ((height/100)**2), 1)), \
               str(round(self.lowest_index * ((height/100)**2), 1))
