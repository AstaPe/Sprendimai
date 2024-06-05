class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0

    def get_current_value(self):
        return self.value


if __name__ == "__main__":
    counter = Counter()

    print("Initial value:", counter.get_current_value())

    counter.increment()
    print("After increment:", counter.get_current_value())

    counter.decrement()
    print("After decrement:", counter.get_current_value())

    counter.reset()
    print("After reset:", counter.get_current_value())
