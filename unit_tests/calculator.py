import pandas as pd

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a +self.b
    
    def get_diff(self):
        return self.a - self.b
    
    def get_product(self):
        return self.a * self.b
    
    def get_quotient(self):
        return self.a / self.b
    
    def print_times_table(self, number=3, limit=10):
        data = {
            "Multiplier": list(range(1, limit + 1)),
            "Result": [number * i for i in range(1, limit + 1)]
        }
        df = pd.DataFrame(data)
        print(f"\n{number} Times Table:")
        print(df)

    
if __name__ == '__main__':
    myCalc = Calculator(a=934, b=35)

    answer1 = myCalc.get_sum()
    answer2 = myCalc.get_diff()
    answer3 = myCalc.get_product()
    answer4 = myCalc.get_quotient()

    #print(answer1, answer2, answer3, answer4)

    # Print 3 times table
    myCalc.print_times_table()