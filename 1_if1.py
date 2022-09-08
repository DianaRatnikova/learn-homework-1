

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

'''
Вопрос:
корректнее использовать функцию с what_to_do_index (см ниже)
или с вытаскиванием сообщений по каждому if?  
'''
def age_compose_conclusion_1(age): #не использую эту функцию, тк кажется менее красивой
    age_str = 'Возраст '
    what_to_do_msg = ''
    if age < 2:
        what_to_do_msg = what_to_do[0]
    elif age < 3:
        what_to_do_msg = what_to_do[1]
    elif age <= 6:
        what_to_do_msg = what_to_do[2]
    elif 7 <= age < 16:
        what_to_do_msg = what_to_do[3]
    elif age < 22:
        what_to_do_msg = what_to_do[4]
    elif age < 65:
        what_to_do_msg = what_to_do[5]
    elif age >= 65:
        what_to_do_msg = what_to_do[6]
    age_message=f'{age_str}{age}{what_to_do_msg}'
    return age_message



def age_compose_conclusion(age): #использую эту. Ведь она лучше?
    age_str = 'Возраст '
    what_to_do_msg = ''
    if age < 2:
        what_to_do_index = 0
    elif age < 3:
        what_to_do_index = 1
    elif age <= 6:
        what_to_do_index = 2
    elif 7 <= age < 16:
        what_to_do_index = 3
    elif age < 22:
        what_to_do_index = 4
    elif age < 65:
        what_to_do_index = 5
    elif age >= 65:
        what_to_do_index = 6
    age_message=f'{age_str}{age}{what_to_do[what_to_do_index]}'
    return age_message

'''
 Вопрос: тк хочется дать норм ответ, 
 когда пользователь вводит 0, 
 не могу запихнуть в return введённое значение (чтобы не возвращал ноль).
 Ввожу глобальную переменную. Это классная идея, или не очень?
'''
def age_raw_convert_to_int(age_raw):
    try:
      global AGE_INT
      AGE_INT = int(age_raw)
      return 1
    except ValueError:
        print("Введите число!")
        return 0


def main():
    age_raw = input("Введите Ваш возраст: ")
    while not age_raw_convert_to_int(age_raw):
        age_raw = input("Введите Ваш возраст: ")
    print(age_compose_conclusion(AGE_INT))

if __name__ == "__main__":
    main()
