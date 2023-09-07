from habit import Habit

def test_habit():
    # Creating a Habit instance for testing
    my_habit = Habit(description="Read a book", periodicity="daily")

    # Testing if the description and periodicity attributes are correctly set
    assert my_habit.description == "Read a book", "Description did not match!"
    assert my_habit.periodicity == "daily", "Periodicity did not match!"

    # Testing the mark_complete method to ensure it correctly updates 'completed' and 'streak'
    my_habit.mark_complete()
    assert my_habit.completed == True, "Marking complete failed!"
    assert my_habit.streak == 1, "Streak did not increment!"

    # Testing the reset_streak method to ensure it resets the 'streak' back to 0
    my_habit.reset_streak()
    assert my_habit.streak == 0, "Resetting streak failed!"

# Running the test function to validate Habit class implementation
test_habit()
print("All tests passed!")
