"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара +
* Посчитать и вывести среднее количество продаж для каждого товара  +
* Посчитать и вывести суммарное количество продаж всех товаров  +
* Посчитать и вывести среднее количество продаж всех товаров    +
"""

phones_sold=  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


# суммарноеколичество продаж для каждого товара
def total(items_sold):
    return sum(items_sold)

# среднее количество продаж для каждого товара
def avg(items_sold):
    return sum(items_sold)/len(items_sold)


def print_phones(phones_sold):
    for phone in phones_sold:
        print('product:      ', phone['product'])
        print('sold_total:   ', phone['sold_total'])
        print(f"sold_average:  {sold_average:.6f}")
        print("------------------------")


def main():
    sale_for_all_total=0
    sale_for_all_avg=0
    for phone in phones_sold:
        phone['sold_total']=total(phone['items_sold'])
        phone['sold_average']=avg(phone['items_sold'])
        sale_for_all_total+=phone['sold_total']
        sale_for_all_avg+=phone['sold_average']
    sale_for_all_avg=sale_for_all_avg/len(phones_sold)
    print_phones(phones_sold)
    print(f"SOLD IN TOTAL:   {sale_for_all_total}")
    print(f"SOLD IN AVERAGE: {sale_for_all_avg}")

    pass
    
if __name__ == "__main__":
    main()
