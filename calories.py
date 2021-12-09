from temperature import Temperature


class Calories:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == "__main__":
    temperature = Temperature(country="honduras", location="tegucigalpa")
    calories = Calories(weight=70, height=127, age=41, temparature=temperature)
    print(calories.calculate())

