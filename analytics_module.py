from habit import Habit

# AnalyticsModule class handles analytics functionality related to user's habits
class AnalyticsModule:
    # Initialize AnalyticsModule with a list of habits
    def __init__(self, habits):
        self.habits = habits
    
    # Returns the list of all habits
    def list_habits(self):
        return self.habits

    # Filters habits based on their periodicity (e.g., 'daily', 'weekly')
    def filter_by_periodicity(self, periodicity):
        return [habit for habit in self.habits if habit.periodicity == periodicity]

    # Calculates the sum of all streaks across habits
    def calculate_streaks(self):
        return sum(habit.streak for habit in self.habits)
    
    # Calculates the average streak across all habits
    def average_streak(self):
        return sum(habit.streak for habit in self.habits) / len(self.habits)

    # Returns the maximum streak value among all habits
    def maximum_streak(self):
        return max(habit.streak for habit in self.habits)

    # Returns the minimum streak value among all habits
    def minimum_streak(self):
        return min(habit.streak for habit in self.habits)

    # Returns the total number of habits
    def total_habits(self):
        return len(self.habits)
