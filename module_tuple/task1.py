## "Ревью кода".

# В задании словарь из трех студентов. Необходимо:
# 1. Вывести на экран список пар "ID студента - возраст".
# 2. Написать функцию, которая принимает в качестве аргумента
#    словарь и возвращает два значения: полный список интересов
#    всех студентов и общую длину всех фамилий студентов.

def interests_len_surname(user_dict):
    interests_list = []
    len_surname = 0
    for _, data in students.items():
        if data.get('surname'):
            len_surname += len(data['surname'])
        if data.get('interests'):
            interests_list.extend(data['interests'])

    return set(interests_list), len_surname


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

id_age_list = [(id_student, data_student.get('age')) for id_student, data_student in students.items()]
print('"ID студента - возраст":', id_age_list)

interests, len_surnames = interests_len_surname(students)

print('Полный список интересов всех студентов:', interests)
print('Общая длина всех фамилий студентов:', len_surnames)

