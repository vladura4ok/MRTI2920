class Calculator:
    def calculate(self, a, b):
        return a

class SumCalc(Calculator):
    def calculate(self, a, b):
        return a+b

class DivCalc(Calculator):
    def calculate(self, a, b):
        # if b == 0:
        #     return 0
        return a/b

base_calc = Calculator()
sum_calc = SumCalc()
div_calc = DivCalc()

calcs = [base_calc, sum_calc, div_calc]

for calc in calcs:
    print(calc.calculate(2, 0))

