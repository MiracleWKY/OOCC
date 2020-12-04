import tkinter as tk  
import os
import numpy as np
from PIL import Image, ImageTk
import copy
import time

class piece:
	def __init__(self, img, x_index, y_index, red, value):
		self.img = img
		self.pos_x = x_index
		self.pos_y = y_index
		self.vitality = True
		self.value = value
		self.red = red

	def move(self, pieces, x2, y2, copy):
		if copy:

			temp = []
			for piece in pieces: 

				if type(piece) == type(king(None, None, None, None)):

					temp.append(king(None, piece.pos_x, piece.pos_y, piece.red))

				elif type(piece) == type(rook(None, None, None, None)):

					temp.append(rook(None, piece.pos_x, piece.pos_y, piece.red))

				elif type(piece) == type(knight(None, None, None, None)):

					temp.append(knight(None, piece.pos_x, piece.pos_y, piece.red))

				elif type(piece) == type(bishop(None, None, None, None)):

					temp.append(bishop(None, piece.pos_x, piece.pos_y, piece.red))

				elif type(piece) == type(advisor(None, None, None, None)):

					temp.append(advisor(None, piece.pos_x, piece.pos_y, piece.red))

				elif type(piece) == type(cannon(None, None, None, None)):

					temp.append(cannon(None, piece.pos_x, piece.pos_y, piece.red))

				elif type(piece) == type(pawn(None, None, None, None)):

					temp.append(pawn(None, piece.pos_x, piece.pos_y, piece.red))


			pieces = temp




		for piece in pieces: 
			if piece.pos_x == x2 and piece.pos_y == y2:
				pieces.remove(piece)
		for piece in pieces:
			if piece.pos_x == self.pos_x and piece.pos_y == self.pos_y:
				piece.pos_x = x2
				piece.pos_y = y2
		return pieces

class king(piece):
	def __init__(self, img, x_index, y_index, red):
		super().__init__(img, x_index, y_index, red, value = 10000)
	# def move(self, x2, y2):

	# 	if abs(self.pos_x - x2) + abs(self.pos_y - y2) == 1 and 3 <= x2 and x2 <= 5:

	# 		if self.red and 7 <= y2 and y2 <= 9:
	# 			self.pos_x = x2
	# 			self.pos_y = y2
	# 			return 1
	# 		if not self.red and 0 <= y2 and y2 <= 2:
	# 			self.pos_x = x2
	# 			self.pos_y = y2
	# 			return 1
	# 	return 0
	def possible_moves(self, pieces):
		moves = []
		if self.red:
			for i in range(3,6):
				for j in range(7,10):
					if abs(self.pos_x - i) + abs(self.pos_y - j) == 1 and not any((k.red and k.pos_x == i and k.pos_y == j) or (not k.red and type(k) == type(self) and k.pos_x == i and not any(l.pos_x == i and l.pos_y > k.pos_y and l.pos_y < j for l in pieces)) for k in pieces):
						moves.append([i,j])
		else:
			for i in range(3,6):
				for j in range(0,3):
					if abs(self.pos_x - i) + abs(self.pos_y - j) == 1 and not any((not k.red and k.pos_x == i and k.pos_y == j) or (k.red and type(k) == type(self) and k.pos_x == i and not any(l.pos_x == i and l.pos_y < k.pos_y and l.pos_y > j for l in pieces)) for k in pieces):
						moves.append([i,j])
		return moves


class rook(piece):
	def __init__(self, img, x_index, y_index, red):
		super().__init__(img, x_index, y_index, red, value = 10)
	# def move(self, x2, y2):
	# 	if self.pos_x == x2 or self.pos_y == y2:
	# 		self.pos_x = x2
	# 		self.pos_y = y2
	# 		return 1
	# 	return 0
	def possible_moves(self, pieces):
		moves = []
		i = self.pos_x
		j = self.pos_y
		i = i + 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])
			i = i + 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.red == self.red and k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])
		i = self.pos_x
		j = self.pos_y
		i = i - 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])
			i = i - 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.red == self.red and k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])

		i = self.pos_x
		j = self.pos_y
		j = j + 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])
			j = j + 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.red == self.red and k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])
		i = self.pos_x
		j = self.pos_y
		j = j - 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])
			j = j - 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.red == self.red and k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])

		return moves


