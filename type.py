import random
engirish = ['Engirish', 'apple', 'kid', 'for', ]
while True:
	r = random.choice(engirish)

	while True:
		print(r)
		type = input('請輸入英文單字:')
		if type == ('q'):
			break
		elif type == (r):
			break
	break