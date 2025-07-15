import time
import math

def format_time(seconds):
    second, millisecond = divmod(int(seconds * 1000), 1000)
    minute, second = divmod(second, 60)
    return f"{minute:02d}:{second:02d}:{millisecond:03d}"

class Timer:
    # FOCUS: time class, dynamic output, threads
    def __init__(self):
        # Constructor
        self.start = 0
        self.end = 0

    def tick(self):
        # 'Ticks' the clock forward .01 seconds and prints the formatted time
        # Carriage makes the output appear as though it is updating, flush ensures accuracy
        time.sleep(.01)
        elapsed = time.perf_counter() - self.start
        print(format_time(elapsed), end='\r', flush=True)

    def run(self):
        # Runs a constantly updating stopwatch until the exit command (ctrl + c) is pressed
        self.start = time.perf_counter()
        try:
            while True:
                self.tick()
        except KeyboardInterrupt:
            self.end = time.perf_counter()
            print(f"\n{format_time(self.end - self.start)}")
            # Change keyboard interrupt to something else. Return
            exit(0)

    def countdown(self, duration):
        # Counts down until the provided duration
        self.start = time.perf_counter()
        while time.perf_counter() - self.start < duration:
            time.sleep(.01)
            self.tick()
        self.end = time.perf_counter()
        print(f"{format_time(math.floor(self.end - self.start))}", end='\r', flush=True)
        # PLACEHOLDER SOUND
        print("\a")
