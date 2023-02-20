# -*- coding: utf-8 -*-
"""

@author: Radwa Abdelsalam
"""


from Creatures import Bear
from Creatures import Fish
from collections import deque
import random


class River:
    def __init__(self, n_rooms):
        self.n_rooms = deque(n_rooms)

# creates eco system based on creatures count
    def create_eco(self, Creature, count):
        eco = random.sample(range(len(self.n_rooms)), count)
        for position in eco:
            if self.n_rooms[position] is None:
                self.n_rooms[position] = Creature()

#checks if instance is Bear, populates if another Bear was found in the left of right cell. Movement is then randomly decided left or right.
    # Makes sure position is within deque range and bear then eats Fish if found and the bear's previous position takes value None.
    def move_bears(self):
        for position, creature in enumerate(self.n_rooms):
            if isinstance(creature, Bear):
                if position - 1 >= 0 and isinstance(self.n_rooms[position - 1], Bear):
                    self.create_eco(Bear, 1)
                elif position + 1 < len(self.n_rooms) and isinstance(self.n_rooms[position + 1], Bear):
                    self.create_eco(Bear, 1)
                else:
                    move_direction = random.choice([-1, 1])
                    new_position = position + move_direction
                    if new_position >= 0 and new_position < len(self.n_rooms):
                        if self.n_rooms[new_position] is None:
                            self.n_rooms[new_position] = creature
                            self.n_rooms[position] = None
                        elif isinstance(self.n_rooms[new_position], Fish):
                            self.n_rooms[position] = None

# checks if instance is Fish, populates if another Fish was found in the left of right cell. Movement is then randomly decided left or right.
# Makes sure position is within deque range. Fish is eaten if a bear was close in the new position and previous position takes the value None.
    def move_fish(self):
        for position, creature in enumerate(self.n_rooms):
            if isinstance(creature, Fish):
                if position - 1 >= 0 and isinstance(self.n_rooms[position - 1], Fish):
                    self.create_eco(Fish, 1)
                elif position + 1 < len(self.n_rooms) and isinstance(self.n_rooms[position + 1], Fish):
                    self.create_eco(Fish, 1)
                else:
                    move_direction = random.choice([-1, 1])
                    new_position = position + move_direction
                    if new_position >= 0 and new_position < len(self.n_rooms):
                        if self.n_rooms[new_position] is None:
                            self.n_rooms[new_position] = creature
                            self.n_rooms[position] = None
                        elif isinstance(self.n_rooms[new_position], Bear):
                            self.n_rooms[position] = None

    def display(self):
        print("- " + " - ".join(str(animal) if animal is not None else 'None ' for animal in self.n_rooms) + " -")