class knight(piece):
	def __init__(self, img, x_index, y_index, red):
		super().__init__(img, x_index, y_index, red, value = 4)
	# def move(self, x2, y2):
	# 	if abs(self.pos_x - x2) + abs(self.pos_y - y2) == 3 and abs(self.pos_x - x2)**2 + abs(self.pos_y - y2)**2 == 5:
	# 		self.pos_x = x2
	# 		self.pos_y = y2
	# 		return 1
	# 	return 0
	def possible_moves(self, pieces):
		moves = []
		points = []
		if not any(self.pos_x == k.pos_x and self.pos_y-1 == k.pos_y for k in pieces):
			points.append([self.pos_x+1, self.pos_y-2])
			points.append([self.pos_x-1, self.pos_y-2])
		if not any(self.pos_x == k.pos_x and self.pos_y+1 == k.pos_y for k in pieces):
			points.append([self.pos_x+1, self.pos_y+2])
			points.append([self.pos_x-1, self.pos_y+2])
		if not any(self.pos_x+1 == k.pos_x and self.pos_y == k.pos_y for k in pieces):
			points.append([self.pos_x+2, self.pos_y+1])
			points.append([self.pos_x+2, self.pos_y-1])
		if not any(self.pos_x-1 == k.pos_x and self.pos_y == k.pos_y for k in pieces):
			points.append([self.pos_x-2, self.pos_y+1])
			points.append([self.pos_x-2, self.pos_y-1])
		for i in points:
			if i[0] >= 0 and i[0] <= 8 and i[1] >= 0 and i[1] <= 9 and not any(self.red == k.red and i[0] == k.pos_x and i[1] == k.pos_y for k in pieces):
				moves.append(i)
		return moves


class bishop(piece):
	def __init__(self, img, x_index, y_index, red):
		super().__init__(img, x_index, y_index, red, value = 3)
	# def move(self, x2, y2):
	# 	if abs(self.pos_x - x2) + abs(self.pos_y - y2) == 4 and abs(self.pos_x - x2)**2 + abs(self.pos_y - y2)**2 == 8:
	# 		self.pos_x = x2
	# 		self.pos_y = y2
	# 		return 1
	# 	return 0
	def possible_moves(self, pieces):
		moves = []
		points = []
		if not any(self.pos_x-1 == k.pos_x and self.pos_y-1 == k.pos_y for k in pieces):
			points.append([self.pos_x-2, self.pos_y-2])
		if not any(self.pos_x-1 == k.pos_x and self.pos_y+1 == k.pos_y for k in pieces):
			points.append([self.pos_x-2, self.pos_y+2])
		if not any(self.pos_x+1 == k.pos_x and self.pos_y-1 == k.pos_y for k in pieces):
			points.append([self.pos_x+2, self.pos_y-2])
		if not any(self.pos_x+1 == k.pos_x and self.pos_y+1 == k.pos_y for k in pieces):
			points.append([self.pos_x+2, self.pos_y+2])
		for i in points:
			if not self.red and i[0] >= 0 and i[0] <= 8 and i[1] >= 0 and i[1] <= 4 and not any(self.red == k.red and i[0] == k.pos_x and i[1] == k.pos_y for k in pieces):
				moves.append(i)
			if self.red and i[0] >= 0 and i[0] <= 8 and i[1] >= 5 and i[1] <= 9 and not any(self.red == k.red and i[0] == k.pos_x and i[1] == k.pos_y for k in pieces):
				moves.append(i)
		return moves


