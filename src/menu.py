import os
import tkinter as tk
from tkinter import filedialog

import src.file_manager as fm
from src.workout_manager import WorkoutManager

# SETUP ----------------------------------------------------------------------
def get_path(msg):
    # Returns a string interpretation of a user-selected folder path
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title=msg)

def load_settings():
    # Uses FileManager to load settings to a dictionary, ensuring a valid folder path
    temp_settings = fm.read_settings()
    if temp_settings["folder_path"] == "":
        print("No folder path found. Select new location.")
        new_path = get_path("New folder path")
        temp_settings["folder_path"] = new_path
    else:
        if not fm.verify_folder(temp_settings["folder_path"]):
            print("Invalid folder path detected. Select new location.")
            new_path = get_path("Select new folder path")
            temp_settings["folder_path"] = new_path
    return temp_settings
# ----------------------------------------------------------------------------------

# UI OPTIONS ---------------------------------------------------
def display_options(wm):
    print("Active workout: ", end="")
    if not wm.loaded:
        print("None")
    else:
        print(f"{wm.name}")
    if wm.loaded:
        print("[0] View workout")
    print("[1] New workout")
    print("[2] Load workout")
    print("[3] Save workout")
    print("[4] Settings")
    # Q to quit

def workout_options():
    print("[1] Begin workout")
    print("[2] Add exercise")
    print("[3] Edit exercise")
    print("[4] Remove exercise")
    print("[5] Rename workout")
    print("[6] Save workout")
    # Q to quit

def exercise_options():
    print("[1] Add set")
    print("[2] Remove set")
    print("[3] Edit weight")
    print("[4] Rename exercise")
    print("[5] Add comment")
    # Q to quit

def print_workout(wm):
    if not wm.loaded:
        print("No workout loaded.")
        return
    print(f"{wm.name}")
    for exercise in wm.exercises:
        print(f"{exercise.print_exercise()}")

def list_exercises(wm):
    if not wm.loaded:
        print("No workout loaded.")
        return
    if wm.exercises:
        for index, exercise in enumerate(wm.exercises):
            print(f"[{index + 1}] {exercise.print_exercise()}")
    else:
        print("No exercises")


def yn_query(prompt):
    # General query prompt. Asks for Y/N response, and returns true/false. Loops until valid input
    while True:
        selection = input(f"{prompt} [Y/N]: ")
        if selection.lower() == "y":
            return True
        elif selection.lower() == "n":
            return False
        else:
            print("Invalid input.\n")

def list_query(prompt, l):
    # OPTIONS MUST BE FROM 1 - len(list)
    # Returns either a valid index, or "q"
    while True:
        selection = input(f"{prompt} ")
        if selection.lower() == "q":
            return "q"
        if selection.isdigit() and 0 <= int(selection) - 1 <= len(l):
            try:
                return selection
            except IndexError:
                print("input out of range.\n")
        else:
            print("[list_query] Invalid input.\n")


def rename_query(wm):
    if not wm.loaded:
        new_name = input("Enter workout name: ")
    else:
        new_name = input("Enter new workout name: ")
        if new_name == "":
            new_name = wm.name
    if new_name == "":
        new_name = "Untitled"
    wm.name = new_name

def select_exercise(wm):
    selected_exercise = None
    if not wm.loaded:
        print("No workout loaded.")
        return selected_exercise

    while True:
        selection = list_query("Select an exercise to edit (Q to quit): ", wm.exercises)
        if selection.lower() == "q":
            break
        else:
            try:
                selected_exercise = wm.exercises[int(selection) - 1]
                break
            except IndexError:
                print("index out of range")
    return selected_exercise


def workout_view(wm):
    # Clear terminal

    # Exercise name
    # - [1] 00kg (prev. 00kg)
    # - [2] 11kg (prev. 11kg)

    print(f"== {wm.name} ==\n")
    if not wm.exercises:
        print("No exercises")
    else:
        for exercise in wm.exercises:
            print(f"{exercise.name}")  # Could also say what type of exercise it is here
            # Notes could go there:
            if len(exercise.set_data) == 0:
                print("- No sets")
            else:
                for set_id, ex_set in enumerate(exercise.set_data):
                    print(f"- [{set_id + 1}] {ex_set["weight"]}kg (prev. {ex_set["prev_weight"]}kg)")
            print()

# ----------------------------------------------------------------------------------

# MENU OPTIONS ----------------------------------------------------------------------
# [0] View Workout
def view_workout(wm):
    if not wm.loaded:
        print("ERROR: No workout loaded.")
        return
    workout_view(wm)
    workout_options()

# [1] New Workout
def new_workout(wm):
    if not wm.loaded:
        wm.new_workout()
        rename_query(wm)
        return
    else:
        print(f"{wm.name} currently loaded. ")
        selection = yn_query("Create new workout? Any changes to the current workout will be lost.")
        if selection:
            wm.new_workout()
            rename_query(wm)
            return
        return

