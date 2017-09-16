<<<<<<< HEAD
class Goal:

    def __init__(self,cost,payment,percent,name,priority):

        self.total_cost = cost
        self.name = name
        self.priority = priority
=======
from math import ceil

class Goal:
    def __init__(self,cost,payment,percent):
        self.total_cost = cost
>>>>>>> 6dcd024c0057ce899fb6b9d4e4359874af08451f
        self.cost = cost
        self.percent = percent
        self.payment = payment
        self.daily_payment = payment*percent
<<<<<<< HEAD
        self.days = self.cost / self.daily_payment

    def change_payment(self, amount):

        self.payment += amount

    def change_percent(self,amount):

        self.percent += amount

    def change_cost(self, amount):

        self.cost += amount

    def change_priority(self, priority):

        self.priority = priority

    def change_total_cost(self, amount):

        self.total_cost += amount

    def update(self):

        self.daily_payment = self.payment * self.percent
        self.days = self.cost / self.daily_payment

    def is_payment_on_track(self, payment):

        return payment >= self.cost_per_day()

    def is_payed_for(self):

        return self.cost < 0

    def get_percent(self):

=======
        self.days = ceil(self.cost / self.daily_payment)

    def change_payment(self, amount):
        self.payment += amount

    def change_percent(self,amount):
        self.percent += amount

    def change_cost(self, amount):
        self.cost += amount

    def change_total_cost(self, amount):
        self.total_cost += amount

    def update(self):
        self.daily_payment = self.payment * self.percent
        self.days = ceil(self.cost / self.daily_payment)

    def is_payment_on_track(self, payment):
        return payment >= self.cost_per_day()

    def is_payed_for(self):
        return self.cost < 0

    def get_percent(self):
>>>>>>> 6dcd024c0057ce899fb6b9d4e4359874af08451f
        return self.percent
