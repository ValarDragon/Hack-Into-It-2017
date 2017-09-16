from math import ceil
from Calculator import *

class Goal:
    def __init__(self,cost,payment,percent,name,priority,i = None):

        """Remember to call goalList update_percents to
        initialize the percents and the correct
        payment value"""

        self.i = i
        self.name = name
        self.priority = priority
        self.total_cost = cost
        self.cost = cost
        self.percent = percent
        self.payment = payment
        self.daily_payment = payment*percent
        self.days = self.cost / self.daily_payment

    def change_payment(self, amount):

        self.payment += amount

        self.update()

    def get_name(self):

        return self.name

    def change_name(self, name):

        self.name = name

    def change_percent(self,amount):

        self.percent += amount

        self.update()

    def change_cost(self, amount):

        self.cost += amount

        self.update()

    def get_days(self):

        return self.days

    def get_priority(self):

        return self.priority

    def change_priority(self, priority):
        """IF YOU CHANGE priority
        PLEASE CALL GOALLIST.update_percents"""
        self.priority = priority

        self.update()

    def change_total_cost(self, amount):

        self.total_cost += amount

        self.update()

    def update(self):

        self.daily_payment = self.payment * self.percent
        self.days = self.cost / self.daily_payment

    def is_payment_on_track(self, payment):

        return payment >= self.cost_per_day()

    def is_payed_for(self):

        return self.cost < 0

    def get_percent(self):

        return self.percent
