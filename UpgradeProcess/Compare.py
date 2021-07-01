import AutoNumberBaseball
import AutoNumberBaseballVer1
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.image import imread
import pandas as pd
import numpy as np


# 프로그램을 시작, 종료하는 funciton이 존재해야 함. 종료 function에는 모든 초기값들이 초기화되어야 한다. 시작 function은 컴퓨터의 시도 횟수와 guess 추이를 반환해야 한다.
def auto_execute(start_func, end_func, repeat):
    list_of_guess_log = []

    list_of_attempts = []
    for i in range(repeat):
        attempts, guess_log = start_func()
        list_of_attempts.append(attempts)
        while len(guess_log) != 14:
            guess_log.append(0)
        list_of_guess_log.append(guess_log)
        end_func()
        print("%d번째 게임 끝" % (i+1))
    attempts = pd.DataFrame(list_of_attempts, columns=['attempt'])
    total_guess = pd.DataFrame(list_of_guess_log, columns=['0회', '1회', '2회', '3회', '4회', '5회', '6회', '7회', '8회', '9회', '10회', '11회', '12회', '13회'])
    total_guess.loc['Avrg.'] = total_guess.mean()

    return attempts, total_guess


Ver0_attempts, Ver0_total_guess = auto_execute(AutoNumberBaseball.ProgramStart, AutoNumberBaseball.ProgramEnd, 100)
Ver1_attempts, Ver1_total_guess = auto_execute(AutoNumberBaseballVer1.ProgramStart, AutoNumberBaseballVer1.ProgramEnd, 100)

print("-"*100)
print("\n\nVer0의 평균 시도 횟수: %.4f\nVer1의 평균 시도 횟수: %.4f" % (np.mean(Ver0_attempts.attempt), np.mean(Ver1_attempts.attempt)))

lresult = stats.levene(Ver0_attempts.attempt, Ver1_attempts.attempt)
print('\n<유의수준 0.05>\n등분산 검정 결과(F값) : %.4f \np-value : %.4f' % (lresult))


tresult = stats.ttest_ind(Ver0_attempts, Ver1_attempts, equal_var=True)
print('\n\n<유의수준 0.05>\n독립표본 등분산 t검정 결과(t값) : %.8f \np-value : %.8f' % (tresult))

tresult2 = stats.ttest_ind(Ver0_attempts, Ver1_attempts, equal_var=False)
print('\n\n<유의수준 0.05>\n독립표본 이분산 t검정 결과(t값) : %.8f \np-value : %.8f' % (tresult2))
    