import random
Scoring = 0
count = -1
correct = 0
engirish = ['Engirish', 'apple', 'kid', 'for', ]
while True:
	r = random.choice(engirish)
	while True:
		count += 1
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
print('總共答錯了', Scoring, '題', '正確率', correct / count * 100, '%')	