from csv import reader
import xml.etree.ElementTree as ET

def count():
    table = open_table()
    c=0
    for row in table:
        if len(row[1])>30:
            c+=1
    print(c)



def find_string(searchline, string):
    string = string.lower()
    index = string.find(searchline.lower())
    return index

def search():
    table = open_table()
    searchline = input('Поиск: ')
    flag = 0
    for row in table:
        if find_string(searchline, row[2]) !=-1 and (int(row[3])<1990):
            print(row)
            flag+=1
    if flag ==0:
        print('Ничего')
    else:
        print(f'Найдено: {flag}')

def find_publishers():
    table = open_table()
    publishers = set()
    for row in table:
        publishers.add(row[4])
    for pub in publishers:
        print(pub)


def rating(r):
    table = open_table()
    items = [j for j in table]
    items.sort(key = lambda i: int(i[5]))
    items.reverse()
    items = items[:r]
    output = open('result.txt', 'w')
    output.write(f'20 популярных книг:\n\n')
    print('Самые популярные книги:')
    for i in range(r):
        print(i+1, items[i][1], items[i][5], 'скачиваний')
        output.write(f'{i+1} Автор: {items[i][2]}. Название: {items[i][1]} - {items[i][3]} год\n\n')

def give_currency():
    file = ET.parse('currency.xml')
    root = file.getroot()
    currency_list = []
    for currency in root.findall('Valute'):
        if int(currency.find('Nominal').text)==1:
            currency_name = currency.find('Name').text
            currency_list.append(currency_name)
    print(currency_list)


f = open('books.csv', 'r')
def open_table():
    f.seek(0)
    k = f.readline()
    table = reader(f, delimiter=';')
    return table

# count() # Вывести количество записей, у которых в поле Название строка длиннее 30 символов.
# search() # Реализовать поиск книги по автору, использовать ограничение на выдачу в зависимости от варианта.
# rating(20) # Самые популярные 20 книг + Реализовать генератор библиографических ссылок вида <автор>. <название> - <год> для 20 записей. Записи выбрать произвольно. Список сохраняется как отдельный файл текстового формата с нумерацией строк.
# give_currency() # Распарсить файл и извлечь данные, согласно варианту. Выполнить приведения типов по необходимости.
# find_publishers() # Вывести перечень всех тегов без повторений (для books-en.csv - перечень издательств без повторений).
f.close()