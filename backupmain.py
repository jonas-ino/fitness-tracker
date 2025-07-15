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