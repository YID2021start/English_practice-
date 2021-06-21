import random
Scoring = 0
count = -1
correct = 0
d = []
engirish = []#'Engirish', 'apple', 'kid', 'for'

with open('word.csv', 'r', encoding='utf-8') as f:
	for line in f:
		name, price, = line.strip().split(',')
		engirish.append([name, price,])
while True:
	t = random.choice(engirish)
	while True:
		r = t[0]
		c = t[1]
		count += 1
		print(c)
		print(r)
		type = input('請輸入英文單字:')
		if type == (r):
			correct += 1
			break
		elif type == ('q'):
			break	
		else :
			Scoring += 1	
	if type == ('q'):
		break
print('總共答題', count)
print('總共答錯了', Scoring, '題')
print('正確率', correct / count * 100, '%')