from src.file_manager import FileManager
from src.timer import Timer
from src.workout_manager import WorkoutManager
import time

def startup():
    print("\n--WORKOUT TRACKER--")

def menu_options():
    #TODO: Clear unnecessary lines afterwards \033[F, \033[K
    time.sleep(1)
    print("\n1. Add Exercise")
    print("2. Remove Exercise")
    print("3. View Workout")
    print("4. Clear Workout")
    print("5. Stopwatch")
    print("6. Exit")

def add_exercise(wm):
    wm.add_exercise()
    #TODO: Feedback that it has worked

def remove_exercise(wm):
    wm.remove_exercise()

def view_workout(wm):
    wm.list_exercises()

def clear_workout(wm):
    wm.clear_exercises()

def stopwatch(timer):
    # TODO: Implement stopwatch interaction
    timer.run()

if __name__ == "__main__":
    timer = Timer()
    manager = WorkoutManager()
    file_manager = FileManager()

    startup()
    manager.import_workout(file_manager.read_file())

    while True:
        menu_options()
        option = input("\nSelect an option: ")

        if option == "1":
            add_exercise(manager)
        elif option == "2":
            remove_exercise(manager)
        elif option == "3":
            view_workout(manager)
        elif option == "4":
            clear_workout(manager)
        elif option == "5":
            stopwatch(timer)
        elif option == "6":
            print("Exiting.")
            break
        else:
            print("Invalid option.")

    file_manager.write_file(manager.export_workout())