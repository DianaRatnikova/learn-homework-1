"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def final_price_count(price_float, discount_value):
    return price_float*(1-discount_value/100)

def discounted(price, discount, max_discount=20):
    try:
        price_float = float(price)
        discount_float = float(discount)
        max_discount_float = int(max_discount)
    except (ValueError):
        print("Ошибка типов")
        return "Err"

    if max_discount_float >= 100:
        raise ValueError("Слишком большая максимальная скидка")
        
    actual_discount = 0
    if discount_float >= max_discount_float:      
        actual_discount = max_discount_float
    else:
        actual_discount = discount_float

    final_price = final_price_count(price_float, actual_discount)

    return final_price


if __name__ == "__main__":
    print("1.", discounted(100, 2))
    print("2.", discounted(100, "3"))
    print("3.", discounted("100", "4.5"))
    print("4.", discounted("five", 5))
    print("5.", discounted("сто", "десять"))
    print("6.", discounted(100.0, 5, "10"))
    print("7.", discounted(100.0, 5, 1000))