class advisor(piece):
	def __init__(self, img, x_index, y_index, red):
		super().__init__(img, x_index, y_index, red, value = 2)



	# def move(self, x2, y2):
	# 	if abs(self.pos_x - x2) + abs(self.pos_y - y2) == 2 and abs(self.pos_x - x2)**2 + abs(self.pos_y - y2)**2 == 2 and 3 <= x2 and x2 <= 5:
	# 		if self.red and 7 <= y2 and y2 <= 9:
	# 			self.pos_x = x2
	# 			self.pos_y = y2
	# 			return 1
	# 		if not self.red and 0 <= y2 and y2 <= 2:
	# 			self.pos_x = x2
	# 			self.pos_y = y2
	# 			return 1
	#	return 0
	def possible_moves(self, pieces):
		moves = []
		if self.red:
			for i in range(3,6):
				for j in range(7, 10):
					if abs(self.pos_x - i) + abs(self.pos_y - j) == 2 and abs(self.pos_x - i)**2 + abs(self.pos_y - j)**2 == 2 and not any(self.red == k.red and i == k.pos_x and j == k.pos_y for k in pieces):
						moves.append([i,j])
		else:
			for i in range(3,6):
				for j in range(0, 3):
					if abs(self.pos_x - i) + abs(self.pos_y - j) == 2 and abs(self.pos_x - i)**2 + abs(self.pos_y - j)**2 == 2 and not any(self.red == k.red and i == k.pos_x and j == k.pos_y for k in pieces):
						moves.append([i,j])
		return moves


class cannon(piece):
	def __init__(self, img, x_index, y_index, red):
		super().__init__(img, x_index, y_index, red, value = 5)
	# def move(self, x2, y2):
	# 	if self.pos_x == x2 or self.pos_y == y2:
	# 		self.pos_x = x2
	# 		self.pos_y = y2
	# 		return 1
	# 	return 0
	def possible_moves(self, pieces):
		moves = []

		i = self.pos_x
		j = self.pos_y
		i = i + 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])
			i = i + 1
		i = self.pos_x
		j = self.pos_y
		i = i - 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])
			i = i - 1

		i = self.pos_x
		j = self.pos_y
		j = j + 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])
			j = j + 1
		i = self.pos_x
		j = self.pos_y
		j = j - 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])
			j = j - 1

		#-----------------------------

		i = self.pos_x
		j = self.pos_y
		i = i + 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			i = i + 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and any(k.pos_x == i and k.pos_y == j for k in pieces)):
			i = i + 1
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			i = i + 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and any(k.red != self.red and k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])

		i = self.pos_x
		j = self.pos_y
		i = i - 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			i = i - 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and any(k.pos_x == i and k.pos_y == j for k in pieces)):
			i = i - 1
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			i = i - 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and any(k.red != self.red and k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])

		i = self.pos_x
		j = self.pos_y
		j = j + 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			j = j + 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and any(k.pos_x == i and k.pos_y == j for k in pieces)):
			j = j + 1
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			j = j + 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and any(k.red != self.red and k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])

		i = self.pos_x
		j = self.pos_y
		j = j - 1;
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			j = j - 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and any(k.pos_x == i and k.pos_y == j for k in pieces)):
			j = j - 1
		while(i >= 0 and i <= 8 and j >= 0 and j <= 9 and not any(k.pos_x == i and k.pos_y == j for k in pieces)):
			j = j - 1
		if(i >= 0 and i <= 8 and j >= 0 and j <= 9 and any(k.red != self.red and k.pos_x == i and k.pos_y == j for k in pieces)):
			moves.append([i,j])



		return moves


