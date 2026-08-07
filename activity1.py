class BMICalculator:

    def get_input(self):
        self.weight = float(input("Enter your weight (kg): "))
        self.height = float(input("Enter your height (m): "))

    def calculate_bmi(self):
        self.bmi = self.weight / (self.height ** 2)

    def display_result(self):
        print(f"\nYour BMI is: {self.bmi:.2f}")

        if self.bmi < 18.5:
            print("Underweight")
        elif self.bmi < 25:
            print("Normal weight")
        elif self.bmi < 30:
            print("Overweight")
        else:
            print("Obese")


# Main Program
calculator = BMICalculator()
calculator.get_input()
calculator.calculate_bmi()
calculator.display_result()
