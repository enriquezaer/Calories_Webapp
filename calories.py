from temperature import Temperature


class Calories:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature.get() * 10
        return result

    def get_kj(self):
        kcal = self.calculate()
        return kcal * 4.184

    def kj_to_file(self):
        file_path = "calories.txt"
        with open(file_path, 'w') as file: file.write(self.get_kj())


if __name__ == "__main__":
    # temperature_ = Temperature(country="honduras", location="tegucigalpa")
    # calories = Calories(weight=70, height=127, age=41, temperature=temperature_)
    # print(calories.calculate())
    calorie = Calories(175, 70, 33, 30)
    calories = calorie.kj_to_file()
