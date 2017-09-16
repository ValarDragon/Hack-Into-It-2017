from Goal import *

def get_percent(goal):

    return goal.get_percent()

class GoalList:

    def __init__(self, goal_list, goal_list_percent):


        self.goal_list = goal_list # this is a list
        self.goal_list_percent = goal_list_percent
        self.goal_list.sort(key=get_percent, reverse=True)

    def append(self,goal):

        self.goal_list.append(goal)
        self.goal_list.sort(key=get_percent, reverse=True)

        self.update_percents()

    def set_indices(self):

        for i in range(len(self.goal_list)):

            self.goal_list[i].i = i

    def remove(self,index):

        del self.goal_list[index]

        self.update_percents()

    def get_list(self):

        return self.goal_list

    def update_percents(self):

        priority_sum = 0
        for i in range(len(self.goal_list)):
            priority_sum += self.goal_list[i].get_priority()

        for i in range(len(self.goal_list)):
            self.goal_list[i].payment *= self.goal_list_percent
            self.goal_list[i].percent = self.goal_list[i].get_priority() / [priority_sum]
