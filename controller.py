from model import DataRepository, Wallet
from view import DealInterface, WalletInterface


wallet = Wallet(DataRepository().read_data())
deal = DealInterface()
wallet_interface = WalletInterface()


def save_data():
    """ Сохраняет данные."""
    DataRepository().write_data(wallet.get_deals())


def print_menu():
    """ Выводит меню"""
    print(f'''
    ДОХОДЫ: {wallet.get_balance().get('incomes')}
    РАСХОДЫ: {wallet.get_balance().get('expenses')}
    БАЛАНС: {wallet.get_balance().get('balance')}
    
    
    1 - ПОСМОТРЕТЬ СДЕЛКИ
    2 - ДОБАВИТЬ СДЕЛКУ
    3 - УДАЛИТЬ СДЕЛКУ
    4 - ИЗМЕНИТЬ СДЕЛКУ
    5 - ПОИСК СДЕЛОК 
    0 - ВЫХОД
    ''')


def show_deals():
    """ Выводит все сделки и их индексы."""
    for index, deal in enumerate(wallet.get_deals()):
        print(index, deal)


def add_deal():
    """ Добавление сделки."""
    new_deal = deal.new_deal()
    wallet.add_deal(new_deal)
    save_data()
    print('\nСделка успешно добавленна')


def delete_deal():
    """ Удаление сделки."""
    index = wallet_interface.get_index(wallet.get_deals())
    wallet.delete_deal(index)
    save_data()
    print('\nСделка успешно удалена')


def update_deal():
    """ Обновление сделки."""
    index = wallet_interface.get_index(wallet.get_deals())
    print(wallet.get_deals()[index])
    new_deal = deal.new_deal()
    wallet.update_deal(index, new_deal)
    save_data()
    print('\nСделка успешно обновлена')


def find_deals():
    """ Поиск сделки по параметрам."""
    key, value = wallet_interface.get_param()
    deals = wallet.find_deals(key, value)
    for deal in deals:
        print(deal)


def run():
    while True:
        print_menu()
        choice = input('Выберите действие: ')

        if choice == '1':
            show_deals()
        elif choice == '2':
            add_deal()
        elif choice == '3':
            delete_deal()
        elif choice == '4':
            update_deal()
        elif choice == '5':
            find_deals()
        elif choice == '0':
            break
        else:
            print('Неверный выбор. Попробуйсте снова')


if __name__ == '__main__':
    run()
