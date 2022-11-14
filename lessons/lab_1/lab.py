import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

visiting_table = pd.read_excel('lessons\\lab_1\\Успеваемость групп.xlsx',sheet_name='Посещение', header=None)
homework_table = pd.read_excel('lessons\\lab_1\\Успеваемость групп.xlsx',sheet_name='ДЗ', header=None,skiprows=3)
test_table = pd.read_excel('lessons\\lab_1\\Успеваемость групп.xlsx',sheet_name='КТ', header=None,skiprows=2)

columns = visiting_table.loc[[0,2]].T
columns = columns.ffill(limit=1)

visiting_table.columns = pd.MultiIndex.from_frame(columns)
visiting_table = visiting_table.drop(index=[0, 1, 2])
visiting_table = visiting_table.dropna(how='all', axis=1)

visiting_table = visiting_table.set_index(visiting_table[(np.nan, 'ID')].squeeze().values)
visiting_table = visiting_table.drop(columns=(np.nan, 'ID'))
visiting_table.index.name = 'ID'

path = 'lessons\\lab_1\\ДЗ\\'

dir =  os.listdir(path=path)

hw_table = pd.DataFrame()

for file in dir:
    ids_dict = {}
    number = file[0]

    hw = pd.read_excel(path+file)

    hw_table[0]  = hw['ID']
    hw_table[number]  = hw['Процент правильных ответов (%)']

homework_table = homework_table.replace(r'^\s*$', np.nan, regex=True).dropna(axis=0,how='all').dropna(axis=1,how='all')
homework_table = homework_table.merge(hw_table,how='left',on=0).replace(np.nan, 0, regex=True)
homework_table = round(homework_table)

homework_table = homework_table.set_index(homework_table[0].squeeze().values)
homework_table = homework_table.drop(columns=(0))
homework_table.index.name = 'ID'

test_table = test_table.set_index(test_table[0].squeeze().values)
test_table = test_table.drop(columns=(0))
test_table.index.name = 'ID'
test_table = test_table.replace(r'^\s*$', np.nan, regex=True).dropna(axis=0,how='all').dropna(axis=1,how='all')
test_table = test_table.replace(np.nan, 0, regex=True).replace('н', 0, regex=True)

test_max_scores = test_table.iloc[0,len(test_table.iloc[0])-1]

test_table = test_table.drop(index='ID').drop(columns=test_table.columns[len(test_table.columns)-1])

def getVisitingByStudent():
    vis = visiting_table.iloc[:, visiting_table.columns.get_level_values(1) == 'посещ-е'].sum(axis=1)
    vis_count = sum(visiting_table.columns.get_level_values(1) == 'посещ-е')
    return vis, vis_count

def getActivitygByStudent():
    act = visiting_table.iloc[:, visiting_table.columns.get_level_values(1) == 'актив'].sum(axis=1)
    return act

def getHomeworkByStudent():
    hw = homework_table.sum(axis=1)
    hw_count = len(homework_table.columns)
    return hw, hw_count

def getTestByStudent():
    test = test_table.sum(axis=1)

    return test

IDs = visiting_table.index
visiting, max_vis_count = getVisitingByStudent()
activity = round(getActivitygByStudent())
pct_visiting = round(visiting / max_vis_count * 100)
pct_activity = round(activity / max_vis_count * 100)
homework_scores, homework_count = getHomeworkByStudent()
homework_scores = round(homework_scores / homework_count)
test_scores = round(getTestByStudent()/test_max_scores * 100)
results = round(0.1 * (0.7*pct_visiting+0.3*pct_activity)+0.2*homework_scores+0.7*test_scores)

table = pd.DataFrame({'Посещение':visiting,'Активность':activity,'% посещения':pct_visiting,'% активности':pct_activity,'ДЗ':homework_scores,'КТ':test_scores,'Итог':results,'Оценка':''})

table['Оценка'] = np.where(table['Итог'] < 50, 'Н/А',np.where(table['Итог'] < 70, '3',np.where(table['Итог'] < 85, '4','5')))

print(table)

table.to_parquet('lessons\\lab_1\\table.parquet',engine='fastparquet')

plt.subplot(2,2,1)
plt.hist(table['Оценка'],bins=['Н/А','3','4','5'])
plt.subplot(2,2,2)
plt.hist(table['Итог'],bins=[0,10,20,30,40,50,60,70,80,90,100])
plt.subplot(2,2,3)
plt.pie(table['Оценка'].value_counts(),labels=table['Оценка'].value_counts().index)

plt.show()