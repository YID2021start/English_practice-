#匯入題目
def read_file(filename):
    engirish = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            name, price, = line.strip().split(',')
            engirish.append([name, price,])
    return engirish        
#練習題目
def topic(engirish):
    i = []
    scoring = 0
    count = -1
    correct = 0
    import random        
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
                scoring += 1  
        if type == ('q'):
            break
    i.append([scoring, count, correct,])    
    return i  

def main():
    engirish = read_file('word.csv')
    i = topic(engirish)    
    print('總共答題', i[0][1])
    print('總共答錯了', i[0][0], '題')
    print('正確率', i[0][2] / i[0][1] * 100, '%')
if __name__ == '__main__':
    	main()    