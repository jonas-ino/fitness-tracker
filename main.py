import time
import json
import src.file_manager as fm
import src.menu as menu
from src.workout_manager import WorkoutManager

#TODO: Save file_name. When workout name is changed, delete original file before writing new one
#TODO: When saving a workout, change spaces in file name to underscores
#TODO: Normalise error messages and how they are handled
#TODO: "finish workout" option - saves current weights to prev weight (probs put in workoutManager)
#TODO: Change to absolute path relative to script file before compilation
#TODO: [fm.verify_workout] Fix error case: .json file is present, but empty
#   Can just use the same logic as with loading settings

if __name__ == "__main__":

    # Load settings from settings.json file
    settings = menu.load_settings()

    # Load settings data to variables for easy access
    path = settings["folder_path"]
    default_rest = settings["default_rest"]
    wm = WorkoutManager(default_rest)

    while True:
        print("\n== WORKOUT TRACKER ==\n")
        menu.display_options(wm)
        option = input("\nSelect an option (Q to quit): ")

        if option == "1": #------------------------- New Workout
            print("Selected: New Workout")
            menu.new_workout(wm)
        elif option == "2": #----------------------- Load Workout
            print("Selected: Load Workout")
            menu.load_workout(path, wm)
        elif option == "3": #----------------------- Save Workout
            print("Selected: Save Workout")
            menu.save_workout(path, wm)
        elif option == "4": #----------------------- Settings                           #TODO
            print("Selected: Settings")
        elif option.lower() == "q": #--------------- Exit
            print("Exiting...")
            break
            # Ask to save workout
        elif option == "0" and wm.loaded: #----------- View workout
            print("Selected: Workout View")
            while True:
                menu.view_workout(wm)
                option = input("\nSelect an option (Q to quit): ")
                if option.lower() == "q":
                    break
                elif option == "1": # -----( VIEW WORKOUT [1] )----- Begin workout      TODO
                    print("\nSelected: Begin workout")
                    menu.wo_begin(wm)
                elif option == "2": # -----( VIEW WORKOUT [2] )----- Add exercise
                    print("\nSelected: Add exercise")
                    menu.wo_add_exercise(wm)
                elif option == "3": # -----( VIEW WORKOUT [3] )----- Edit exercise      TODO
                    print("\nSelected: Edit exercise")
                    while True:
                        # SELECT EXERCISE FROM QUERY LIST
                        menu.list_exercises(wm)
                        selected_exercise = menu.select_exercise(wm)

                        # SHOW OPTIONS
                        menu.exercise_options()
                        selection = input("\nSelect an option (Q to quit): ")
                        if selection == "1":     # [1] Add set
                            print("Selected: Add set")
                            menu.ex_add(wm, selected_exercise)
                        elif selection == "2":  # [2] Remove set
                            print("Selected: Remove set")
                            # QUERY WHICH SET (break if no exercises)
                            # TRY REMOVE SET
                            menu.ex_remove(selected_exercise)
                        elif selection == "3":  # [3] Edit weight           #TODO
                            print("Selected: Edit weight")
                            # QUERY WHICH SET (break if no exercises)
                            menu.ex_edit_weight(wm)
                        elif selection == "4":  # [4] Rename exercise       #TODO
                            print("Selected: Rename exercise")
                        elif selection == "5":  # [5] Add comment           #TODO
                            print("Selected: Add comment")
                            print("Comments haven't been implemented yet...")
                            break
                        elif selection == "q":  # QUIT
                            break
                        else:
                            print("Invalid Selection")
                elif option == "4": # -----( VIEW WORKOUT [4] )----- Remove exercise
                    print("\nSelected: Remove exercise")
                    index = 0
                    menu.wo_remove_exercise(wm)
                elif option == "5": # -----( VIEW WORKOUT [5] )----- Rename workout
                    print("\nSelected: Rename workout")
                    menu.wo_rename_workout(wm)
                elif option == "6":
                    print("\nSelected: Save workout")
                    menu.save_workout(path, wm)
                else:
                    print("Invalid selection.")
        else:
            print("Invalid selection.")