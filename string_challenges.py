# Вывести последнюю букву в слове
from itertools import count


word = 'Архангельск'

print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'

print(word.lower().count('a'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
for vowel in word.lower():
    if vowel in 'ае':
        count += 1
 
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
count = 0
for word in sentence.split(' '):
    if word in sentence:
        count += 1 

print(count)



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

for letter in sentence.split(' '):
    print(letter[0])



# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

def count_average(sentence):
    words = sentence.split()
    counting_word = len(words)
    counting_letters = 0
    for one_word in words:
        counting_letters += len(one_word)
    average_number = counting_letters / counting_word
    print(average_number)
count_average(sentence)
    