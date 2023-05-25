# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = [student['first_name'] for student in students]

for name in set(names):
    count_names = names.count(name)
    print(f"{name}: {count_names}")
print('\n')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

def search_popular_name(names_list):
    names = [student['first_name'] for student in names_list]
    names_dict = {}

    for name in set(names):
        names_dict[name] = names.count(name)

    max_repit_name = max(names_dict.values())
    popular_names = {key: value for key, value in names_dict.items() if value == max_repit_name}
    return popular_names

max_names = search_popular_name(students)

print('Самое частое имя среди учеников:', end=' ')
print(*max_names.keys(), sep=(', '))
print('\n')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for school_class in range(len(school_students)):
    max_names = search_popular_name(school_students[school_class])

    print(f"Самое частое имя в классе {school_class+1}:", end=' ')
    print(*max_names.keys(), sep=(', '))
print('\n')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def count_students(class_dic, is_male):
        count_girls = 0
        count_boys = 0
        
        for names_students in class_dic ['students']:
            name = names_students['first_name']
            if is_male[name]:
                count_boys += 1
            else:
                count_girls += 1
        return {'boys':count_boys, 'girls':count_girls}

for class_dic in school:
    count_student_class = count_students(class_dic, is_male)
    print(f"Класс {class_dic['class']}: девочки {count_student_class['girls']}, мальчики {count_student_class['boys']}")  
print('\n')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
max_count_student = {'boys_class':None, 'boys':0, 'girls_class':None, 'girls':0}
for class_dic in school:
    count_stud_class = count_students(class_dic, is_male)
    if count_stud_class['boys'] > max_count_student['boys']:
        max_count_student['boys'] = count_stud_class['boys']
        max_count_student['boys_class'] = class_dic['class']

    if count_stud_class['girls'] > max_count_student['girls']:
        max_count_student['girls'] = count_stud_class['girls']
        max_count_student['girls_class'] = class_dic['class']

print("Больше всего мальчиков в классе", max_count_student['boys_class'])
print("Больше всего девочек в классе", max_count_student['girls_class'])