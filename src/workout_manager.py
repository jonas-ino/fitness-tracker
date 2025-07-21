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
    def __init__(self, rest_timer):
        self.name = ""
        self.exercises = []
        self.rest_timer = rest_timer
        self.loaded = False
        self.file_name = ""

    def clear_workout(self):
        self.exercises.clear()
        self.loaded = False

    def new_workout(self):
        self.name = ""
        self.clear_workout()
        self.loaded = True

    def add_exercise(self, name):
        new_exercise = Exercise(name, self.rest_timer)
        self.exercises.append(new_exercise)

    # ADD SET - MENU
    # REMOVE SET - MENU
    # EDIT SET - MENU

    def remove_exercise(self, index):
        if not self.exercises:
            print("ERROR: Cannot remove an exercise from an empty workout")         #DEBUG
            return
        if 0 <= index < len(self.exercises):
            try:
                self.exercises.pop(index)
                return
            except IndexError:
                print("Invalid index.")                                             #DEBUG
        return

    # def start_workout(self):
    # def import_workout(self, data):

    def import_workout(self, data):
        self.loaded = True
        self.name = data["workout_name"]
        self.file_name = data["file_name"]
        formatted_exercises = data["exercises"]
        for ex in formatted_exercises:
            temp_name = ex["exercise_name"]
            temp_rest = ex["rest_timer"]
            temp_set_data = ex["set_data"]
            temp_exercise = Exercise(temp_name, temp_rest)
            for temp_set in temp_set_data:
                temp_exercise.load_set(temp_set["weight"], temp_set["prev_weight"])
            self.exercises.append(temp_exercise)

    def export_workout(self):
        formatted_exercises = []
        for exercise in self.exercises:
            formatted_exercises.append(exercise.format_exercise())
        data = {
            "workout_name": self.name,
            "file_name": self.file_name,
            "exercises": formatted_exercises
        }
        return data
