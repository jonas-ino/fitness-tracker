import json
import os

# TODO: CHANGE BACK TO OBJECT WITH VARIABLES:
#   FOLDER LOCATION
#   CURRENT WORKOUT NAME
#   Settings?
# SETTINGS -----------------------------------------------------------------------
def default_settings():
    settings = {
        "folder path" : "",
        "default rest" : 30
    }
    return settings
def read_settings():
    # Loads settings.json file, updating only specific keys. If these do not exist, uses default values
    # TODO: Change to absolute path relative to script file before compilation
    settings = default_settings()
    try:
        with open("settings.json", "r") as file:
            new_settings = json.load(file)
        for key in new_settings:
            if key in settings:
                settings[key] = new_settings[key]
    except FileNotFoundError:
        write_settings(settings)

    return settings

def write_settings(settings):
    with open("settings.json", "w") as file:
        json.dump(settings, file, indent=4)
# --------------------------------------------------------------------------------

# WORKOUTS -----------------------------------------------------------------------
def verify_folder(folder_path):
    if os.path.exists(folder_path):
        return True
    else:
        return False

def verify_workout(workout_name, folder_path):
    # TODO: Fix error case: .json file is present, but empty
    if verify_folder(folder_path):
        if os.path.exists(folder_path + "/" + workout_name):
            return True
    return False

def list_workouts(folder_path):
    workout_list = []
    if verify_folder(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".json"):
                workout_list.append(file)
    return workout_list

def read_workout(file_name, folder_path):
    if verify_workout(file_name, folder_path):
        with open(folder_path + "/" + file_name, "r") as file:
            workout = json.load(file)
            return workout
    else:
        print(f"{folder_path}/{file_name} not found.")
        return None

def write_workout(file_name, folder_path, workout):
    with open(folder_path + "/" + file_name, "w") as file:
        json.dump(workout, file, indent=4)
# --------------------------------------------------------------------------------

    # exercises.json
    #   exercise = {
    #       "exercise": "name",
    #       "sets": "number",
    #       "reps": "number",
    #       "weight": "number"
    #       "prev_weight": "number"
    #   }

    # ADVANCED
    #   exercises = {
    #       "exercise": "name",
    #       "sets": integer,
    #       "set_data": tuple(weight, prev_weight)

