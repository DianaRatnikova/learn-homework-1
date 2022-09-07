"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

what_to_do = [
    ' - Да быть такого не может', # 0 - меньше 2
    ' - Пора в ясли!',            # 1 - от 2 до 3
    ' - Иди в сад :)',            # 2 - от 3 до 6
    ' - Учись в школе',           # 3 - от 7 до 16
    ' - Ботай в  ВУЗе',           # 4 - от 16 до 22
    ' - Можно и поработать',      # 5 - от 22 до 65
    ' - Хватит работать, пора на пенсию'#6 - больше 65
     ]


def age_conclusion(age):
    age_str='Возраст '
    if age < 2:
        age_message=f'{age_str}{age}{what_to_do[0]}'
    elif age < 3:
        age_message=f'{age_str}{age}{what_to_do[1]}'
    elif age <= 6:
        age_message=f'{age_str}{age}{what_to_do[2]}'
    elif 7 <= age < 16:
        age_message=f'{age_str}{age}{what_to_do[3]}'
    elif age < 22:
        age_message=f'{age_str}{age}{what_to_do[4]}'
    elif age < 65:
        age_message=f'{age_str}{age}{what_to_do[5]}'
    elif age >= 65:
        age_message=f'{age_str}{age}{what_to_do[6]}'
    return age_message


def age_raw_convert_to_int(age_raw):
    if type(age_raw)!=int:
        try:
            age_int=int(age_raw)
            return age_int
        except ValueError:
            print("Введите число!")
            return 0


def main():
    age_raw=input("Введите Ваш возраст:")
    while not age_raw_convert_to_int(age_raw):
            age_raw=input("Введите Ваш возраст:")
    print(age_conclusion(age_raw_convert_to_int(age_raw)))

if __name__ == "__main__":
    main()
