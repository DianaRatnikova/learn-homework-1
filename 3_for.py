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

# суммарное/среднее количество продаж для каждого товара
def sold_total_avg(items_sold, flag):
    sum=0
    for i in range(len(items_sold)):
        sum+=items_sold[i]
    if flag=="TOTAL":
        return sum
    elif flag=="AVG":
        return sum/len(items_sold)
    else:
        return -1


def print_phones(phones_sold):
    for phone in phones_sold:
        print('product:      ', phone['product'])
        print('sold_total:   ', phone['sold_total'])
        print('sold_average:  {:.6}'.format(phone['sold_average']))
        print("------------------------")


def main():
    sale_for_all_total=0
    sale_for_all_avg=0
    for phone in phones_sold:
        phone['sold_total']=sold_total_avg(phone['items_sold'], 'TOTAL')
        phone['sold_average']=sold_total_avg(phone['items_sold'], 'AVG')
        sale_for_all_total+=phone['sold_total']
        sale_for_all_avg+=phone['sold_average']
    sale_for_all_avg=sale_for_all_avg/len(phones_sold)
    print_phones(phones_sold)
    print("SOLD IN TOTAL:   {}".format(sale_for_all_total))
    print("SOLD IN AVERAGE: {}".format(sale_for_all_avg))

    pass
    
if __name__ == "__main__":
    print()
    main()
