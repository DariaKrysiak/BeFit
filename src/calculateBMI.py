class CalculateBMI:
    lowest_index = 18.5
    highest_index = 24.9

    def calculateBMI(self, weight, height):
        bmi = float(weight)/(float(height)**2)
        if self.lowest_index < bmi < self.highest_index:
            print("waga prawidłowa")
        elif bmi <= self.lowest_index:
            print("niedowaga")
        else:
            print("nadwaga")

    def findCorrectWeigth(self, height):
        highest_correct_weight = str(round(self.highest_index * (float(height)**2), 1))
        lowest_correct_weight = str(round(self.lowest_index * (float(height)**2), 1))
        print("Twoja waga powinna mieścić się w granicach od " + lowest_correct_weight + " kg do "
              + highest_correct_weight + " kg.")