class pawn(piece):
	def __init__(self, img, x_index, y_index, red):
		super().__init__(img, x_index, y_index, red, value = 1)
	# def move(self, x2, y2):
	# 	if self.red:
	# 		if self.pos_y <= 4:
	# 			if abs(self.pos_x - x2) + abs(self.pos_y - y2) == 1 and self.pos_y >= y2:
	# 				self.pos_x = x2
	# 				self.pos_y = y2
	# 				return 1
	# 		else:
	# 			if self.pos_y - y2 == 1 and self.pos_x == x2:
	# 				self.pos_x = x2
	# 				self.pos_y = y2
	# 				return 1
	# 	else:
	# 		if self.pos_y >= 5:
	# 			if abs(self.pos_x - x2) + abs(self.pos_y - y2) == 1 and self.pos_y <= y2:
	# 				self.pos_x = x2
	# 				self.pos_y = y2
	# 				return 1
	# 		else:
	# 			if self.pos_y - y2 == -1 and self.pos_x == x2:
	# 				self.pos_x = x2
	# 				self.pos_y = y2
	# 				return 1
	# 	return 0
	def possible_moves(self, pieces):
		moves = []
		if self.red:
			if self.pos_y <= 4:
				if self.pos_x-1 >= 0 and self.pos_x-1 <= 8 and self.pos_y >= 0 and self.pos_y <= 9 and not any(k.red == self.red and k.pos_x == self.pos_x-1 and k.pos_y == self.pos_y for k in pieces):
					moves.append([self.pos_x - 1, self.pos_y])
				if self.pos_x+1 >= 0 and self.pos_x+1 <= 8 and self.pos_y >= 0 and self.pos_y <= 9 and not any(k.red == self.red and k.pos_x == self.pos_x+1 and k.pos_y == self.pos_y for k in pieces):
					moves.append([self.pos_x + 1, self.pos_y])
				if self.pos_x >= 0 and self.pos_x <= 8 and self.pos_y-1 >= 0 and self.pos_y-1 <= 9 and not any(k.red == self.red and k.pos_x == self.pos_x and k.pos_y == self.pos_y - 1 for k in pieces):
					moves.append([self.pos_x, self.pos_y - 1])
			else:
				if self.pos_x >= 0 and self.pos_x <= 8 and self.pos_y-1 >= 0 and self.pos_y-1 <= 9 and not any(k.red == self.red and k.pos_x == self.pos_x and k.pos_y == self.pos_y-1 for k in pieces):
					moves.append([self.pos_x, self.pos_y - 1])
		else:
			if self.pos_y >= 5:
				if self.pos_x-1 >= 0 and self.pos_x-1 <= 8 and self.pos_y >= 0 and self.pos_y <= 9 and not any(k.red == self.red and k.pos_x == self.pos_x-1 and k.pos_y == self.pos_y for k in pieces):
					moves.append([self.pos_x - 1, self.pos_y])
				if self.pos_x+1 >= 0 and self.pos_x+1 <= 8 and self.pos_y >= 0 and self.pos_y <= 9 and not any(k.red == self.red and k.pos_x == self.pos_x+1 and k.pos_y == self.pos_y for k in pieces):
					moves.append([self.pos_x + 1, self.pos_y])
				if self.pos_x >= 0 and self.pos_x <= 8 and self.pos_y+1 >= 0 and self.pos_y+1 <= 9 and not any(k.red == self.red and k.pos_x == self.pos_x and k.pos_y == self.pos_y + 1 for k in pieces):
					moves.append([self.pos_x, self.pos_y + 1])
			else:
				if self.pos_x >= 0 and self.pos_x <= 8 and self.pos_y+1 >= 0 and self.pos_y+1 <= 9 and not any(k.red == self.red and k.pos_x == self.pos_x and k.pos_y == self.pos_y + 1 for k in pieces):
					moves.append([self.pos_x, self.pos_y + 1])
		return moves

#------------------------------

#factory pattern

