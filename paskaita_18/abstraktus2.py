from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def get_role(self):
        pass