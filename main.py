import time
import src.file_manager as fm
import src.menu as menu
from src.workout_manager import WorkoutManager

import json

if __name__ == "__main__":

    wm = WorkoutManager()
    workouts = []

    time.sleep(0.2)

    settings = menu.load_settings()
    # Load settings data to variables for easy access
    path = settings["folder_path"]
    default_rest = settings["default_rest"]

    # Hyatus Hernia
    while True:
        print("\n== WORKOUT TRACKER ==\n")
        menu.display_options(wm)
        option = input("\nSelect an option: ")

        if option == "1":           # New Workout
            print("Selected: New Workout")
            menu.new_workout(wm)
        elif option == "2":         # Load Workout
            print("Selected: Load Workout")
            menu.load_workout(path, wm)
        elif option == "3":         # Save Workout
            print("Selected: Save Workout")
        elif option == "4":         # Settings
            print("Selected: Settings")                 # DEBUG
            break                                       # DEBUG
        elif option == "5":         # Exit
            print("Exiting...")
            break
            # Ask to save workout
        else:
            print("Invalid selection.")

    #menu.load_workout(path, wm)
    menu.load_workout(path, wm)

    menu.print_workout(wm)

    menu.save_workout(path, wm)

    fm.write_settings(settings)

# LOAD SETTINGS (if exists) [✓]
#   [Y] Load settings based on defaults
#   [N] Setup default settings

# CHECK FOLDER [✓]
#   [Y] cont.
#   [N] Setup folder

# CHECK FOLDER FOR WORKOUTS [✓ PARTIAL]
#   [Y] Load/New
#   [N] New workout

# START/EDIT WORKOUT