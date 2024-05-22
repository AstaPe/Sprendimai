class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self._steps = 0

    def _check_goal(self):
        if self._steps >= 10000:
            print("Congratulations! You've reached your daily step goal of 10,000 steps.")

    def add_steps(self, steps):
        self._steps += steps
        self._check_goal()
        print(f"{steps} steps added. Current step count: {self._steps}")

    def reset_steps(self):
        self._steps = 0
        print("Step count reset.")

    def get_steps(self):
        return self._steps