#------------------------------
class factory:  
	def __init__(self, imgs):
		self.imgs = imgs
		self.pieces = []
	def initialize(self):

		#black:

		self.pieces.append(rook(self.imgs["BR"], 0, 0, False))
		self.pieces.append(knight(self.imgs["BN"], 1, 0, False))
		self.pieces.append(bishop(self.imgs["BB"], 2, 0, False))
		self.pieces.append(advisor(self.imgs["BA"], 3, 0, False))
		self.pieces.append(king(self.imgs["BK"], 4, 0, False))
		self.pieces.append(advisor(self.imgs["BA"], 5, 0, False))
		self.pieces.append(bishop(self.imgs["BB"], 6, 0, False))
		self.pieces.append(knight(self.imgs["BN"], 7, 0, False))
		self.pieces.append(rook(self.imgs["BR"], 8, 0, False))

		self.pieces.append(cannon(self.imgs["BC"], 1, 2, False))
		self.pieces.append(cannon(self.imgs["BC"], 7, 2, False))

		self.pieces.append(pawn(self.imgs["BP"], 0, 3, False))
		self.pieces.append(pawn(self.imgs["BP"], 2, 3, False))
		self.pieces.append(pawn(self.imgs["BP"], 4, 3, False))
		self.pieces.append(pawn(self.imgs["BP"], 6, 3, False))
		self.pieces.append(pawn(self.imgs["BP"], 8, 3, False))

		#red:

		self.pieces.append(rook(self.imgs["RR"], 0, 9, True))
		self.pieces.append(knight(self.imgs["RN"], 1, 9, True))
		self.pieces.append(bishop(self.imgs["RB"], 2, 9, True))
		self.pieces.append(advisor(self.imgs["RA"], 3, 9, True))
		self.pieces.append(king(self.imgs["RK"], 4, 9, True))
		self.pieces.append(advisor(self.imgs["RA"], 5, 9, True))
		self.pieces.append(bishop(self.imgs["RB"], 6, 9, True))
		self.pieces.append(knight(self.imgs["RN"], 7, 9, True))
		self.pieces.append(rook(self.imgs["RR"], 8, 9, True))

		self.pieces.append(cannon(self.imgs["RC"], 1, 7, True))
		self.pieces.append(cannon(self.imgs["RC"], 7, 7, True))

		self.pieces.append(pawn(self.imgs["RP"], 0, 6, True))
		self.pieces.append(pawn(self.imgs["RP"], 2, 6, True))
		self.pieces.append(pawn(self.imgs["RP"], 4, 6, True))
		self.pieces.append(pawn(self.imgs["RP"], 6, 6, True))
		self.pieces.append(pawn(self.imgs["RP"], 8, 6, True))


class indicator_factory:
	def __init__(self, img):
		self.img = img
	def initialize(self, coordinates):
		indicators = []
		for [x,y] in coordinates:
			indicators.append(piece(self.img, x, y, None, 0))
		return indicators

#------------------------------

#observer/announcer pattern

#------------------------------
class visualizer:
	def __init__(self, size, x, y):
		self.size  = size
		self.x = x
		self.y = y
		self.selector = None
		self.imgs = []
		self.in_imgs = []

	def visualize(self, pieces):
		for i in pieces:
			self.imgs.append(canvas.create_image(self.x[i.pos_x]-(self.size/2), self.y[i.pos_y]-(self.size/2), anchor='nw',image=i.img))
		return 1
	def delete_pieces(self):
		for i in self.imgs:
			canvas.delete(i)


	def visualize_selector(self, selector):
		self.selector = canvas.create_image(self.x[selector.pos_x]-(self.size/2), self.y[selector.pos_y]-(self.size/2), anchor='nw',image=selector.img)
	def delete_selector(self):
		canvas.delete(self.selector)


	def visualize_indicator(self, indicators):
		for i in indicators:
			self.in_imgs.append((canvas.create_image(self.x[i.pos_x]-(self.size/2), self.y[i.pos_y]-(self.size/2), anchor='nw',image=i.img)))
	def delete_indicators(self):
		for i in self.in_imgs:
			canvas.delete(i)


