# -*- coding: utf-8 -*-
"""

@author: Radwa Abdelsalam
"""


from River import River
from Creatures import Bear
from Creatures import Fish
from collections import deque
import random

#eco system created is within the range of rooms and animals simulated.
# positions the fish based on the number of fish and the bears are allocated based on the positions left which do not include already allocated fish.
#both creatures' allocation is random
n_rooms = [None]*15
n_fish = 5
n_bears = 5
eco = random.sample(range(len(n_rooms)), n_fish+n_bears)
for position in eco[:n_fish]:
    n_rooms[position] = Fish()
for position in eco[n_fish:]:
    n_rooms[position] = Bear()

river = River(n_rooms)


for i in range(10):
    river.display()
    river.move_fish()
    river.move_bears()
    print("\n")