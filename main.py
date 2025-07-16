import time
import src.file_manager as fm
import src.menu as menu
from src.workout_manager import WorkoutManager

import json

if __name__ == "__main__":

    wm = WorkoutManager()
    workouts = []

    print("\n--WORKOUT TRACKER--")
    time.sleep(0.2)

    settings = menu.load_settings()
    path = settings["folder_path"]

    #menu.load_workout(path, wm)
    default_rest = settings["default_rest"]
    wm.new_workout()
    wm.name = "TEST WORKOUT"

    wm.add_exercise("test1", default_rest)
    wm.exercises[0].add_set(10)
    wm.exercises[0].add_set(20)

    wm.add_exercise("test2", default_rest)
    wm.exercises[1].add_set(10)
    wm.exercises[1].add_set(20)

    wm.add_exercise("test3", default_rest)
    wm.exercises[2].add_set(10)
    wm.exercises[2].add_set(20)

    print(f"{wm.name}")
    for exercise in wm.exercises:
        print(f"{exercise.print_exercise()}")

    with open("testExercises.json", "w") as file:
        json.dump(wm.export_workout(), file, indent=4)


            #
            # with open("settings.json", "w") as file:
            #     json.dump(settings, file, indent=4)

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