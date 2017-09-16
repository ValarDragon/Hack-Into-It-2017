from math import ceil

class Goal:
    def __init__(self,cost,payment,percent):
        self.total_cost = cost
        self.cost = cost
        self.percent = percent
        self.payment = payment
        self.daily_payment = payment*percent
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
        return self.percent
