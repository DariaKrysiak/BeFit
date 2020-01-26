class CalculateBMI():
    weight = 0
    height = 0
    lowest_index = 18.5
    highest_index = 24.9

    def __init__(self):
        self.getWeightFromUser()
        self.getHeightFromUser()
        self.calculateBMI()
        self.findCorrectWeigth()

    def getWeightFromUser(self):
        self.weight = float(input("Podaj swoją wagę w kilogramach: ").replace(',', '.'))

    def getHeightFromUser(self):
        self.height = float(input("Podaj swój wzrost w metrach: ").replace(',', '.'))

    def calculateBMI(self):
        bmi = self.weight/(self.height**2)
        if self.lowest_index < bmi < self.highest_index:
            print("waga prawidłowa")
        elif bmi <= self.lowest_index:
            print("niedowaga")
        else:
            print("nadwaga")

    def findCorrectWeigth(self):
        highest_correct_weight = str(round(self.highest_index * (self.height**2), 1))
        lowest_correct_weight = str(round(self.lowest_index * (self.height**2), 1))
        print("Twoja waga powinna mieścić się w granicach od " + lowest_correct_weight + " kg do "
              + highest_correct_weight + " kg.")