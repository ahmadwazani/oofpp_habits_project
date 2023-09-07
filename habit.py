# The Habit class represents a user's habit, including task specifications and periodicity.
# The streak is set to 0 and the completed status is set to false.
class Habit:
    def __init__(self, description, periodicity, streak=0, completed=False):
        self.description = description # The description of the habit ("Exercise Daily")
        self.periodicity = periodicity # The periodicity of the habit ("daily","weekly")
        self.streak = streak # The current streak counter for completing the habit
        self.completed = completed # The status of completion of the habit

# Mark the habit as complete, the streak counter is incremented by 1
    def mark_complete(self):
        self.completed = True
        self.streak += 1

# Reset the counter for the habit back to 0
    def reset_streak(self):
        self.streak = 0

# Updates the description of the habit with a new description
    def update_description(self, new_description):
        self.description = new_description

# Updates the periodicity of the habit with a new periodicity
    def update_periodicity(self, new_periodicity):
        self.periodicity = new_periodicity
