"""Задание 44 |
| --- |
| В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его
в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head() |"""
import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

unique_values = list(set(lst))

one_hot = pd.DataFrame({value: [int(value == category) for category in lst] for value in unique_values})
data = pd.concat([data, one_hot], axis=1)   # обьеденим данные по столбцам axis=1

print(data)  # для отображения не более 5 строк можем использовать (data.head())
