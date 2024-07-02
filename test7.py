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

subjects = ['математика', 'геометрия', 'физика', 'информатика', 'история']

for subject in subjects:
    print(f"Средняя оценка по {subject} - {df[subject].mean()}")
    print(f"Медианная оценка по {subject} - {df[subject].median()}")
    print(f"Стандартное отклонение по {subject} - {df[subject].std()}")

Q1_math = df['математика'].quantile(0.25)
Q3_math = df['математика'].quantile(0.75)
IQR = Q3_math - Q1_math
print(f"Границы интервала для математики Q1_math - {Q1_math}, Q3_math - {Q3_math}, IQR - {IQR}")

# Вычисление средней оценки для каждого студента
students = df['name'].unique()
for student in students:
    student_data = df[df['name'] == student]
    average_grade = student_data[['математика', 'геометрия', 'физика', 'информатика', 'история']].mean(axis=1).values[0]
    print(f"Средняя оценка для {student}: {average_grade}")
