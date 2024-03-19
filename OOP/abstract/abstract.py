from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, n):
        self.no_of_tyres = n

    @abstractmethod
    def start(self):
        print("Hello")

    def display(self):
        print("Hi I'm  calling from vehicle class")

    
