class Exercise:
    def __init__(self, name):
        self.name = name
        self.sets = 0
        self.reps = 0
        self.weight = 0
        self.prev_weight = 0
        self.rest_timer = 30

        # self.sets = []
        # GOAL: allow modular set changes

    def set_name(self, name):
        self.name = name

    def set_sets(self, sets):
        self.sets = sets

    def set_reps(self, reps):
        self.reps = reps

    def set_weight(self, weight):
        self.prev_weight = self.weight
        self.weight = weight

    def set_rest_timer(self, rest_timer):
        self.rest_timer = rest_timer

    def print_exercise(self):
        print(f"{self.name}: {self.sets}x{self.reps} ({self.weight}kg)")

    def format_exercise(self):
        # for writing to file
        exercise = {
            "name": self.name,
            "sets": self.sets,
            "reps": self.reps,
            "weight": self.weight,
            "prev_weight": self.prev_weight,
            "rest_timer": self.rest_timer
        }
        return exercise
