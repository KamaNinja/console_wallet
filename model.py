import json
from typing import Union, List


class DataRepository:
    """ Класс для работы с файлами (Чтение/Запись)."""

    def __init__(self):
        self.file_path = 'deals.json'

    def read_data(self):
        """ Чтение данных и возврат."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=3)
        return data

    def write_data(self, data):
        """ Запись данных в файл."""
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=3)


class Wallet:
    """ Класс для работы со списком сделок (CRUD)."""

    def __init__(self, deals: List[dict]):
        self.__deals = deals

    def __get_amount_by_category(self, category: str) -> float:
        """Метод принимает категорию (Доход/Расход) в качестве аргумента и возвращает сумму доходов/расходов"""
        total = sum(i['Сумма'] for i in self.__deals if i['Категория'] == category)
        return total

    def get_balance(self) -> dict:
        """Метод возвращает словарь в котором содержатся расходы, доходы, и баланс."""
        incomes = self.__get_amount_by_category('Доход')
        expenses = self.__get_amount_by_category('Расход')
        balance = incomes - expenses
        return {'incomes': incomes, 'expenses': expenses, 'balance': balance}

    def get_deals(self) -> List[dict]:
        """Возврат списка сделок."""
        return self.__deals

    def add_deal(self, deal: dict) -> None:
        """Добавление новой сделки."""
        self.__deals.append(deal)

    def delete_deal(self, index: int) -> None:
        """Удаление сделки по индексу."""
        del self.__deals[index]

    def update_deal(self, index, deal) -> None:
        """Обновление сделки.
        Метод принимает 2 аргумента, индекс и новую сделку и заменяет по индексу старую сделку на новую."""
        self.__deals[index] = deal

    def find_deals(self, key: str, value: Union[str, float]) -> list:
        """Находит и возращает сделки по заданному ключу и значению."""
        result = []
        for deal in self.__deals:
            if deal.get(key) == value:
                result.append(deal)
        return result
