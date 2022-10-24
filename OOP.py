# Watto needs a new system for organizing his inventory of podracers.
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

# Define a repair() method that will update the condition of the podracer to "repaired".
    def repair(self):
        self.condition = "repaired"


# Given a pod created from your defined Podracer class, running pod.repair() and printing the pod.condition afterwards should display "repaired" in the console.
pod = Podracer(2, "perfect", 20)
pod.repair()
print(pod.condition)

# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will
# multiply max_speed by 2.


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

# Given another new_pod created from your defined AnakinsPod class with a max_speed of 2, running new_pod.boost() and printing the new_pod.max_speed afterwards should display "4".


new_pod = AnakinsPod(2, "perfect", 40)
new_pod.boost()
print(new_pod.max_speed)

# Define another class that inherits Podracer and call this one SebulbasPod.
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self):
        self.condition = "trashed"

# Given a third_pod created from your defined SebulbasPod class, running third_pod.flame_jet() and printing the third_pod.condition afterwards should display "thrashed" in the console.


third_pod = SebulbasPod(2, "perfect", 60)
third_pod.flame_jet()
print(third_pod.condition)


# Make sure to answer the following prompts about your coding experience:

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Answer: This solution demonstrate the inheritance that is considered one of the four pillars of OOP.It allows for one class(child class) to inherit the fields and methods of another class(parent class).An inherited class is also called a subclass of its superclass(parent class).

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# Answer: No, because In object-oriented programming(OOP), we structure the code based on the concept of objects.Classes that have been instantiated in our code become objects that can interact with one another to perform the desired functions of the application.

# How in particular did Object Oriented Programming assist in the solving of this problem?
# Answer: The purpose of using OOP is to make our code reusable and flexible.
