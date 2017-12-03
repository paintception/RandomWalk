import time
import seaborn
import random

import numpy as np 

from matplotlib import pyplot as plt 


class RandomWalker(object):
	def __init__(self):
		self.width = 10
		self.height = 10
		self.n_walkers = 1
		self.probability_threshold = 0.5
		self.time_stamps = 10

	def probability_decisioner(self):
		return random.random() < self.probability_threshold

	def create_2D_space(self):
		return[None, None]
		
	def create_x_start(self):
		return random.randint(0, self.width)

	def create_y_start(self):
		return random.randint(0, self.height)	

	def get_direction(self):
		return random.randint(0,3)

	def go_left(self, initial_space):
		initial_space[0] = initial_space[0] - 1
		return initial_space

	def go_right(self, initial_space):
		initial_space[0] = initial_space[0] + 1
		return initial_space

	def go_up(self, initial_space):
		initial_space[1] = initial_space[1] + 1
		return initial_space

	def go_down(self, initial_space):
		initial_space[1] = initial_space[1] - 1
		return initial_space

	def define_goal(self):
		return random.randint(0, self.width)

	def run_simulation(self, initial_space):

		for time_stamp in xrange(0, self.time_stamps):
			direction = self.get_direction()

			if direction == 0:
				initial_space = self.go_left(initial_space)
				
			elif direction == 1:
				initial_space = self.go_right(initial_space)
				
			elif direction == 2:
				initial_space = self.go_down(initial_space)
				
			elif direction == 3:
				initial_space = self.go_up(initial_space)

	def main(self):		
		
		initial_space = self.create_2D_space()
		x_start = self.create_x_start()
		y_start = self.create_y_start()
		initial_space[0] = x_start
		initial_space[1] = y_start
		
		self.run_simulation(initial_space)		

if __name__ == '__main__':
	walker = RandomWalker()
	walker.main()