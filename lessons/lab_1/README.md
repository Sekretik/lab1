# Лабораторная работа № 1
## Расчет промежуточной аттестации студентов по математике

Выдана: 07 ноября 2022

Мягкий дедлайн: 11 ноября 2022

Жесткий дедлайн: 14 ноября 2022
___
## Задание
### Основная задача: посчитать итоговые баллы каждого студента и перевести их в оценки.
Формулы для расчета итогового балла приведены на листе *Итог* в файле *Успеваемость групп*.

Перевод в оценку осуществляется следующим образом: 
* менее 50 баллов - Н/А (неаттестация)
* от 50 до 69 баллов - 3 (оценка "три"), 
* от 70 до 84 баллов - 4 (оценка "четыре"), 
* от 85 и выше - 5 (оценка "пять"). 

При получении нецелого числа баллов округление до целого производится по правилам математики.
* * *
До рассчета итоговых баллов необходимо добавить баллы за домашние задания в лист с *ДЗ*. Баллы за каждую из домашних работ находятся в отдельном файле в папке ДЗ.

Не забудьте корректно обработать данные: преобразовать типы, удалить пустые строки и столбцы, и т.д.

В итоге у вас должна получиться таблица с колонками, как в примере на листе *Итог*

ID | Посещение | Активность | % посещения | % активности | ДЗ | КТ | ИТОГ | 

\+ столбец с оценкой.

**Результат вычислений (полученную таблицу) сохраняем в отдельный файл с расширением .parquet.**

Всю обработку и вычисления производим с помощью pandas и другими средствами python, если это необходимо. Код также отправляем на проверку.
* * *
После обработки данных нужно будет построить следующие графики:
* гистограмму распределения оценок
* гистограмму распределения итоговых баллов с шагом 10
* круговую диаграмму оценок

Графики сохранить в формате .html. Гистограммы можно изобразить в одном файле.
Для построения графиков можно пользоваться любой библиотекой python для визуализации.

**Засчитывается работа с верным результатом расчета итогового балла и оценок, корректной итоговой таблицей (типы, названия и т.д.) и 3 графиками.**

**Код в формате jupyter notebook или скриптов .py**

* * *
Пример работы с подобными файлами мы рассматривали в `practice_2`.