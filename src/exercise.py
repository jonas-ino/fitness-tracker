from typing import List, TypedDict

# exercise = {
#   "exercise_name": string,
#   "rest_timer": int,
#   "set_data": [{
#       "weight": int,
#       "prev_weight": int
#   }]

class SetEntry(TypedDict):
    weight: int
    prev_weight: int

class Exercise:
    def __init__(self, name, rest_timer):
        self.name = name
        self.rest_timer = rest_timer
        self.set_data: List[SetEntry] = []

    def add_set(self, weight):
        new_set = {
            "weight": int(weight),
            "prev_weight": 0
        }
        self.set_data.append(new_set)

    def load_set(self, weight, prev_weight):
        new_set = {
            "weight": int(weight),
            "prev_weight": int(prev_weight)
        }
        self.set_data.append(new_set)

    def remove_set(self, index):
        if not self.set_data:
            print("ERROR: No sets found")      #DEBUG
            return False
        try:
            self.set_data.pop(index)
            return True
        except IndexError:
            print("ERROR: Invalid index")                               #DEBUG
            return False

    def set_weight(self, index, weight):
        # SHOULD NOT UPDATE PREVIOUS WEIGHT. THIS WILL BE HANDLED BY THE WORKOUT MANAGER WHEN IT LOADS A NEW WORKOUT
        if not self.set_data:
            print("ERROR: No sets found")
            return False
        try:
            self.set_data[index]["weight"] = weight
            return True
        except IndexError:
            print("ERROR: Invalid index")
            return False

    def print_exercise(self):
        # Returns a string representation of the workout (name, sets, rest timer)
        #   "Bench Press : 3 x 10kg : 30s Rest
        #   "Bench Press : 3 x [variable] : 30s Rest
        output = ""
        output += self.name + " : "
        num_sets = len(self.set_data)
        if num_sets <= 0:
            output += "no sets"
            return output
        output += str(num_sets) + "x"

        # Determine whether exercise has one or multiple weights
        weights = []

        variable_weights = False
        for s in self.set_data:
            if s["weight"] not in weights:
                weights.append(s["weight"])
        if len(weights) > 1:
            variable_weights = True

        if variable_weights:
            output += "["
            for i, weight in enumerate(weights):
                output += str(weight) + "kg"
                if i != len(weights) - 1:
                    output += ", "
            output += "] : "
        else:
            output += str(weights[0]) + "kg : "

        output += str(self.rest_timer) + "sec"
        return output

    def format_exercise(self):
        # for writing to file
        exercise = {
            "exercise_name": self.name,
            "rest_timer": self.rest_timer,
            "set_data": self.set_data
        }
        return exercise

