import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0

    def start(self):
        if not self.start_time:
            self.start_time = time.time()
        else:
            print("Timer is already running.")

    def stop(self):
        if self.start_time:
            self.end_time = time.time()
            self.elapsed_time += self.end_time - self.start_time
            self.start_time = None
        else:
            print("Timer is not running.")

    def reset(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0

    def get_elapsed_time(self):
        if self.start_time:
            current_time = time.time()
            return self.elapsed_time + (current_time - self.start_time)
        else:
            return self.elapsed_time

# Example usage:
if __name__ == "__main__":
    timer = Timer()

    timer.start()
    time.sleep(2)
    timer.stop()

    print("Elapsed time:", timer.get_elapsed_time(), "seconds")
    timer.reset()

    timer.start()
    time.sleep(3)
    timer.stop()

    print("Elapsed time:", timer.get_elapsed_time(), "seconds")
