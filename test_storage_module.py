from storage_module import StorageModule
from habit import Habit

def test_save_habit():
    # Create an instance of StorageModule with a test file
    storage = StorageModule(file_path='test_habits.json')

    # Create a sample Habit object for testing
    test_habit = Habit(description="Exercise Daily", periodicity="daily")

    # Save the habit using StorageModule's save_habit method
    storage.save_habit(test_habit)

    # Load habits from the storage to verify the habit has been saved
    loaded_habits = storage.load_habits()

    # Validate the saved habit against the loaded one
    assert loaded_habits[0].description == "Exercise Daily"
    assert loaded_habits[0].periodicity == "daily"

print("Test Save Habit Passed!")


def test_load_habits():
    # Create an instance of StorageModule with a test file
    storage = StorageModule(file_path='test_habits.json')

    # Load habits from the storage
    loaded_habits = storage.load_habits()

    # Validate the loaded habits
    assert loaded_habits[0].description == "Exercise Daily"
    assert loaded_habits[0].periodicity == "daily"

print("Test Load Habits Passed!")


def test_update_habit():
    # Create an instance of StorageModule with a test file
    storage = StorageModule(file_path='test_habits.json')

    # Create a new Habit object with updated details
    updated_habit = Habit(description="Exercise Weekly", periodicity="weekly")

    # Update the habit at index 0 using StorageModule's update_habit method
    storage.update_habit(habit_index=0, updated_habit=updated_habit)

    # Load habits from storage to verify the update
    loaded_habits = storage.load_habits()

    # Validate the updated habit
    assert loaded_habits[0].description == "Exercise Weekly"
    assert loaded_habits[0].periodicity == "weekly"

print("Test Update Habit Passed!")


def test_delete_habit():
    # Create an instance of StorageModule with a test file
    storage = StorageModule(file_path='test_habits.json')

    # Delete the habit at index 0 using StorageModule's delete_habit method
    storage.delete_habit(habit_index=0)

    # Load habits from storage to verify the deletion
    loaded_habits = storage.load_habits()

    # Check if the habit list is empty as expected
    assert len(loaded_habits) == 0

print("Test Delete Habit Passed!")
