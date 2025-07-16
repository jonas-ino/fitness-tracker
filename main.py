import time
import src.file_manager as fm
import src.menu as menu
from src.workout_manager import WorkoutManager
from src.exercise import Exercise

if __name__ == "__main__":

    wm = WorkoutManager()
    workouts = []

    print("\n--WORKOUT TRACKER--")
    time.sleep(0.2)

    settings = menu.load_settings()
    path = settings["folder path"]

    #menu.load_workout(path, wm)

    test = Exercise("TEST EXERCISE", 30)
    print(f"{test.print_exercise()}")

    print("\nADD SET")
    test.add_set(10)
    print(f"{test.print_exercise()}")

    print("\nADD SET")
    test.add_set(10)
    print(f"{test.print_exercise()}")

    print("\nADD SET")
    test.add_set(10)
    print(f"{test.print_exercise()}")

    print("\nADD SET")
    test.add_set(11)
    print(f"{test.print_exercise()}")

    print("\nREMOVE INVALID SET")
    test.remove_set(10)
    print(f"{test.print_exercise()}")

    print("\nREMOVE SET")
    test.remove_set(0)
    print(f"{test.print_exercise()}")

    print("\nREMOVE SET")
    test.remove_set(2)
    print(f"{test.print_exercise()}")

    print("\nEDIT SET WITH INVALID INDEX")
    test.set_weight(10, 100)
    print(f"{test.print_exercise()}")

    print("\nEDIT SET")
    test.set_weight(0, 100)
    print(f"{test.print_exercise()}")

    print("\nEND\n\n\n")





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