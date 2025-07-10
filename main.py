from src.file_manager import FileManager
from src.timer import Timer
from src.workout_manager import WorkoutManager

if __name__ == "__main__":
    test_timer = Timer()
    manager = WorkoutManager()
    file_manager = FileManager()

    manager.import_workout(file_manager.read_file())

    file_manager.write_file(manager.export_workout())