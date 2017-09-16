from Calculator import *
from GoalList import *
from Goal import *

class Manager:

    def __init__(self,daily_savings,
        days_until_grad, income_bracket,amount_saved =0):

        self.User = Calculator(amount_saved,daily_savings
            days_until_grad, income_bracket)

        self.NeedList = GoalList([],
            self.User.calculate_need_percent())

        self.WantList = GoalList([],
            1 - self.User.calculate_need_percent())

    def update(self):

        self.NeedList.goal_list_percent = self.User.calculate_need_percent()
        self.WantList.goal_list_percent = 1 - self.User.calculate_need_percent()
        self.NeedList.make_payment(daily_savings)
        self.WantList.make_payment(daily_savings)
