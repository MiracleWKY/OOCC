import tkinter as tk  
import os
import numpy as np
from PIL import Image, ImageTk


class piece:
	def __init__(self, img, x_index, y_index, red, value):
		self.img = img
		self.pos_x = x_index
		self.pos_y = y_index
		self.vitality = True
		self.value = value
		self.red = red
	def remove():
		self.vitality = False

class king(piece):
	def __init__(self, img, x_index, y_index, red):
		super().__init__(img, x_index, y_index, red, value = np.infty)
	def move(self, x2, y2):

		if abs(self.pos_x - x2) + abs(self.pos_y - y2) == 1 and 3 <= x2 and x2 <= 5:

			if self.red and 7 <= y2 and y2 <= 9:
				print("called")
				self.pos_x = x2
				self.pos_y = y2
				return 1
			if not self.red and 0 <= y2 and y2 <= 2:
				self.pos_x = x2
				self.pos_y = y2
				return 1
		return 0


class rook(piece):
  def __init__(self, img, x_index, y_index, red):
    super().__init__(img, x_index, y_index, red, value = 10)

class knight(piece):
  def __init__(self, img, x_index, y_index, red):
    super().__init__(img, x_index, y_index, red, value = 4)

class bishop(piece):
  def __init__(self, img, x_index, y_index, red):
    super().__init__(img, x_index, y_index, red, value = 3)

class advisor(piece):
  def __init__(self, img, x_index, y_index, red):
    super().__init__(img, x_index, y_index, red, value = 2)

class cannon(piece):
  def __init__(self, img, x_index, y_index, red):
    super().__init__(img, x_index, y_index, red, value = 5)

class pawn(piece):
  def __init__(self, img, x_index, y_index, red):
    super().__init__(img, x_index, y_index, red, value = 1)


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



class visualizer:
	def __init__(self, size, x, y):
		self.size  = size
		self.x = x
		self.y = y
		self.selector = None
		self.imgs = []
	def visualize(self, pieces):
		for i in pieces:
			self.imgs.append(canvas.create_image(self.x[i.pos_x]-(self.size/2), self.y[i.pos_y]-(self.size/2), anchor='nw',image=i.img))

	def visualize_selector(self, selector):
		self.selector = canvas.create_image(self.x[selector.pos_x]-(self.size/2), self.y[selector.pos_y]-(self.size/2), anchor='nw',image=selector.img)
	def delete_selector(self):
		canvas.delete(self.selector)
	def delete_pieces(self):
		for i in self.imgs:
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

class judge:
	def __init__(self, pieces):
		self.pieces = pieces
	def move(self, x1, y1, x2, y2):
		if x1 == -1 or y1 == -1 or x2 == -1 or y2 == -1:
			return 0
		for piece in self.pieces:
			if piece.pos_x == x1 and piece.pos_y == y1:
				return piece.move(x2,y2)




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



cwd = os.getcwd()

print(cwd)

x = np.linspace(69, 732, 9)
y = np.linspace(73, 830, 10)
print(y)


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

# BK = king(piece_imgs["BB"], 4, 0)
# canvas.create_image(x[BK.pos_x]-(size/2), y[BK.pos_y]-(size/2), anchor='nw',image=BK.img) 
canvas.pack()

fact = factory(piece_imgs)
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



def getorigin(eventorigin):

    x0 = eventorigin.x
    y0 = eventorigin.y
    global x1
    global y1 
    global x2 
    global y2 
    print(x0,y0)
    v.delete_selector()
    x1, y1 = x2, y2
    x2, y2 = s.select(judge.pieces, x0, y0)

    print(x1, y1, x2, y2)
    if(judge.move(x1,y1,x2,y2)):
    	print("asdfag")
    	v.delete_pieces()
    	v.visualize(judge.pieces)
    	x1, y1 = -1, -1
    	x2, y2 = -1, -1
    v.visualize_selector(s)
    
#mouseclick event


canvas.bind("<Button 1>",getorigin)









window.mainloop()