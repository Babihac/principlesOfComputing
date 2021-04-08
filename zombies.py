"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import user47_dWd4Ieo7g2_3 as poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        self.obstacle_list = obstacle_list
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
    def is_obst(self,row,col):
        return self._cells[row][col] == 5
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._human_list = []
        self._zombie_list = []
        poc_grid.Grid.clear(self)
            
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = poc_grid.Grid(20,20)
        distance_list = [[30*40 for i in range(20)]
                        for j in range(20)]
        boundary = poc_queue.Queue()
        if entity_type == HUMAN:
            for zombie in self.zombies():
                boundary.enqueue(zombie)
                visited.set_full(zombie[0], zombie[1])
                distance_list[zombie[0]][zombie[1]] = 0
            while len(boundary) > 0:
                zombie = boundary.dequeue()
                for n in self.four_neighbors(zombie[0],
                                           zombie[1]):
                    if visited.is_empty(n[0], n[1]) and self.is_empty(n[0],n[1]):
                        visited.set_full(n[0],n[1])
                        boundary.enqueue(n)
                        distance_list[n[0]][n[1]] = distance_list[zombie[0]][zombie[1]] +1
        elif entity_type == ZOMBIE:
            for human in self.humans():
                boundary.enqueue(human)
                visited.set_full(human[0], human[1])
                distance_list[human[0]][human[1]] = 0
            while len(boundary) > 0:
                human = boundary.dequeue()
                for n in self.four_neighbors(human[0],
                                           human[1]):
                    if visited.is_empty(n[0], n[1]) and self.is_empty(n[0],n[1]):
                        visited.set_full(n[0],n[1])
                        boundary.enqueue(n)
                        distance_list[n[0]][n[1]] = distance_list[human[0]][human[1]] +1
        print entity_type
        print distance_list
        return distance_list
    
    def move_zombies(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        update = []
        for human in self.humans():
            minimal_dist = zombie_distance_field[human[0]][human[1]]
            pos = human
            neigh = self.eight_neighbors(human[0], human[1])
            values = [zombie_distance_field[human[0]][human[1]]]
            for n in neigh:
                if zombie_distance_field[n[0]][n[1]] > minimal_dist and self.is_empty(n[0],n[1]):
                    minimal_dist = zombie_distance_field[n[0]][n[1]]
                    pos = n
            update.append(pos)
        self._human_list = update
          
            
    
    def move_humans(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        update = []
        for zombie in self.zombies():
            minimal_dist = human_distance_field[zombie[0]][zombie[1]] 
            pos = zombie
            neigh = self.four_neighbors(zombie[0], zombie[1])
            values = [human_distance_field[zombie[0]][zombie[1]]]
            for n in neigh:
                if human_distance_field[n[0]][n[1]] < minimal_dist and self.is_empty(n[0],n[1]):
                    minimal_dist = human_distance_field[n[0]][n[1]]
                    pos = n
            update.append(pos)
        self._zombie_list = update

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(20, 20,None,[(0,0)], [(1,1)]))

