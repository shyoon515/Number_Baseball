import random



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
    if num>=0 and num<=9999:
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


# 컴퓨터가 유추을 한다.
def com_guess():
    global answer_cand
    global com_trial
    global com_answer
    global guess_log
    global first_guess
    
    if com_trial == 2 and len(answer_cand) >= 10:
        thou, hund, ten, one = object_generator(first_guess)
        nums = [x for x in range(10)]

        nums.remove(thou.num)
        nums.remove(hund.num)
        nums.remove(ten.num)
        nums.remove(one.num)

        temp_index = random.randrange(len(nums))
        thou2 = Numbers(nums[temp_index], 1000)
        nums.remove(thou2.num)

        temp_index = random.randrange(len(nums))
        hund2 = Numbers(nums[temp_index], 100)
        nums.remove(hund2.num)
        
        temp_index = random.randrange(len(nums))
        ten2 = Numbers(nums[temp_index], 10)
        nums.remove(ten2.num)

        temp_index = random.randrange(len(nums))
        one2 = Numbers(nums[temp_index], 1)
        nums.remove(one2.num)

        guess = (thou2 + hund2) + (ten2 + one2)
        # print(guess)
        strike, ball = judge_SBO(guess, com_answer)
        
        com_trial += 1
        temp_list = []
        guess_sbo = (strike, ball)
        for i, num in enumerate(answer_cand):
            sbo = judge_SBO(num, guess)
            if guess_sbo == sbo:
                temp_list.append(num)
            else:
                continue
        answer_cand = temp_list
        # print("컴퓨터는 후보 정답을 ", len(temp_list), "개로 추려내었습니다!")
        guess_log.append(len(temp_list))
        # print(guess_log)

        return 1
        
        
    else:
        guess_index = random.randrange(len(answer_cand))
        # print("\n컴퓨터의 %d번째 유추: %04d" % (com_trial, answer_cand[guess_index]))
        strike, ball = judge_SBO(answer_cand[guess_index], com_answer)
        if com_trial == 1:
            first_guess = answer_cand[guess_index]
        
        if strike == 4:
            # print("\n컴퓨터가 정답을 구하였습니다. 답은 "+str(answer_cand[guess_index])+"입니다. "+str(com_trial)+"번 만에 맞추었습니다. 프로그램을 종료합니다.\n")
            # print("컴퓨터의 답: %04d" % com_answer)
            return 0
        com_trial += 1
        temp_list = []
        guess_sbo = (strike, ball)
        for i, num in enumerate(answer_cand):
            sbo = judge_SBO(num, answer_cand[guess_index])
            if guess_sbo == sbo:
                temp_list.append(num)
            else:
                continue
        answer_cand = temp_list
        # print("컴퓨터는 후보 정답을 ", len(temp_list), "개로 추려내었습니다!")
        guess_log.append(len(temp_list))
        # print(guess_log)

        return 1





answer_cand = []
com_trial = 1
first_guess = 0

for i in range(10000):
    thou, hund, ten, one = object_generator(i)
    result = redundancy_check(thou.num, hund.num, ten.num, one.num)
    if result == 1:
        continue
    else:
        answer_cand.append(i)

answer_index = random.randrange(len(answer_cand))
com_answer = answer_cand[answer_index]

guess_log = [len(answer_cand)]


def ProgramStart():
    global guess_log
    status = 1
    while status == 1:
        status = com_guess()
    return com_trial, guess_log

def ProgramEnd():
    global answer_cand
    global com_answer
    global com_trial
    global guess_log
    global first_guess
    
    answer_cand = []
    
    for i in range(10000):
        thou, hund, ten, one = object_generator(i)
        result = redundancy_check(thou.num, hund.num, ten.num, one.num)
        if result == 1:
            continue
        else:
            answer_cand.append(i)
    
    answer_index = random.randrange(len(answer_cand))
    com_answer = answer_cand[answer_index]
    
    com_trial=1
    guess_log = [len(answer_cand)]
    first_guess = 0