class selector:
	def __init__(self, size, x, y, img):
		self.size  = size
		self.x = x
		self.y = y
		self.img = img
		self.pos_x = 0
		self.pos_y = 0
	def select(self, pieces, x0, y0):
		for i in range(len(self.x)):
			for j in range(len(self.y)):
				if (self.x[i] - x0)**2 + (self.y[j] - y0)**2 < (size/2)**2:
					self.pos_x = i
					self.pos_y = j
					return i,j
		return -1,-1

#------------------------------

#object pool pattern

#------------------------------
class judge:
	def __init__(self, pieces):
		self.pieces = pieces
	def move(self, x1, y1, x2, y2):
		if x1 == -1 or y1 == -1 or x2 == -1 or y2 == -1:
			return 0
		for piece in self.pieces:
			if piece.pos_x == x1 and piece.pos_y == y1:
				if [x2,y2] in piece.possible_moves(self.pieces):
					self.pieces = piece.move(self.pieces, x2,y2, False)
					return 1
		return 0
	def get_piece(self, x1, y1):
		for piece in self.pieces:
			if piece.pos_x == x1 and piece.pos_y == y1:
				return piece
		return None


class mystupidfuckartificalintelligence:
	def __init__(self, depth):
		self.depth = depth
	def get_difference(self, pieces):
		score_black = 0
		score_red = 0 
		for piece in pieces:
			if piece.red:
				score_red += piece.value
			else:
				score_black += piece.value
		return score_black - score_red

	def min_score(self, pieces, d, alpha, beta):
		d = d + 1
		#print(d)
		if d > self.depth:
			return self.get_difference(pieces)
		

		min_score = np.infty
		br = False
		for piece in pieces:

			if piece.red == True:
				
				for [x,y] in piece.possible_moves(pieces):
					temp = self.max_score(piece.move(pieces, x, y, True), d, alpha, beta)
					min_score = min(temp, min_score)
					beta = min(temp, beta)
					if beta <= alpha:
						br = True
						break;
			if br:
				break;
		return min_score

	def max_score(self, pieces, d, alpha, beta):
		d = d + 1
		#print(d)
		if d > self.depth:
			return self.get_difference(pieces)


		max_score = -np.infty
		br = False
		for piece in pieces:
			if piece.red == False:
				for [x,y] in piece.possible_moves(pieces):
					temp = self.min_score(piece.move(pieces, x, y, True), d, alpha, beta)
					max_score = max(temp, max_score)
					alpha = max(temp, alpha)
					if beta <= alpha:
						br = True
						break;
			if br:
				break;


		return max_score


	def alpha_beta_pruning(self, pieces):
		alpha = -np.infty
		beta = np.infty
		max_ = -np.infty
		p = None
		x_move, y_move = 0, 0
		for piece in pieces:
			if piece.red == False:
				for [x,y] in piece.possible_moves(pieces):
					score = self.min_score(piece.move(pieces,x,y,True), 0, alpha, beta)
					#print(score)
					if score > max_:
						max_ = score
						p = piece
						x_move = x
						y_move = y
					alpha = max(alpha, score)
		return p.move(pieces, x_move, y_move, False)


