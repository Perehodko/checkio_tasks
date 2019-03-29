# -*- coding: utf-8 -*-
'''
Задание:
You are given a text, which contains different english letters and punctuation symbols. You should find the most
frequent letter in the text. The letter returned must be in lower case. While checking for the most wanted letter,
casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols,
digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet.
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105
'''


def checkio(text: str) -> str:
    # перевод строки в нижний регистр
    text = text.lower()
    # недопустимые символы '!? ,-'
    text = text.replace('!', '').replace("?", '').replace(" ", '').replace("-", "").replace(',', '')
    # убираю из строки цифры
    text = ''.join([i for i in text if not i.isdigit()])

    # перевожу строку в список
    text_list = []
    for i in text:
        text_list.append(i)

    # создаю словарь на основе списка
    my_dict = dict.fromkeys(text_list)

    # считаю количество каждой буквы в заданной строке
    for key in text:
        my_dict[key] = text.count(key)

    # нахожу букву с самым большм числом совпадений
    max_val = max(my_dict.values())

    # создаю словарь с max значениями, если max значений несколько
    # он нужен для дальнейшей сортировки
    max_dict = {}
    for key, value in my_dict.items():
        if value == max_val:
            max_dict[key] = value
            # print(key)

    return min(max_dict.keys())


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    assert checkio("Lorem ipsum dolor sit amet 0000000000000000000") == "m", "Lorem with 0000"
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    assert checkio("Lorem ipsum dolor sit amet") == "m", "Lorem"
    print("The local tests are done.")
