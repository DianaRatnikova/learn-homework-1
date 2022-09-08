
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
#phones_sold_etalon
phones_sold =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

'''
Словари для тестирования.
Надо ли их сохранять на случай дальнейшей доработки проги?
'''
phones_sold_nodata = []

phones_sold_no_sold =  [
    {'product': 'iPhone 12', 'items_sold': []},
    {'product': 'Xiaomi Mi11', 'items_sold': []},
    {'product': 'Samsung Galaxy 21', 'items_sold': []},
  ]


# среднее количество продаж для каждого товара
def avg(items_sold):
    sold_in_average=0
    sold_in_average = sum(items_sold)/len(items_sold)
    return sold_in_average


def print_phones(phones_sold):
    for phone in phones_sold:
        print(f"product:      {phone['product']}" )
        print(f"sold_total:   {phone['sold_total']}")
        print(f"sold_average: {phone['sold_average']:.6}")
        print("------------------------")


def main():
    sale_for_all_total = 0
    sale_avg_onephone = 0
    if not phones_sold:              #если весь словарь пустой
        print('Нет данных о товарах')
    else:
        for phone in phones_sold:
            if not phone.get('items_sold'):
                print(f"{phone['product']}:  Нет данных о продажах") # указать название телефона
            else:
                phone['sold_total'] = sum(phone['items_sold'])  
                phone['sold_average'] = avg(phone['items_sold'])
                sale_for_all_total += phone['sold_total']
        if phone.get('items_sold'):
            print_phones(phones_sold)    
            sale_for_all_avg = sum(avg['sold_average'] for avg in phones_sold)/len(phones_sold)
            print(f"SOLD IN TOTAL:   {sale_for_all_total}")
            print(f"SOLD IN AVERAGE: {sale_for_all_avg}")
    
if __name__ == "__main__":
    main()
