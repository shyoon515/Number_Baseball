import AutoNumberBaseball
import AutoNumberBaseballVer1
import matplotlib.pyplot as plt
from matplotlib.image import imread
import pandas as pd


# 프로그램을 시작, 종료하는 funciton이 존재해야 함. 종료 function에는 모든 초기값들이 초기화되어야 한다. 시작 function은 컴퓨터의 시도 횟수와 guess 추이를 반환해야 한다.
def auto_execute(start_func, end_func, repeat):
    list_of_guess_log = []

    sum_attempt = 0
    for i in range(repeat):
        attempts, guess_log = start_func()
        sum_attempt += attempts
        while len(guess_log) != 14:
            guess_log.append(0)
        list_of_guess_log.append(guess_log)
        end_func()
        print("%d번째 게임 끝" % (i+1))
    average_attmpt = sum_attempt/repeat
    total_guess = pd.DataFrame(list_of_guess_log, columns=['0회', '1회', '2회', '3회', '4회', '5회', '6회', '7회', '8회', '9회', '10회', '11회', '12회', '13회'])
    total_guess.loc['Avrg.'] = total_guess.mean()    # 평균 행이 추가된 DataFrame 객체
    return average_attmpt, total_guess
    # plt.plot([0,1,2,3,4,5,6,7,8,9], list_of_guess_log[0])
    # plt.xlabel('Attempts')
    # plt.ylabel('Possible Answer')
    # plt.title('Possible Answer Log of Ver 0')
    # plt.savefig('/workspace/Number_Baseball/UpgradeProcess/Ver_0')

data_of_attempt = []
data_of_attempt2 = []
for i in range(100):
    average_attmpt, total_guess = auto_execute(AutoNumberBaseball.ProgramStart, AutoNumberBaseball.ProgramEnd, 20)
    average_attmpt2, total_guess2 = auto_execute(AutoNumberBaseballVer1.ProgramStart, AutoNumberBaseballVer1.ProgramEnd, 20)
    data_of_attempt.append(average_attmpt)
    data_of_attempt2.append(average_attmpt2)
    print("\n------------------------------------\n%d번째 반복 끝\n\n" % (i+1))

print(data_of_attempt, data_of_attempt2)

bins = [x/10 for x in range(40, 70, 2)]


fig = plt.figure(figsize=(8, 12))

#plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.2, hspace=0.5)

plt.subplot(2, 1, 1)
plt.hist(data_of_attempt, bins, rwidth = 0.8, color='b')
plt.xlabel('Average Attempts')
plt.ylabel('Count')
plt.title('Ver0 Histogram')
plt.grid

plt.subplot(2, 1, 2)
plt.hist(data_of_attempt2, bins, rwidth = 0.8, color='g')
plt.xlabel('Average Attempts')
plt.ylabel('Count')
plt.title('Ver1 Histogram')
plt.grid

plt.savefig('/workspace/Number_Baseball/UpgradeProcess/Ver_0_1')

# 표본 당 개수 50개, 표본개수 100개로 비교한 결과, Ver0은 평균 5.4746회, Ver1은 평균 5.5716회 만에 정답을 구하였다.

#print(total_guess)
#print(total_guess2)
#print("\n")
#print(average_attmpt, average_attmpt2)