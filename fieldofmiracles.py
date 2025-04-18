my_words_list = [["динозавры", "Вымершие рептилии"], ["геометрия", "Любимый предмет Веры Игоревны"], ["окружность", "Множество всех точек на плоскости, которые равно удалены от данной точки"], ["музыкант", "Человек, который занимается музыкой"], ["кондиционер", "Бытовая техника, которую используют что бы охладить комнату"], ["роза", "Цветок, у которого есть шипы"], ["нарцисс", "Человек, который думает только о себе(так же может быть названием цветка)"], ["винсентвангог", "Известный художник, который отрезал себе ухо"], ["тетрадь", "То, в чём мы пишем на уроках"], ["ручка", "То, чем мы пишем на уроках"]]
print("FIELD OF MIRACLES")
print("Start")
print("Введите свою букву")
rounds = 3
for g in range(rounds):
    attempts = 10
    attempt_key, attempt_value = my_words_list.pop()
    idk = [" _ "] * len(attempt_key)
    for i in range(attempts):
        print("".join(idk))
        letter_or_word = input()
        if i == 0:
            if len(letter_or_word) != 1:
                print("1 раз вы можете ввести только 1 букву. -1 попытка")
                continue
            else:
                if letter_or_word not in attempt_key:
                    print("-1 попытка")
                else:
                    for n in range(len(attempt_key)):
                        if attempt_key[n] == letter_or_word:
                            idk[n] = attempt_key[n]
                            print("".join(idk))
            print("Вы хотите подсказку? Если да, то введите 1. Если нет, то 0.")
            clue = input()
            if clue != "1" and clue != "0":
                print("Вводите только 1 или 0!")
                continue
            elif clue == "1":
                print(attempt_value)
            else:
                continue
        elif i == 9:
            if len(letter_or_word) != len(attempt_key):
                print("На последней попытке вы можете вводить только слово целиком. Вы проиграли. Сейчас начнётся новый раунд")
                break
            else:
                if letter_or_word == attempt_key:
                    print("Позравляю! Вы выйграли! Сейчас начнётся новый раунд")
                    break
                else:
                    print("Вы проиграли. Сейчас начнётся новый раунд")
                    break
        else:
            if len(letter_or_word) == 1:
                if letter_or_word not in attempt_key:
                    print("-1 попытка")
                else:
                    for n in range(len(attempt_key)):
                        if attempt_key[n] == letter_or_word:
                            idk[n] = attempt_key[n]
                            print("".join(idk))
                print("Вы хотите подсказку? Если да, то введите 1. Если нет, то 0.")
                clue = input()
                if clue != "1" and clue != "0":
                    print("Вводите только 1 или 0!")
                    continue
                elif clue == "1":
                    print(attempt_value)
                else:
                    continue
            elif len(letter_or_word) == len(attempt_key):
                if letter_or_word == attempt_key:
                    print("Позравляю! Вы выйграли! Сейчас начнётся новый раунд")
                    break
            else:
                print("Можно вводить либо 1 букву либо слово целиком. -1 попытка")
                print("Вы хотите подсказку? Если да, то введите 1. Если нет, то 0.")
                clue = input()
                if clue != "1" and clue != "0":
                    print("Вводите только 1 или 0!")
                    continue
                elif clue == "1":
                    print(attempt_value)
                else:
                    continue