def read_images(s):
	piece_imgs = {}
	size = s

	piece_img = Image.open(cwd +'/pieces/BA.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["BA"] = piece_img

	piece_img = Image.open(cwd +'/pieces/BB.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["BB"] = piece_img

	piece_img = Image.open(cwd +'/pieces/BC.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["BC"] = piece_img

	piece_img = Image.open(cwd +'/pieces/BK.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["BK"] = piece_img

	piece_img = Image.open(cwd +'/pieces/BN.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["BN"] = piece_img

	piece_img = Image.open(cwd +'/pieces/BP.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["BP"] = piece_img

	piece_img = Image.open(cwd +'/pieces/BR.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["BR"] = piece_img


	piece_img = Image.open(cwd +'/pieces/RA.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["RA"] = piece_img

	piece_img = Image.open(cwd +'/pieces/RB.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["RB"] = piece_img

	piece_img = Image.open(cwd +'/pieces/RC.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["RC"] = piece_img

	piece_img = Image.open(cwd +'/pieces/RK.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["RK"] = piece_img

	piece_img = Image.open(cwd +'/pieces/RN.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["RN"] = piece_img

	piece_img = Image.open(cwd +'/pieces/RP.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["RP"] = piece_img

	piece_img = Image.open(cwd +'/pieces/RR.GIF')
	piece_img = piece_img.resize((size,size),Image.NEAREST)
	piece_img = ImageTk.PhotoImage(piece_img)

	piece_imgs["RR"] = piece_img
	return piece_imgs


def read_selector(s):
	selector_img = Image.open(cwd +'/pieces/OOS.GIF')
	selector_img = selector_img.resize((size,size),Image.NEAREST)
	selector_img = ImageTk.PhotoImage(selector_img)
	return selector_img


def read_indicator(s):
	in_img = Image.open(cwd +'/pieces/OOS2.GIF')
	in_img = in_img.resize((size,size),Image.NEAREST)
	in_img = ImageTk.PhotoImage(in_img)
	return in_img



cwd = os.getcwd()

print(cwd)

x = np.linspace(69, 732, 9)
y = np.linspace(73, 830, 10)


window = tk.Tk()
window.resizable(False, False) 
window.title('My Window')
 

canvas = tk.Canvas(window, bg='green', width=800, height=900)

img = Image.open(cwd +'/board.gif')
img = img.resize((800,900),Image.NEAREST)
image_file = ImageTk.PhotoImage(img)


image = canvas.create_image(0, 0, anchor='nw',image=image_file)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处

size = 75

piece_imgs = read_images(size)
in_img = read_indicator(size)

# BK = king(piece_imgs["BB"], 4, 0)
# canvas.create_image(x[BK.pos_x]-(size/2), y[BK.pos_y]-(size/2), anchor='nw',image=BK.img) 
canvas.pack()



fact = factory(piece_imgs)
in_fact = indicator_factory(in_img)
fact.initialize()
v = visualizer(size, x, y)
pieces = fact.pieces



selector_img = read_selector(size)
s = selector(size, x, y, selector_img)

x0,y0 = 0, 0


x1 = -1

y1 = -1

x2 = -1

y2 = -1

judge = judge(pieces) 

v.visualize(judge.pieces)

#test = copy.deepcopy(judge.pieces[0])
#print(test)



AI = mystupidfuckartificalintelligence(3)
print([i for i in range(10)])

def getorigin(eventorigin):

	x0 = eventorigin.x
	y0 = eventorigin.y
	global x1
	global y1 
	global x2 
	global y2 
	print(x0,y0)
	v.delete_selector()

	v.delete_indicators()

	x1, y1 = x2, y2
	x2, y2 = s.select(judge.pieces, x0, y0)


	print(x1, y1, x2, y2)
	selected_piece = judge.get_piece(x2,y2)



	#test = copy.deepcopy(judge.pieces[0])

	v.visualize_selector(s)
	print(type(selected_piece) == type(king(None, None, None, None)))
	if(selected_piece):
		coords = selected_piece.possible_moves(judge.pieces)

		v.visualize_indicator(in_fact.initialize(coords))


	if(judge.move(x1,y1,x2,y2)):

		print("asdfag")
		
		v.delete_selector()
		v.delete_indicators()
		v.delete_pieces()
		v.visualize(judge.pieces)
		
		x1, y1 = -1, -1
		x2, y2 = -1, -1
		judge.pieces = AI.alpha_beta_pruning(judge.pieces)
		v.delete_pieces()
		v.visualize(judge.pieces)

		print(len(judge.pieces))

		if(len(judge.pieces)<20):
			AI.depth = 5






    
#mouseclick event


canvas.bind("<Button 1>",getorigin)









window.mainloop()