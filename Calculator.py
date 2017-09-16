
class Calculator:

    def __init__(self,amount_saved,daily_savings,days_until_grad,
        income_bracket,max_money_needed,min_money_needed):

        self.amount_saved = amount_saved
        self.daily_savings = daily_savings
        self.days_until_grad = days_until_grad
        self.income_bracket = income_bracket
        self.max_money_needed = max_money_needed
        self.min_money_needed = min_money_needed

    def update_daily_savings(self,savings):

        self.daily_savings = savings

    def update_amount_saved(self, saved):

        self.amount_saved = saved

    def update_days_until_grad(self, days):

        self.days_until_grad = days

    def possible_savings(self):

        sum_daily_savings = 0
        for i in range(self.days_until_grad):
            sum_daily_savings += self.daily_savings

        return self.amount_saved + sum_daily_savings

    def money_needed(self):

        return (1-self.income_bracket) *
            (self.max_money_needed-self.min_money_needed) + self.min_money_needed

    def calculate_need_percent(self):

        return self.possible_savings()/self.money_needed()
