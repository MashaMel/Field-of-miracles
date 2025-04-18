my_words_set = ({"динозавры": "Вымершие рептилии"}, {"геометрия": "Любимый предмет Веры Игоревны"}, {"окружность": "Множество всех точек на плоскости, которые равно удалены от данной точки"}, {"музыкант": "Человек, который занимается музыкой"}, {"кондиционер": "Бытовая техника, которую используют что бы охладить комнату"}, {"роза": "Цветок, у которого есть шипы"}, {"нарцисс": "Человек, который думает только о себе(так же может быть названием цветка)"}, {"винсентвангог": "Известный художник, который отрезал себе ухо"}, {"тетрадь": "То, в чём мы пишем на уроках"}, {"ручка": "То, чем мы пишем нв уроках"})
print("FIELD OF MIRACLES")
print("Start")
print("Введите свою букву")
rounds = 3
for g in range(rounds):
    attempts = 3
    for i in range(attempts):
        attempt_key = my_words_set.pop()[0]
        attempt_value = my_words_set.pop()[1]
        idk = "_" * len(attempt_key)
        letter_or_word = input()
        print(idk)
        if i == 0:
            if len(letter_or_word) != 1:
                print("1 раз вы можете ввести только 1 букву")
            else:
                if letter_or_word not in attempt_key:
                    print("-1 попытка")
                    continue
                else:
                    for n in range(len(attempt_key)):
                        if attempt_key[n] == letter_or_word:
                            idk[n] = letter_or_word[n]
                            print(letter_or_word)
                        print("Вы хотите подсказку? Если да, то введите 1. Если нет, то 0.")
                        clue = int(input())
                        if clue != 1 and clue != 0:
                            print("Вводите только 1 или 0!")
                        elif clue == 1:
                            print(attempt_value)
                        else:
                            continue
        elif i == 1:
            if len(letter_or_word) == 1:
                if letter_or_word not in attempt_key:
                    print("-1 попытка")
                else:
                    for n in range(len(attempt_key)):
                        if attempt_key[n] == letter_or_word:
                            idk[n] = letter_or_word[n]
                            print(letter_or_word)
                        print("Вы хотите подсказку? Если да, то введите 1. Если нет, то 0.")
                        clue = int(input())
                        if clue != 1 and clue != 0:
                            print("Вводите только 1 или 0!")
                        elif clue == 1:
                            print(attempt_value)
                        else:
                            continue
            elif len(letter_or_word) == len(attempt_key):
                if letter_or_word == attempt_key:
                    print("Позравляю! Вы выйграли!")
                    break
                else:
                    print("Вы ошиблись. -1 ошибка")
                print("Вы хотите подсказку? Если да, то введите 1. Если нет, то 0.")
                clue = int(input())
                if clue != 1 and clue != 0:
                    print("Вводите только 1 или 0!")
                elif clue == 1:
                    print(attempt_value)
                else:
                    continue
        else:
            if len(letter_or_word) != len(attempt_key):
                print("На третьей попытке вы можете вводить только слово целиком")
            else:
                if letter_or_word == attempt_key:
                    print("Позравляю! Вы выйграли!")
                else:
                    print("Вы проиграли")