# [2] Load Workout
def load_workout(folder_path, wm):
    workout_list = fm.get_workout_list(folder_path)
    if workout_list:
        for index, item in enumerate(workout_list):
            print(f"[{index + 1}] {item[:-5]}")
    print("[N] New workout")
    selection = input("\nSelection: ")
    while True:
        if selection == "n" or selection == "N":
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
                    wm.clear_workout()
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

# [3] Save Workout
def save_workout(folder_path, wm):
    workout_name = wm.name
    workout_name = workout_name.strip().replace(" ", "_").lower()
    if workout_name == "" or workout_name is None:
        workout_name = "untitled"
        wm.name = workout_name
    if not workout_name.endswith(".json"):
        workout_name += ".json"
    formatted_workout = wm.export_workout()

    # DELETE OLD FILE
    if workout_name != wm.file_name:
        old_file_path = folder_path + "/" + wm.file_name
        if os.path.exists(old_file_path):
            print(f"Overwriting {wm.file_name} with {workout_name}...")
            try:
                os.remove(old_file_path)
            except OSError:
                print("ERROR: Could not delete old file.")

    fm.write_workout(workout_name, folder_path, formatted_workout)

# [4] Settings
def edit_settings(settings):
    print("WILL BE ADDED")

# [5] Exit
def exit_message(folder_path, wm):
    selection = yn_query("Save changes?")
    if selection:
        save_workout(folder_path, wm)
    return
# ----------------------------------------------------------------------------------

# WORKOUT OPTIONS ------------------------------------------------------------------

# [1] Begin workout
def wo_begin(wm):
    print("Selected: Begin workout")
    print("TO BE COMPLETED")

# [2] Add exercise
def wo_add_exercise(wm):    #DEBUG
    while True:
        ex_name = input("Exercise name (Q to quit): ")
        if ex_name == "":
            print("Exercise name cannot be empty.")
        elif ex_name.lower() == 'q':
            break
        else:
            wm.add_exercise(ex_name)
            print_workout(wm)
            break

# [3] Edit exercise
def wo_edit_exercise(wm, index):
    # List query
    print("Selected: Edit exercise")        #DEBUG
    print("TO BE COMPLETED")

# [4] Remove exercise
def wo_remove_exercise(wm):
    if not wm.exercises:
        print("No exercises in current workout.\n")
        return
    list_exercises(wm)
    while True:
        selection = list_query("Select exercise to remove (Q to quit): ", wm.exercises)
        if selection.isdigit() and 0 <= int(selection) - 1 < len(wm.exercises):
            wm.remove_exercise(int(selection) - 1)
            print_workout(wm)
            break
        elif selection.lower() == "q":
            break
        else:
            print("Invalid selection.")

# [5] Rename workout
def wo_rename_workout(wm):
    while True:
        new_name = input("Enter new workout name (Q to quit): ")
        if new_name == "" or new_name.lower() == "q":
            return
        wm.name = new_name
        return

# ----------------------------------------------------------------------------------

# WORKOUT OPTIONS ------------------------------------------------------------------

# [1] Add set
def ex_add(wm, exercise):
    # Adds a new set with user-defined weight
    while True:
        print(exercise.name)
        print(exercise.print_sets())
        ex_weight = input("Enter exercise weight (Q to quit): ")
        if ex_weight.isdigit():
            exercise.add_set(ex_weight)
        elif ex_weight.lower() == "q":
            break
        else:
            print("Invalid input.")

# [2] Remove set
def ex_remove(exercise):
    # Removes a user-selected set from the specified exercise
    while True:
        if exercise.set_data:
            print(exercise.name)
            print(exercise.print_sets())
        else:
            print("Exercise has no sets.")
            break
        selection = list_query("Select set to remove (Q to quit): ", exercise.set_data)
        if selection.lower() == "q":
            break
        else:
            try:
                exercise.remove_set(int(selection) - 1)
                break
            except IndexError:
                print("Invalid selection.")

# [3] Change weight
def ex_edit_weight(exercise):
    # Allows the user to edit the weight of an exercise (does not affect previous weight)
    while True:
        if exercise.set_data:
            print(exercise.name)
            print(exercise.print_sets())
        else:
            print("Exercise has no sets.")
            break
        selection = list_query("Select set to edit (Q to quit): ", exercise.set_data)
        if selection.lower() == "q":
            break
        else:
            while True:
                new_weight = input("Enter new weight (Q to quit): ")
                if new_weight.isdigit():
                    exercise.edit_set_weight(int(selection) - 1, new_weight)
                    break
                elif new_weight.lower() == "q":
                    break
                else:
                    print("Invalid input.")
            break

# [4] rename exercise
def ex_rename_exercise(exercise):
    print("Selected: Rename exercise")

# [5] Add comment
def ex_comment(exercise):
    print("Selected: Edit comment")

# ----------------------------------------------------------------------------------

