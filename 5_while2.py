"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

ANSWERS_DICT = {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую",
    "Когда отпуск?": "Не знаю",
    "1": "ONE"
}


def ask_user():
    question=''
    while not ANSWERS_DICT.get(question):
        question=input('Задайте мне вопрос: ')
        print(ANSWERS_DICT.get(question, "НихтФерштейн"))


if __name__ == "__main__":
    ask_user()
