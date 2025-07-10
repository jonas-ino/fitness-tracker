import json

class FileManager:
    def __init__(self):
        self.exercises = []
        # if the file exists, boolean that it exists

    def read_file(self):
        print("TEST")
        data = []

        print("Importing date from exercises.json")
        with open("exercises.json", "r") as file:
            data = json.load(file)
            return data

        # pref.json
        #   preferences = {
        #       "type": "value"
        #   }

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

    def write_file(self, exercise_list):
        print("Writing data to exercises.json")
        with open("exercises.json", "w") as file:
            json.dump(exercise_list, file, indent=4)
