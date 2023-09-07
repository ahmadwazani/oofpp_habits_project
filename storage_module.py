import json
from json.decoder import JSONDecodeError
from habit import Habit

# The StorageModule class is responsible for all file storage operations related to habits.
class StorageModule:
    
    # Constructor initializes the StorageModule with a file path for the JSON storage.
    def __init__(self, file_path='habits.json'):
        self.file_path = file_path
        # Try reading the file to check if it exists. If not, initialize it.
        try:
            with open(self.file_path, 'r') as file:
                json.load(file)
        except FileNotFoundError:
            self.initialize_file()

    # Initializes the storage file, writing an empty list to it.
    def initialize_file(self):
        with open(self.file_path, 'w') as file:
            json.dump([], file)

    # A generic function for safe file operations, takes a mode and an operation function as arguments.
    def safe_file_operation(self, mode, operation):
        try:
            with open(self.file_path, mode) as file:
                return operation(file)
        except FileNotFoundError:
            print("The file was not found. Make sure it exists and try again.")
        except JSONDecodeError:
            print("An error occurred while decoding the JSON. The file may be corrupted or have an incorrect format.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    # Adds a new habit to the JSON storage.
    def save_habit(self, habit):
        def operation(file):
            habits = json.load(file)
            habits.append(vars(habit))
            # Reset the cursor and clear the file before writing.
            file.seek(0)
            file.truncate()
            json.dump(habits, file)
        self.safe_file_operation('r+', operation)

    # Loads all habits from the JSON storage and returns them as a list of Habit objects.
    def load_habits(self):
        def operation(file):
            try:
                habits = json.load(file)
                return [Habit(**habit) for habit in habits]
            except json.JSONDecodeError:
                print("An error occurred while decoding the JSON. The file may be corrupted or have an incorrect format.")
                return []
        return self.safe_file_operation('r', operation) or []

    # Updates a habit at a specific index in the JSON storage.
    def update_habit(self, habit_index, updated_habit):
        def operation(file):
            habits = json.load(file)
            habits[habit_index] = vars(updated_habit)
            # Reset the cursor and clear the file before writing.
            file.seek(0)
            file.truncate()
            json.dump(habits, file)
        self.safe_file_operation('r+', operation)

    # Deletes a habit at a specific index from the JSON storage.
    def delete_habit(self, habit_index):
        def operation(file):
            habits = json.load(file)
            habits.pop(habit_index)
            # Reset the cursor and clear the file before writing.
            file.seek(0)
            file.truncate()
            json.dump(habits, file)
        self.safe_file_operation('r+', operation)

    # Saves a complete list of habits to the JSON storage.
    def save_habits(self, habits_list):
        def operation(file):
            # Reset the cursor and clear the file before writing.
            file.seek(0)
            file.truncate()
            json.dump([vars(habit) for habit in habits_list], file)
        self.safe_file_operation('r+', operation)

    # Marks a habit as completed and updates the storage accordingly.
    def mark_habit_completed(self, habit_index):
        habits = self.load_habits()
        habit = habits[habit_index]
        habit.mark_complete()
        self.save_habits(habits)
