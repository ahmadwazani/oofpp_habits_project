from habit import Habit
from storage_module import StorageModule
from analytics_module import AnalyticsModule
from termcolor import colored

class HabitTrackingApp:

    def __init__(self):
        # Initialize the storage module to handle all storage-related tasks
        self.storage_module = StorageModule()
        # Load the habits from the storage
        habits = self.storage_module.load_habits()
        #Pass the habits to the AnalyticsModule
        self.analytics_module = AnalyticsModule(habits)

    # To mark habit as completed and increment its streak
    def mark_habit_completed(self):
        habit_index = self.list_habits(ask_for_index=True)
        if habit_index is not None:
            self.storage_module.mark_habit_completed(habit_index)
            print("Habit marked as completed for today, streak incremented.")


    def create_habit(self):
        # Create a new habit
        print("\nCreating a new habit:")
        print("Note: Periodicity should be 'daily', 'weekly', etc.")
        description = input("Enter the description of the habit (e.g., 'Drink Water'): ")
        periodicity = input("Enter the periodicity of the habit (e.g., 'daily'): ")
        habit = Habit(description, periodicity)
        self.storage_module.save_habit(habit)
        print(f"The habit '{description}' has been successfully created.")


    def list_habits(self, page=0, habits_per_page=5, ask_for_index=True):
        # List and paginate habits
        habits = self.storage_module.load_habits()
        while True:
            start_index = page * habits_per_page
            end_index = start_index + habits_per_page
            displayed_habits = habits[start_index:end_index]

            print("Listing Habits:")
            print("--------------------------------------------------")
            print(colored("ID   Name                Periodicity    Streak", 'green'))
            print("--------------------------------------------------")
            for i, habit in enumerate(displayed_habits):
                absolute_index = start_index + i
                print(f"{absolute_index:<5}{habit.description:<20}{habit.periodicity:<15}{habit.streak:<5}")

            next_page_exists = end_index < len(habits)

            if next_page_exists:
                if ask_for_index:
                    print("Enter the index of the habit to select or 'n' for the next page:")
                else:
                    print("Press 'n' for the next page, or any other key to return to the main menu.")
            else:
                if ask_for_index:
                    print("Enter the index of the habit to select or any other key to return to the main menu:")

            choice = input()

            if choice.lower() == 'n' and next_page_exists:
                page += 1
            elif choice.isdigit():
                habit_index = int(choice)
                if 0 <= habit_index < len(habits) and ask_for_index:  
                    return habit_index
                else:
                    print("Invalid index. Please try again.")
            else:
                if ask_for_index:
                    break
                else:
                    break




    def update_habit(self):
        # Prompt the user to select a habit and update its details
        habit_index = self.list_habits(page=0)
        print("\nUpdating the habit:")
        print("Note: Periodicity should be 'daily', 'weekly', etc.")
        description = input("Enter the new description of the habit (e.g., 'Drink water'): ")
        periodicity = input("Enter the new periodicity of the habit (e.g., 'daily'): ")
        updated_habit = Habit(description, periodicity)
        self.storage_module.update_habit(habit_index, updated_habit)
        print(f"The habit has been successfully updated.")


    def delete_habit(self):
        # Delete a habit
        habit_index = self.list_habits(page=0)
        self.storage_module.delete_habit(habit_index)
        print(f"The habit has been successfully deleted.")
    

    def main_menu(self):
        # Main application loop
        while True:
            print("\n1. Create Habit")
            print("2. List Habits")
            print("3. Update Habit")
            print("4. Delete Habit")
            print("5. View Habits by Criteria")
            print("6. View Statistics")
            print("7. Mark Habit as Completed")
            print("8. Exit")
            choice = input("Choose an option: ")

            # Check if the input is an integer
            if not choice.isdigit():
                print("Invalid input! Please enter a number between 1 and 7.")
                continue
        
            if choice == '1':
                self.create_habit()
            elif choice == '2':
                self.list_habits(ask_for_index=False)
            elif choice == '3':
                self.update_habit()
            elif choice == '4':
                self.delete_habit()
            elif choice == '5':
                self.view_habits_by_criteria()
            elif choice == '6':
                self.view_statistics()
            elif choice == '7':
                self.mark_habit_completed()
            elif choice == '8':
                print("Exiting the application...")
                break
            else:
                print("Invalid option! Please try again.")
    
    def view_habits_by_criteria(self):
        print("\nView habits by specific criteria:")
        criteria = input("Enter the periodicity to filter (e.g., 'daily'): ")
        filtered_habits = self.analytics_module.filter_by_periodicity(criteria)
    
        # Display the filtered habits
        print(colored("ID   Name                Periodicity    Streak", 'green'))
        print("--------------------------------------------------")
        for i, habit in enumerate(filtered_habits):
            print(f"{i:<5}{habit.description:<20}{habit.periodicity:<15}{habit.streak:<5}")

    def view_statistics(self):
        print("\nViewing Statistics:")

        total_habits = self.analytics_module.total_habits()

        if total_habits == 0:
            print("No habits available to calculate statistics.")
            return

        avg_streak = self.analytics_module.average_streak()
        print(f"Average streak: {avg_streak}")

        max_streak = self.analytics_module.maximum_streak()
        print(f"Maximum streak: {max_streak}")

        min_streak = self.analytics_module.minimum_streak()
        print(f"Minimum streak: {min_streak}")

        print(f"Total habits: {total_habits}")



if __name__ == "__main__":
    # Initialize the HabitTrackingApp and launch the main menu
    app = HabitTrackingApp()
    app.main_menu()