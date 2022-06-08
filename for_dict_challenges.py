from collections import defaultdict
from email.quoprimime import body_check
from html.entities import name2codepoint
from webbrowser import get

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


students_dict = {}
for name in students:
    the_name = name['first_name']
    if the_name in students_dict: 
        students_dict[the_name] += 1
    else:
        students_dict[the_name] = 1
for the_name in students_dict:
    print(f'{the_name}: {students_dict[the_name]}')


# counting_names(students)       
# def counting_names(students):
#     calcul = defaultdict(int)
#     for one_name in students:
#         name = one_name['first_name']
#         calcul[name] += 1
#     for name in calcul:
#         name_count = calcul[name]
#         print(name, name_count)

# counting_names(students)
       



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

 


def common_name (students):
    calcul = defaultdict(int)
    for one_name in students: 
        name = one_name['first_name']
    for name in calcul:
        calcul[name] += 1
        print(max(calcul, key = (calcul.get)))
        
common_name (students)



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

def common_name (school_students):
    # calcul = defaultdict(int)
    count_class = 1
    for school_class in school_students: 
        max_child = {}
        for child in school_class:
            name = child['first_name']
            if max_child.get[name]:
                max_child[name] += 1
            else:
                max_child[name] = 1     
        print(max_child)       #больше всего учеников
        popular_name = ""
        for key, item in max_child.items():
            if item == "":
                popular_name = key
            if max_child[popular_name] < item:
                popular_name = key

        print(f"{count_class} самое популярное имя {popular_name}")
        count_class += 1

    # for key, child in calcul.items():
    #     print(key, child)    
        
common_name (school_students)


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
def Who_in_class (school):
    for school_class in school:
        m = 0
        f = 0
        for student in school_class['students']:
            name = student.get('first_name')
            if is_male[name]:
                m += 1
            else:
                f += 1
        print(f'В классе {school_class["class"]}: мальчики {m}, девочки {f}')
Who_in_class (school)        

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

maximum_m = ['',0]
maximum_f = ['',0]

def Who_in_class_more (school):
    for school_class in school:
        m = 0
        f = 0
        for student in school_class['students']:
            name = student.get('first_name')
            if is_male[name]:
                m += 1
            else:
                f += 1
        
         
        if m > maximum_m [1]:
            maximum_m[0] = school_class['class']
            maximum_m[1] = m
        if f > maximum_f [1]:
            maximum_f[0] = school_class['class']
            maximum_f[1] = f   

    print(f'в класcе больше мальчиков {maximum_m[0]}')
    print(f'в класcе больше девочек {maximum_f[0]}')

        # print(f'В классе {school_class["class"]}: мальчики {m}, девочки {f}')
Who_in_class_more (school)  

