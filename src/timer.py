import time
import math

def format_time(seconds):
    second, millisecond = divmod(int(seconds * 1000), 1000)
    minute, second = divmod(second, 60)
    return f"{minute:02d}:{second:02d}:{millisecond:03d}"

class Timer:
    # LOOKS AT:
    # Time class (performance counter), updating outputs, etc.
    # Threads
    def __init__(self):
        self.start = 0
        self.end = 0

    def tick(self):
        elapsed = time.perf_counter() - self.start
        print(format_time(elapsed), end='\r', flush=True)

    def run(self):
        self.start = time.perf_counter()
        try:
            while True:
                time.sleep(.01)
                self.tick()
        except KeyboardInterrupt:
            self.end = time.perf_counter()
            print(f"\n{format_time(self.end - self.start)}")
            # Change keyboard interrupt to something else. Return
            exit(0)

    def countdown(self, duration):
        self.start = time.perf_counter()
        while time.perf_counter() - self.start < duration:
            time.sleep(.01)
            self.tick()
        self.end = time.perf_counter()
        print(f"{format_time(math.floor(self.end - self.start))}", end='\r', flush=True)
