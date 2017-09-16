from goal_object import *

def get_percent(goal):

    return goal.get_percent()

class GoalList:

    def __init__(self, goal_list):

<<<<<<< HEAD
        self.goal_list = goal_list
=======
        self.goal_list = goal_list # this is a list
>>>>>>> 6dcd024c0057ce899fb6b9d4e4359874af08451f
        self.goal_list.sort(key=get_percent, reverse=True)

    def append(self,goal):

        self.goal_list.append(goal)
        self.goal_list.sort(key=get_percent, reverse=True)

    def remove(self,index):

        del self.goal_list[index]

    def get_list(self):

        return self.goal_list
