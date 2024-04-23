import random

def guess_num(max_num:int):
    print(f'guess number between 0 and {max_num}')
    target_num=random.randint(0,max_num)
    total_times=0
    while True:
        total_times+=1
        input_num=int(input('Please input your number:'))
        if(input_num==target_num):
            print(f'Congratulations! you guess the right number:{target_num}')
            print(f'Total guess times:{total_times}')
            break
        elif input_num>target_num:
            print(f'{input_num} is hgih')
        else:
            print(f'{input_num} is low')

if(__name__=='__main__'):
    guess_num(100)
    guess_num(1000)
    guess_num(10000)
        
            
        