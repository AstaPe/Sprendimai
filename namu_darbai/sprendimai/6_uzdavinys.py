from namu_darbai.classes.fitness_tracker6 import FitnessTracker

tracker = FitnessTracker("Asta")


tracker.add_steps(5000)
tracker.add_steps(6000)


tracker.reset_steps()


tracker.add_steps(12000)