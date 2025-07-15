import tkinter as tk
from tkinter import filedialog

import src.file_manager as fm
from src.workout_manager import WorkoutManager

def get_path(msg):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title=msg)

def load_settings():
    temp_settings = fm.read_settings()
    if temp_settings["folder path"] == "":
        print("No folder path found. Select new location.")
        new_path = get_path("Select new folder path")
        temp_settings["folder path"] = new_path
    else:
        if not fm.verify_folder(temp_settings["folder path"]):
            print("Invalid folder path detected. Select new location.")
            new_path = get_path("Select new folder path")
            temp_settings["folder path"] = new_path
    return temp_settings

def get_workouts(folder_path):
    # TODO: Add additional folder check maybe?
    # CAN MAYBE COMBINE WITH LIST WORKOUTS DEPENDING ON WORKFLOW
    return fm.list_workouts(folder_path)

def list_workouts(wo_list):
    # If workouts exist in the specified folder, prints out each entry, stripping off the .json extension, starting at 1
    for index, wo in enumerate(wo_list):
        print(str(index + 1) + ": " + wo[:-5])

def select_workout():
    # Reminder: you can declare variables within while/for loops and use them afterwards in python
    while True:
        wo_index = input("Select a workout to import ('Q' to exit): ")
        if wo_index == "Q":
            print("Exiting.")
            exit(0)
        elif wo_index.isnumeric():
            wo_index = int(wo_index) - 1
            if 0 <= wo_index < len(workouts):
                break
            else:
                print("Selection out of range. Try again.")
        else:
            print("Invalid selection.")
    selected_wo = workouts[wo_index]
    return selected_wo


if __name__ == "__main__":

    wm = WorkoutManager()
    settings = load_settings()
    path = settings["folder path"]
    workouts = []

    print("\nTEST - READING SETTINGS")
    for key in settings:
        print(key + ": " + str(settings[key]))

    print("\nTEST - IMPORTING WORKOUTS")
    workouts = get_workouts(path)
    list_workouts(workouts)
    choice = select_workout()
    curr_workout = fm.read_workout(choice, path)
    print("\nSelected workout: " + choice)

    fm.write_settings(settings)
    wm.import_workout(curr_workout)

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