class Money():    
    def __init__(self, amount_rub, amount_cop):
        self.amount_rub = amount_rub
        while amount_cop > 99:
            self.amount_rub += 1
            amount_cop -= 100
        self.amount_cop = amount_cop
    
    def __str__ (self):
        return f'{self.amount_rub}руб {self.amount_cop}коп'
    
    def __add__(self, other_rub):
        self.amount_cop += other_rub.amount_cop
        while self.amount_cop > 99:
            self.amount_rub += 1
            self.amount_cop -= 100
        out_rub = self.amount_rub + other_rub.amount_rub
        out_cop = self.amount_cop
        return Money(out_rub, out_cop)
    
    def __sub__(self, other_rub):
        while self.amount_cop - other_rub.amount_cop < 0:
            self.amount_rub -= 1
            self.amount_cop += 100
        out_rub = self.amount_rub - other_rub.amount_rub
        out_cop = self.amount_cop
        return Money(out_rub, out_cop)
    
    def __mul__(self, multiple_int):
        self.amount_rub *= multiple_int
        self.amount_cop *= multiple_int
        while self.amount_cop > 99:
            self.amount_rub += 1
            self.amount_cop -= 100
        out_rub = self.amount_rub
        out_cop = self.amount_cop
        return Money(out_rub, out_cop)
    
    def __lt__(self, other) - x < y вызывает x.__lt__(y).

    def __le__(self, other) - x ≤ y вызывает x.__le__(y).

    def __eq__(self, other) - x == y вызывает x.__eq__(y).

    def __ne__(self, other) - x != y вызывает x.__ne__(y)

    def __gt__(self, other) - x > y вызывает x.__gt__(y).

    def __ge__(self, other) - x ≥ y вызывает x.__ge__(y).


money_sum1 = Money(20, 70)
money_sum2 = Money(10, 70)

print(money_sum1)


money_result = money_sum1 - money_sum2
print(money_result)
money_result1 = money_sum1 + money_sum2
print(money_result1)

