from src.timer import Timer
#from src.reader import Reader
from src.exercise import Exercise

if __name__ == "__main__":
    test_timer = Timer()

    test_exercise = Exercise("TEST")
    test_exercise.set_sets(3)
    test_exercise.set_reps(10)
    test_exercise.set_weight(40)

    print(f"{test_exercise.format_exercise()}")
    test_exercise.print_exercise()