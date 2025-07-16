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
        new_path = get_path("New folder path")
        temp_settings["folder path"] = new_path
    else:
        if not fm.verify_folder(temp_settings["folder path"]):
            print("Invalid folder path detected. Select new location.")
            new_path = get_path("Select new folder path")
            temp_settings["folder path"] = new_path
    return temp_settings

def load_workout(folder_path, wm):
    workout_list = fm.get_workout_list(folder_path)
    current_workout = None
    print("\nLOAD WORKOUT\n")
    # CASE: Available workouts
    if workout_list:
        for workout in workout_list:
            for index, item in enumerate(workout_list):
                print(f"[{index + 1}] {item[:-5]}")
    print("[N] New workout")
    selection = input("\nSelection: ")
    while True:
        if selection == "n" or selection == "N":
            print("PLACEHOLDER: NEW WORKOUT")                               #DEBUG
            wm.clear_workout()
            break
        elif selection.isdigit():
            try:
                # CAN CHANGE TO fm.verify_workout
                index = int(selection) - 1
                current_workout = workout_list[index]
                print(f"Selected: {current_workout[:-5]}")                  #DEBUG
                if fm.verify_workout(current_workout, folder_path):
                    workout = fm.read_workout(current_workout, folder_path)
                    wm.import_workout(workout)
                    break
                else:
                    print("ERROR: WORKOUT NOT FOUND [menu.load_workout]")   #DEBUG
                    print("EXITING.")                                       #DEBUG
                    exit(0)
            except IndexError:
                print("Invalid selection.")
        else:
            print("Invalid selection.")



def save_workout(folder_path, wm):
    print("TEMP")





# def get_workouts(folder_path):
#     return fm.get_workout_list(folder_path)
#
# def list_workouts(wo_list):
#     # If workouts exist in the specified folder, prints out each entry, stripping off the .json extension, starting at 1
#     for index, wo in enumerate(wo_list):
#         print("[" + str(index + 1) + "] " + wo[:-5])
#
# def verify_wo_index(wo_list, selection):
#     if selection.isnumeric() and 0 <= int(selection) < len(wo_list):
#         return True
#     else:
#         return False

# def load_workout(wm, folder_path):
#     wo_list =

# def new_workout
# def load_workout
# def select_workout
