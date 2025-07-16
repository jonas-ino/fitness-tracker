from src.exercise import Exercise
from src.timer import Timer

class WorkoutManager:
    def __init__(self):
        self.name = ""
        self.exercises = []

    def add_exercise(self):
        # This should all be handled by the menu class
        print("Name: ")
        name = input()
        exercise = Exercise(name)
        print("Sets: ")
        exercise.set_sets(input())
        # ADD ERROR HANDLING
        print("Reps: ")
        exercise.set_reps(input())
        # ADD ERROR HANDLING
        print("Weight: ")
        exercise.set_weight(input())
        # ADD ERROR HANDLING

        self.exercises.append(exercise)

    def remove_exercise(self):
        if not self.exercises:
            print("No exercises.")
            return
        self.list_exercises()
        print("REMOVE EXERCISE ('-1' to cancel): ")
        choice = int(input())
        # FIX: if 'choice' is not integer
        if choice != '-1':
            try:
                self.exercises.pop(choice)
            except IndexError:
                print("Invalid index.")

    # def overwrite_exercise(self, index, exercise):
    #     self.exercises[index] = exercise

    def clear_workout(self):
        self.exercises.clear()

    def list_exercises(self):
        if not self.exercises:
            print("No exercises.")
            return
        for i, exercise in enumerate(self.exercises):
            print(f"{i}: {exercise.display_exercise()}")

    # modify exercise??
    #

    def start_workout(self):
        timer = Timer()
        timer.countdown(int(input("Duration: ")))

    def import_workout(self, data):
        self.clear_workout()
        for ex in data:
            temp = Exercise(ex["name"])
            temp.set_sets(ex["sets"])
            temp.set_reps(ex["reps"])
            temp.set_weight(ex["weight"])
            self.exercises.append(temp)
        self.list_exercises()

    def export_workout(self):
        export = []
        for exercise in self.exercises:
            export.append(exercise.format_exercise())
        return export