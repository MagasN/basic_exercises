# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Последняя буква в слове {word} "{word[-1]}"', end='\n\n')


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f'В слове {word} {word.count("а")} прописных букв "a"')
print(f'А всего {word.lower().count("а")}', end='\n\n')


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
vowels = set("аеёиоуыэюя")

for letter in word.lower():
    if letter in vowels:
        count += 1
print(f'в слове {word} {count} гласных', end='\n\n')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sentence_list = [word for word in sentence.split()]
print(f'В предложении "{sentence}" {len(sentence_list)} слов(а)', end='\n\n')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence_list = [word for word in sentence.split()]

for letter in sentence_list:
    print(f'Первая буква слова "{letter}" "{letter[0]}"')
print()


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence_list = [len(word) for word in sentence.split()]

count_word_len = sum(sentence_list)
avg_word_len  = round(count_word_len/len(sentence_list))

print(f'Усреднённая длина слова в предложении "{sentence}" равна {avg_word_len}')

# Вывод усреднённой длины слова в предложении с помощью функции mean()
from statistics import mean 

sentence = 'Мы приехали в гости'
sentence_list = [len(word) for word in sentence.split()]
avg_word_len = mean(sentence_list)

print(f'Усреднённая длина слова в предложении "{sentence}" равна {avg_word_len}')
