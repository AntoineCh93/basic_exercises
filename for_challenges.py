# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']

def by_one_name (names: list):
    for names in names:

        print(names)
      
by_one_name (names)

names = ['Оля', 'Петя', 'Вася', 'Маша']

def by_one_name (names: list):
    for names in names:

        print(f'{names} {len(names)}')
      
by_one_name (names)


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

def gender_by_name (names, gen):
    for name in names:
        find_gender = gen.get(name)
        if find_gender:
            m_or_f = 'M'
        else:
            m_or_f = 'Ж'
        print(f"{name} {m_or_f}")
        
gender_by_name(names, is_male)     


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
def divide_by_groups(groups):
    for group in groups: 
        number = groups.index(group)+1
        number_of_people = len(group)
        print(f'Группа:{number},{number_of_people} ')

divide_by_groups(groups)


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

def divide_by_groups(groups):
    for group in groups: 
        number = groups.index(group)+1
        names_in_group = ','.join(group)
        print(f'Номер групп:{number} ,{names_in_group} ')

divide_by_groups(groups)