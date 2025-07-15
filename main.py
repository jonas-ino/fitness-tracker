import os
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

def list_workouts(folder_path):
    # If workouts exist in the specified folder, prints out each entry, stripping off the .json extension, starting at 1
    # TODO: Add additional folder check maybe?
    wo_list = fm.list_workouts(folder_path)

    for index, wo in enumerate(wo_list):
        print(str(index + 1) + ": " + wo[:-5])


if __name__ == "__main__":

    wm = WorkoutManager()
    settings = load_settings()
    path = settings["folder path"]

    print("TEST - READING SETTINGS")
    for key in settings:
        print(key + ": " + str(settings[key]))

    print("\n\nTEST - LISTING WORKOUTS")
    list_workouts(path)

    print("\n\nTEST - IMPORTING WORKOUT")
    selected_workout = input("Select a workout to import ('Q' to exit): ")
    while True:
        if selected_workout == "Q":
            print("Exiting Program.")
            exit(0)
        elif (not selected_workout.isdigit()
        or int(selected_workout) < 1
        or int(selected_workout) > len(fm.list_workouts(path))):
            print("Invalid selection.")
        else:
            selected_workout = int(selected_workout) - 1
            try:
                fm.read_workout(fm.list_workouts(path)[selected_workout], path)
            except IndexError:
                print("Invalid selection.")



    fm.read_workout("test", path)

    fm.write_settings(settings)


# LOAD SETTINGS (if exists)
#   [Y] Load settings based on defaults
#   [N] Setup default settings

# CHECK FOLDER
#   [Y] cont.
#   [N] Setup folder

# CHECK FOLDER FOR WORKOUTS
#   [Y] Load/New
#   [N] New workout

# START/EDIT WORKOUT