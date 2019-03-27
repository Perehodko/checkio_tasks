'''
Задание:
The function should recognise if a subject line is stressful. A stressful subject line means that all letters
are in uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following
“red” words: "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP",
"help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP"

Input: Subject line as a string.
Output: Boolean.
Precondition: Subject can be up to 100 letters
'''


def is_stressful(subj):
    # Список слов, на которые надо реагировать
    stressful_list = ["help", "asap", "urgent"]

    # Результат, котрый возвращает функция
    result = False

    # Длина полученного слова
    len_subj = len(subj)

    # Если последние три символа "!!!", значит письмо срочное
    if "!!!" in subj[(len_subj) - 3:]:
        result = True
    # Если весь текст в верхнем регистре, значит письмо тоже срочное
    elif subj.isupper() == True:
        result = True
    # Если первые два условия не про нас, то идем дальше
    else:
        # Преобразуем строку в нижний регистр
        lowercase_subj = subj.lower()

        # Убираем лишние символы из строки
        clean_subj1 = lowercase_subj.replace("!", "")
        clean_subj2 = clean_subj1.replace("-", "")
        clean_subj3 = clean_subj2.replace(".", "")

        # Отладочная информация
        # print(clean_subj2)

        # Добавляю один символ в конец строки
        clean_subj = clean_subj3 + "a"

        # Сюда буду записывать слово без повторений символов
        new_word = []

        # Если текущий и следующий за ним символ не совпадает, то записываю его в new_word
        for j in range(0, len(clean_subj) - 1, 1):
            # print(clean_subj[j])
            if clean_subj[j] == clean_subj[j + 1]:
                continue
            else:
                new_word.append(clean_subj[j])

        # Преобразаую список в строку
        my_string = "".join(new_word)

        # Проверяю есть ли одно из стресс-слов из списка stressful_list в моей строке
        for i in stressful_list:
            if i in my_string:
                result = True
            else:
                pass

    # Возвращаю результат
    if result == True:
        return True
    else:
        return False


if __name__ == '__main__':
    # Asserts для самопроверки
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("where are you?!!!!") == True, "Third"
    assert is_stressful("UUUURGGGEEEEENT here") == True, "Fourth"
    assert is_stressful("HI HOW ARE YOU?") == True, "Fifth"
    print('Done!')
