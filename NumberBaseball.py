import numpy as np
import pandas as pd
from tabulate import tabulate
import random
import time

class Numbers:
    def __init__(self, num, place_value):
        self.num = num
        self.place_value = place_value
    
    def __add__(self, other):
        return self.place_value*self.num + other.place_value*other.num
    
    def __str__(self):
        return "%d의 자리 수 값: %d" % (self.place_value, self.num)
    
    def real_value(self):
        return self.place_value*self.num


answer_cand = []
com_trial = 1
usr_trial = 1


# 경기 종료 시 0을 반환. 아니면 1 반환.
def usr_guess():
    global com_answer
    global usr_trial
    guess = int(input("-"*100+"\n사용자의 "+str(usr_trial)+"번째 유추입니다. 유추할 숫자를 입력하세요.\n"))
    usr_trial += 1
    if guess>=1000 and guess<=9999:
        thou, hund, ten, one = object_generator(guess)
        if redundancy_check(thou.num, hund.num, ten.num, one.num) == 0:
            sbo = judge_SBO(guess, com_answer)
        else:
            raise ValueError("잘못된 입력입니다.")
    else:
        raise ValueError("잘못된 입력입니다.")
    
    print("\n유추 결과는 "+str(sbo[0])+" Strike "+str(sbo[1])+" Ball 입니다.\n")
    if sbo[0] == 4:
        print("\n사용자가 승리하였습니다. 축하드립니다.\n")
        return 0
    else:
        return 1


# 컴퓨터가 유추을 한다.
def com_guess():
    global answer_cand
    global com_trial
    global com_answer
    guess_index = random.randrange(len(answer_cand))
    print("-"*100+"\n컴퓨터가 유추 중입니다. 잠시만 기다려주십시오...\n")
    time.sleep(1)
    print("\n컴퓨터의 "+str(com_trial)+"번째 유추: "+str(answer_cand[guess_index]))
    com_trial += 1

    strike = int(input("\nStrike(스트라이크)의 개수를 입력 후 Enter 키를 누르세요. Strike가 없거나 OUT(아웃)이라면 '0'을 입력합니다. (ex: 1S1B이면 '1'을 입력.)\n"))
    if strike == 4:
        print("\n컴퓨터가 정답을 구하였습니다. 답은 "+str(answer_cand[guess_index])+"입니다. "+str(com_trial)+"번 만에 맞추었습니다. 프로그램을 종료합니다.\n")
        print("컴퓨터의 답: ", com_answer)
        return 0
    
    ball = int(input("\nBall(볼)의 개수를 입력 후 Enter 키를 누르세요. OUT(아웃)이라면 '0'을 입력합니다. (ex: 1S2B이면 '2'를 입력.)\n"))
    
    print("\n컴퓨터가 계산 중입니다. 잠시만 기다려 주십시오...\n")
    time.sleep(0.5)
    
    temp_list = []
    guess_sbo = (strike, ball)
    for i, num in enumerate(answer_cand):
        sbo = judge_SBO(num, answer_cand[guess_index])
        if guess_sbo == sbo:
            temp_list.append(num)
        else:
            continue
    answer_cand = temp_list
    print("컴퓨터는 후보 정답을 ", len(temp_list), "개로 추려내었습니다!")
    
    if len(answer_cand) == 1:
        print("\n컴퓨터가 정답을 다음에 구할 것 같습니다...!\n")
        status = 1
    elif len(answer_cand) == 0:
        print("\n중간 과정에서 사용자가 Strike와 Ball의 개수를 잘못입력하셨습니다. 컴퓨터의 승리로 판정되며, 프로그램을 종료합니다.\n")
        status = 0
    else:
        status = 1

    return status


# 숫자의 중복을 체크하는 함수. 만약 중복이 있으면 1, 없으면 0을 반환
def redundancy_check(num1, num2, num3, num4):
    num_tuple = (num1, num2, num3, num4)
    for i in range(4):
        for j in range(3-i):
            if num_tuple[i] == num_tuple[i+j+1]:
                return 1
            else:
                continue
    return 0


# 4자리 숫자를 받으면 class Numbers의 객체를 tuple에 담아 반환해주는 함수.
def object_generator(num):
    if num>=1000 and num<=9999:
        place_four = Numbers(num//1000, 1000)
        num -= Numbers.real_value(place_four)
        place_three = Numbers(num//100, 100)
        num -= Numbers.real_value(place_three)
        place_two = Numbers(num//10, 10)
        num -= Numbers.real_value(place_two)
        place_one = Numbers(num//1, 1)
        return (place_four, place_three, place_two, place_one)
    else:
        raise ValueError("잘못된 입력")


# Strike, Ball, Out을 판정하는 함수. 판정할 4자리 숫자(유추값), 비교할 4자리 숫자(정답값)를 입력받은 후, (S, B)를 tuple로 반환한다. (0, 0)이 반환되면 Out이며, (4, 0)이면 정답이다.
def judge_SBO(num1, num2):
    num_tuple_1 = object_generator(num1)
    num_tuple_2 = object_generator(num2)
    strike = 0
    ball = 0
    
    for i in range(4):
        for j in range(4):
            if (i==j) and (num_tuple_1[i].num == num_tuple_2[j].num):
                strike += 1
            elif (i!=j) and (num_tuple_1[i].num == num_tuple_2[j].num):
                ball += 1
            else:
                continue
    return (strike, ball)






for i in range(1000, 10000):
    thou, hund, ten, one = object_generator(i)
    result = redundancy_check(thou.num, hund.num, ten.num, one.num)
    if result == 1:
        continue
    else:
        answer_cand.append(i)

answer_index = random.randrange(len(answer_cand))
com_answer = answer_cand[answer_index]


# 유저가 플레이 시에 넘어오는 시작 함수
def ProgramStart(usr_name):
    print("\n환영합니다, "+usr_name+"님. 숫자야구 프로그램을 시작합니다.\n")
    resp = input("시작하려면 Enter 키를 누르세요.")
    
    status = 1
    while status == 1:
        if usr_guess() == 0 or com_guess() == 0:
            break
