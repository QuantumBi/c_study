import os
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.prompt import Confirm, IntPrompt
from rich.columns import Columns
from rich import print as rprint



console = Console()

cart_spisok = {}


def first_command():
    number = int(input("Что хочешь сделать?\t"))
    if number == 1:
        cart_add()
    elif number == 2:
        my_cart()
    elif number == 3:
        remove_cart()
    elif number == 4:
        end_menu()
    elif number == 5:
        exist = input("Вы действительно хотите выйти?\t[y/n]\t").lower()
        if exist == "y":
            print("Досвидания!")
            return 0
        else:
            return 1



def first_menu(): #Начальный юзер экран
    kassa_menu = """\n Выбери одну позицию\n
1. Добавить товар
2. Что в корзине
3. Очистить корзину
4. Создать чек
5. Завершить работу"""
    rprint(Align(Panel.fit(kassa_menu, title="Kacca.py"), align="center"))



def my_cart():# Функция по отображению корзины с продуктами
    global cart_spisok
    if len(cart_spisok) > 0:
        table = Table(title="Корзина")
        table.add_column("Твои продукты", justify="left", style="cyan")
        table.add_column("Цена продуктов", justify="left", style="magenta")
        for name, price in cart_spisok.items():
            table.add_row(name, str(price))

        console.print(table)
    else:
        print("Корзина пока что пуста\n")

def remove_cart():
    global cart_spisok
    approval = input("Вы точно уверены что хотите очистить корзину?\t[y/n]\t").lower()
    if approval == "y":
        cart_spisok.clear()
        print("Корзина чиста\n")

def sudo_remove_cart():
    global cart_spisok
    cart_spisok.clear()
    print("Корзина чиста\n")

def cart_add(): #Функциюю для добавления продуктов в корзину
    global cart_spisok
    name = input("Что хотите добавить в корзину?\t")
    price = int(input("Уточните цену товара?\t"))
    cart_spisok[name] = price
    print("Вы добавили свой товар!\n")



def summator(spis_dict):
    sum_ = 0
    for key, value in spis_dict.items():
        sum_ += value
    return sum_

def end_menu():#Конечный юзер экран
    global cart_spisok
    user_name = os.getlogin()
    count_cart = len(cart_spisok)
    summa_cart = summator(cart_spisok)
    end_check = ("      Большое спасибо за покупку!\n\t  Будем ждать вас ещё!\n________________________________________\nКол-во товаров:\t {}\nОбщая стоимость: {}\nПокупатель:\t {}\n\nАдрес магазина: Grove Street... Home...".format(count_cart, summa_cart, user_name))
    rprint(Align(Panel(end_check, title="Чек"), align="center"))
    sudo_remove_cart()



first_menu()

while True:
    back = first_command()
    if back == 0:
        break
    else:
        continue

