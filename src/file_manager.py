import json
import os

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

# def verify_workout(workout_name, folder_path):
#     if verify_folder(folder_path):
#         if os.path.exists(folder_path + "/" + workout_name + ".json"):
#             return True
#     return False
#
# def list_workouts(folder_path):
#     workout_list = []
#     if verify_folder(folder_path):
#         for file in os.listdir(folder_path):
#             if file.endswith(".json"):
#                 workout_list.append(file)
#     return workout_list
#
# def read_workout(workout_name, folder_path):
#     if verify_workout(workout_name, folder_path):
#         with open(folder_path + "/" + workout_name + ".json", "r") as file:
#             return json.load(file)
#     else:
#         print("File not found. Exiting.")
#         return None
# --------------------------------------------------------------------------------









# class FileManager:
#     def __init__(self):
#         self.exercises = []
#         self.settings = []
#
#     def read_exercises(self):
#         print("Importing data from exercises.json")
#         with open("exercises.json", "r") as file:
#             self.exercises = json.load(file)
#             return self.exercises
#
#         # exercises.json
#         #   exercise = {
#         #       "exercise": "name",
#         #       "sets": "number",
#         #       "reps": "number",
#         #       "weight": "number"
#         #       "prev_weight": "number"
#         #   }
#
#         # ADVANCED
#         #   exercises = {
#         #       "exercise": "name",
#         #       "sets": integer,
#         #       "set_data": tuple(weight, prev_weight)
#
#     def write_exercises(self):
#         print("Writing data to exercises.json")
#         with open("exercises.json", "w") as file:
#             json.dump(self.exercises, file, indent=4)
#
#     def read_settings(self):
#         print("Importing settings from settings.json")
#         with open("settings.json", "r") as file:
#             self.settings = json.load(file)
#             return self.settings
#
#         # settings.json
#         #   settings = {
#         #       "folder_path" : string
#         #       "default_rest" : int
#
#     def write_settings(self):
#         print("Writing data to exercises.json")
#         with open("settings.json", "w") as file:
#             json.dump(self.settings, file, indent=4)
#
#     def validate_exercises(self):
#         return True
#
#     def validate_settings(self):
#         return True
