from Goal import *

def get_percent(goal):

    return goal.get_percent()

class GoalList:

    def __init__(self, goal_list, goal_list_percent):


        self.goal_list = goal_list # this is a list
        self.goal_list_percent = goal_list_percent

    def append(self,goal):

        self.goal_list.append(goal)

        self.update()

    def set_indices(self):

        for i in range(len(self.goal_list)):

            self.goal_list[i].i = i

    def make_payment(self,amount):

        for i in range(len(self.goal_list)):
            percent = self.goal_list[i].get_percent()
            self.goal_list[i].change_cost(amount * goal_list_percent * percent)

    def remove(self,index):

        del self.goal_list[index]

        self.update()

    def get_list(self):

        return self.goal_list

    def update(self):

        priority_sum = 0
        for i in range(len(self.goal_list)):
            priority_sum += self.goal_list[i].get_priority()

        for i in range(len(self.goal_list)):
            self.goal_list[i].payment *= self.goal_list_percent
            self.goal_list[i].percent = self.goal_list[i].get_priority() / priority_sum

        self.goal_list.sort(key=get_percent, reverse=True)

    def get_tooltip(self):

        for i in range(len(self.goal_list)):

            if self.goal_list[i].get_days() >= 730:

                return_string = 'Your goal for ' + self.goal_list[i].get_name()
                return_string += ' may take too long to complete. You should consider '
                return_string += 'that your circumstances and desires might change '
                return_string += 'before you have achieved your goal.'

                return return_string

        if len(self.goal_list) > 3:

            return_string = 'You may have too many goals! Consider that saving '
            return_string += 'for too many things at once could be slow and '
            return_string += 'an inefficient use of your money. Consider deleting some '
            return_string += 'goals and re-adding them later.'

            return return_string
