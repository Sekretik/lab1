import pandas as pd
import numpy as np
import math, os

visiting_table = pd.read_excel('lessons\\lab_1\\Успеваемость групп.xlsx',sheet_name='Посещение', header=None,skiprows=3)
homeworck_table = pd.read_excel('lessons\\lab_1\\Успеваемость групп.xlsx',sheet_name='ДЗ', header=None,skiprows=3)
test_table = pd.read_excel('lessons\\lab_1\\Успеваемость групп.xlsx',sheet_name='КТ', header=None,skiprows=2)

path = 'lessons\\lab_1\\ДЗ\\'

dir =  os.listdir(path=path)

for file in dir:
    ids_dict = {}
    number = int(file[0])

    hw_table = pd.read_excel(path+file)
    for i in range(len(hw_table)):
        ids_dict[hw_table.iloc[i,7]] = round(hw_table.iloc[i,6])

    for i in range(len(homeworck_table)):
        student = homeworck_table.iloc[i,0]
        if(student in ids_dict):
            homeworck_table.loc[i,number] = ids_dict[student]

def getVisitingByStudent(index):
    vis = 0
    vis_count = 0
    for i in range(1,len(visiting_table.iloc[index]),2):
        count = visiting_table.iloc[index,i]
        if(not math.isnan(count)):
            vis += count
            vis_count += 1
    return vis, vis_count

def getActivitygByStudent(index):
    act = 0
    for i in range(2,len(visiting_table.iloc[index]),2):
        count = visiting_table.iloc[index,i]
        if(not math.isnan(count)):
            act += count
    return act

def getHomeworkByStudent(index):
    hw = 0
    hw_count = 0
    for i in range(1,len(homeworck_table.iloc[index])):
        count = homeworck_table.iloc[index,i]
        if(not isinstance(count,str) and not math.isnan(count)):
            hw += count
            hw_count += 1
    return hw, hw_count

def getTestByStudent(index):
    index += 1
    test = 0
    test_count = 0
    for i in range(1,len(test_table.iloc[index])):
        count = test_table.iloc[index,i]
        if(isinstance(count,str) and count != 'н'):
            count = count.replace(',','.')
            count = float(count)
        if((not isinstance(count,str) and not math.isnan(count))):
            test += count
            test_count += test_table.iloc[0,i]
        elif(count == 'н'):
            test_count += test_table.iloc[0,i]

    return test, test_count

IDs = []
visiting = []
activity = []
pct_visiting = []
pct_activity = []
homeworck_scores = []
test_scores = []
results = []
scores = []

for i in range(len(visiting_table)):
    id = visiting_table.iloc[i,0]
    vis_count, max_vis_count = getVisitingByStudent(i)
    act_count = getActivitygByStudent(i)
    hw_score, max_hw_score = getHomeworkByStudent(i)
    test_score, max_test_score = getTestByStudent(i)

    IDs.append(id)
    visiting.append(round(vis_count))
    activity.append(round(act_count))
    pct_visiting.append(round(vis_count/max_vis_count*100))
    pct_activity.append(round(act_count/max_vis_count*100))
    homeworck_scores.append(round(hw_score/6))
    test_scores.append(round(test_score/max_test_score*100))
    results.append(round(0.1 * (0.7*pct_visiting[i]+0.3*pct_activity[i])+0.2*homeworck_scores[i]+0.7*test_scores[i]))

    score = ''

    if(results[i] < 50):
        score = 'Н/А'
    elif(results[i] < 70):
        score = '3'
    elif(results[i] < 85):
        score = '4'
    else:
        score = '5'

    scores.append(score)

table = pd.DataFrame({'ID':IDs,'Посещение':visiting,'Активность':activity,'% посещения':pct_visiting,'% активности':pct_activity,'ДЗ':homeworck_scores,'КТ':test_scores,'ИТОГ':results,'Оценка':scores})

#print(table)

table.to_parquet('lessons\\lab_1\\table.parquet',engine='fastparquet')