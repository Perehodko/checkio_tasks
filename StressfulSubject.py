def is_stressful(subj):

    # список слов, на которые надо реагировать
    stressful_list = ["help", "asap", "urgent"]

    # результат, котрый возвращает функция
    result = False

    # длина полученного слова
    len_subj = len(subj)

    # если последние три символа "!!!" значит письмо срочное
    if "!!!" in subj[(len_subj) - 3:]:
        result = True
    # если весь текст в верзнем регистре, значит письмо тоже срочное
    elif subj.isupper() == True:
        result = True
    # если первые два условия не про нас, то идем дальше
    else:
        # преобразакм строку в нижний регистр
        lowercase_subj = subj.lower()

        # убираем лишние символы из строки
        clean_subj1 = lowercase_subj.replace("!", "")
        clean_subj2 = clean_subj1.replace("-", "")
        clean_subj3 = clean_subj2.replace(".", "")

        # Отладочная информация
        # print(clean_subj2)

        # добавляю один символ в конец строки
        clean_subj = clean_subj3 + "a"

        # сюда буду записывать слово без повторений
        new_word = []

        # если текущий и следующий за ним символ не совпадает,
        # то записываю его в new_word
        for j in range(0, len(clean_subj) - 1, 1):
            # print(clean_subj[j])
            if clean_subj[j] == clean_subj[j + 1]:
                continue
            else:
                new_word.append(clean_subj[j])

        # Преобразаую список в строку
        my_string = "".join(new_word)

        # Проверяю есть ли одно из стресс-слов из списка stressful_list
        # в строке my_string
        for i in stressful_list:
            if i in my_string:
                result = True
            else:
                pass

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
