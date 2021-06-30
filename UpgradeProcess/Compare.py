import AutoNumberBaseball
import matplotlib.pyplot as plt
from matplotlib.image import imread
import pandas as pd

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
    total_guess.loc['Avrg.'] = total_guess.mean()
    print(total_guess)
    return average_attmpt, total_guess
    #plt.plot([0,1,2,3,4,5,6,7,8,9], list_of_guess_log[0])
    #plt.xlabel('Attempts')
    #plt.ylabel('Possible Answer')
    #plt.title('Possible Answer Log of Ver 0')
    #plt.savefig('/workspace/Number_Baseball/UpgradeProcess/Ver_0')

auto_execute(AutoNumberBaseball.ProgramStart, AutoNumberBaseball.ProgramEnd, 10)