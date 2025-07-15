from src.file_manager import FileManager
from src.timer import Timer
from src.workout_manager import WorkoutManager
import time

def startup(fm, wm):
    print("\n--WORKOUT TRACKER--")
    time.sleep(0.2)
    while True:
        selection = input("\n[1] Load File\n[2] New Workout\n[3] Exit\n\nSelect an option:")
        if selection == "1":
            break
        elif selection == "2":
            break
        elif selection == "3":
            exit(0)
        else:
            print("Invalid option.")
            time.sleep(0.2)

# def menu_options():
#     #TODO: Clear unnecessary lines afterwards \033[F, \033[K
#     time.sleep(1)
#     print("\n------------------------")
#     print("MENU")
#     print("[1] Add Exercise")
#     print("[2] Remove Exercise")
#     print("[3] View Workout")
#     print("[4] Clear Workout")
#     print("[5] Stopwatch")
#     print("[6] Exit")
#     print("------------------------\n")
#
# def add_exercise(wm):
#     wm.add_exercise()
#     #TODO: Feedback that it has worked
#
# def remove_exercise(wm):
#     wm.remove_exercise()
#
# def view_workout(wm):
#     wm.list_exercises()
#
# def clear_workout(wm):
#     wm.clear_exercises()
#
# def stopwatch(wm):
#     # TODO: Implement stopwatch interaction
#     wm.start_workout()

if __name__ == "__main__":
    workout_manager = WorkoutManager()
    file_manager = FileManager()

    startup()
    # workout_manager.import_workout(file_manager.read_file())
    #
    # while True:
    #     menu_options()
    #     option = input("\nSelect an option: ")
    #
    #     if option == "1":
    #         add_exercise(workout_manager)
    #     elif option == "2":
    #         remove_exercise(workout_manager)
    #     elif option == "3":
    #         view_workout(workout_manager)
    #     elif option == "4":
    #         clear_workout(workout_manager)
    #     elif option == "5":
    #         stopwatch(workout_manager)
    #     elif option == "6":
    #         print("Exiting.")
    #         break
    #     else:
    #         print("Invalid option.")
    #
    # file_manager.write_file(workout_manager.export_workout())

    import os
    import tkinter as tk
    from tkinter import filedialog
    import json

    from src.file_manager import FileManager
    from src.workout_manager import WorkoutManager


    def load_folder():
        # TODO: DEFAULT FOLDER IS %/WORKOUTS
        root = tk.Tk()
        root.withdraw()

        while True:
            selection = input("[1] Select folder\n[2] Exit\nSelection: ")
            if selection == "1":
                folder_path = filedialog.askdirectory(title="Select exercise folder")
                if folder_path:
                    print("Selected folder: " + folder_path)
                    return folder_path
                else:
                    print("No folder selected.")
            elif selection == "2":
                "Exiting."
                exit(0)
            else:
                print("Invalid option.")


    if __name__ == "__main__":
        print("TEST")

        wm = WorkoutManager()
        fm = FileManager()
        folder_path = load_folder()

        settings = {
            "folder_path": folder_path,
            "default_rest": 30
        }
        with open("settings.json", "w") as file:
            json.dump(settings, file, indent=4)

    # settings.json
    # default_folder : %/workouts
    # default_rest : 30