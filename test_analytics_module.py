from analytics_module import AnalyticsModule
from habit import Habit

# Test function for the AnalyticsModule class
def test_analytics_module():
    # Creating a list of Habit objects to be used for testing
    habits = [
        Habit(description="Read a book", periodicity="daily"),
        Habit(description="Exercise", periodicity="daily"),
        Habit(description="Meditate", periodicity="weekly"),
    ]
    
    # Initializing the AnalyticsModule with the list of Habit objects for testing
    analytics_module = AnalyticsModule(habits)

    # Testing the list_habits method to check if it correctly returns the list of habits
    assert len(analytics_module.list_habits()) == 3, "list_habits failed!"

    # Testing the filter_by_periodicity method to ensure it correctly filters habits by periodicity
    daily_habits = analytics_module.filter_by_periodicity("daily")
    assert len(daily_habits) == 2, "filter_by_periodicity failed!"
    assert all(habit.periodicity == "daily" for habit in daily_habits), "filter_by_periodicity failed!"

    # Testing the calculate_streaks method to verify if it sums streaks correctly
    for habit in habits:
        habit.mark_complete()  # Completing each habit twice to set streaks to 2
        habit.mark_complete()
    assert analytics_module.calculate_streaks() == 6, "calculate_streaks failed!"

    print("All tests passed!")

# Running the test function
test_analytics_module()
