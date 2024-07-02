import pandas as pd

data = {
                'name': ['Alice','Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
                'математика': [3, 5, 4, 3, 5, 4, 3, 5, 4, 3],
                'геометрия': [5, 4, 3, 5, 4, 3, 5, 4, 3, 5],
                'физика': [2, 4, 3, 5, 4, 3, 2, 4, 3, 5],
                'информатика': [4, 3, 5, 4, 3, 5, 4, 3, 5, 4],
                'история': [5, 5, 4, 3, 5, 4, 3, 5, 4, 3]
    }

df = pd.DataFrame(data)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

print(f"Средняя оценка по математике - {df['математика'].mean()}")
print(f"Медианная оценка по математике - {df['математика'].median()}")
print(f"Стандартное отклонение по математике -{df['математика'].std()}")

print(f"Средняя оценка по геометрии - {df['геометрия'].mean()}")
print(f"Медианная оценка по геометрии - {df['геометрия'].median()}")
print(f"Стандартное отклонение по геометрии -{df['геометрия'].std()}")

print(f"Средняя оценка по физике - {df['физика'].mean()}")
print(f"Медианная оценка по физике - {df['физика'].median()}")
print(f"Стандартное отклонение по физике -{df['физика'].std()}")

print(f"Средняя оценка по информатике - {df['информатика'].mean()}")
print(f"Медианная оценка по информатике - {df['информатика'].median()}")
print(f"Стандартное отклонение по информатике -{df['информатика'].std()}")

print(f"Средняя оценка по истории - {df['история'].mean()}")
print(f"Медианная оценка по истории  - {df['история'].median()}")
print(f"Стандартное отклонение по истории  -{df['история'].std()}")

Q1_math = df['математика'].quantile(0.25)
Q3_math = df['математика'].quantile(0.75)
IQR = Q3_math - Q1_math
print(f"Границы интервала для математики Q1_math - {Q1_math},  Q3_math- {Q3_math}, IQR - {IQR}")


# Фильтрация данных для Alice
alice_data = df[df['name'] == 'Alice']
# Вычисление средней оценки по всем предметам
average_grade_alice = alice_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
print(f"Средняя оценка для Alice: {average_grade_alice}")
Bob_data = df[df['name'] == 'Bob']
average_grade_bob = Bob_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
print(f"Средняя оценка для Bob: {average_grade_bob}")
Charlie_data = df[df['name'] == 'Charlie']
average_grade_charlie = Charlie_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
print(f"Средняя оценка для Charlie: {average_grade_charlie}")
David_data = df[df['name'] == 'David']
average_grade_david = David_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
print(f"Средняя оценка для David: {average_grade_david}")
Eve_data = df[df['name'] == 'Eve']
average_grade_eve = Eve_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
print(f"Средняя оценка для Eve: {average_grade_eve}")
Frank_data = df[df['name'] == 'Frank']
average_grade_frank = Frank_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
print(f"Средняя оценка для Frank: {average_grade_frank}")
Grace_data = df[df['name'] == 'Grace']
average_grade_grace = Grace_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
print(f"Средняя оценка для Grace: {average_grade_grace}")
Henry_data = df[df['name'] == 'Henry']
average_grade_henry = Henry_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
print(f"Средняя оценка для Henry: {average_grade_henry}")
Ivy_data = df[df['name'] == 'Ivy']
average_grade_ivy = Ivy_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
print(f"Средняя оценка для Ivy: {average_grade_ivy}")
Jack_data = df[df['name'] == 'Jack']
average_grade_jack = Jack_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
print(f"Средняя оценка для Jack: {average_grade_jack}")