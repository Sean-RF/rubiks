colors = ['wo','ow','wg','gw','wr','rw','wb','bw','go','og','gr','rg','br','rb','bo','ob','yo','oy','yg','gy','yr','ry','yb','by']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x']
import time

current_milli_time = lambda: int(round(time.time() * 1000))


class statTracker:
	def __init__(self, i):
		self.index = i
		self.correct = 0
		self.incorrect = 0
	def get_letter(self):
		return letters[self.index]
	def get_colors(self):
		return colors[self.index]
	def accuracy(self):
		if self.correct + self.incorrect == 0:
			return 'n/a'
		else:
			return self.correct/(self.correct + self.incorrect)
	def get_total(self):
		return self.correct + self.incorrect

stats = []
for i in range(len(letters)):
	stats.append(statTracker(i))


import random
low = int(input('bottom index?'))
high = int(input('top index?'))

def report():
	global letters, colors
	for i in range(low,high+1):
		print(str(stats[i].get_colors()) + " (" + str(stats[i].get_letter()) + "): " + str(stats[i].correct) + "/" + str(stats[i].get_total()))
	cont = input('continue? y/n, r to reverse\n')
	if cont == 'r':
		temp = letters
		letters = colors
		colors = temp
		return
	if cont == 'y':
		pass
	if cont == 'n':
		exit()

while(1):
	i = random.randint(low, high)
	print(colors[i])
	guess = input()
	if guess == '.':
		report()
		print(colors[i])
		guess = input()
	if guess == letters[i]:
		stats[i].correct += 1
		print('correct!')
	else:
		stats[i].incorrect += 1
		print('you suck!')
		while guess != letters[i]:
			print('try again')
			guess = input()
		print('finally...')
