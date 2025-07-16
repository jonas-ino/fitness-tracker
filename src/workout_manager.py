from src.exercise import Exercise
from src.timer import Timer

# workout.json
#   workout = {
#       "workout_name": String
#       "exercises" = [{
#          "exercise_name": string,
#          "rest_timer": int,
#          "set_data": [{
#              "weight": int,
#              "prev_weight": int
#          }]
#       }]

class WorkoutManager:
    def __init__(self):
        self.name = ""
        self.exercises = []

    def clear_workout(self):
        self.exercises.clear()

    def new_workout(self):
        self.name = ""
        self.clear_workout()

    def add_exercise(self, name, rest_timer):
        new_exercise = Exercise(name, rest_timer)
        self.exercises.append(new_exercise)

    def remove_exercise(self, index):
        if not self.exercises:
            print("ERROR: Cannot remove an exercise from an empty workout")         #DEBUG
            return False
        if 0 <= index < len(self.exercises):
            try:
                self.exercises.pop(index)
                return True
            except IndexError:
                print("Invalid index.")                                             #DEBUG
        return False

    def list_exercises(self):
        # CAN MAYBE BE REPLACED WITH A MENU FUNCTION
        if not self.exercises:
            print("No exercises.")
            return
        for i, exercise in enumerate(self.exercises):
            print(f"{i}: {exercise.display_exercise()}")

    def get_exercise(self, index):
        # CAN MAYBE BE REPLACED WITH A MENU FUNCTION
        try:
            return self.exercises[index]
        except IndexError:
            print("Invalid index.")
            return None

    # def start_workout(self):
    #
    #
    # def import_workout(self, data):
    #
    #
    def export_workout(self):
        formatted_exercises = []
        for exercise in self.exercises:
            formatted_exercises.append(exercise.format_exercise())
        data = {
            "workout_name": self.name,
            "exercises": formatted_exercises
        }
        return data
