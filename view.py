from datetime import datetime
from typing import Union, Tuple


class DealInterface:
    """ Интерфейс для работы со сделками. """

    def _validate_date(self, date_str: str) -> Union[str, bool]:
        """ Проверяет допустимость строки с датой в формате "YYYY-MM-DD".
        Проверяет чтобы дата была в диапазоне от 2020 года до текущей даты.
        """
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            current_date = datetime.now().date()
            if date.year > 2020 and date <= current_date:
                return str(date)
            return False
        except ValueError:
            return False

    def _validate_category(self, category: str) -> Union[str, bool]:
        """ Проверяет допустимость категории."""
        categories = {
            '1': 'Доход',
            '2': 'Расход'
        }
        return categories.get(category, False)

    def _validate_amount(self, amount_str: str) -> Union[float, bool]:
        """ Проверяет допустимость суммы."""
        try:
            amount = float(amount_str)
            if amount > 0:
                return amount
            return False
        except ValueError:
            return False

    def add_date(self) -> str:
        """
        Метод запрашивает у пользователя ввод даты в формате "YYYY-MM-DD"
        и проверяет ввод с помощью метода _validate_date. Он продолжает запрашивать
        ввод, пока не будет введена допустимая дата.
        """
        while True:
            date = input('Введите дату в формате "YYYY-MM-DD": ')
            if self._validate_date(date):
                return self._validate_date(date)

    def add_category(self) -> str:
        """ Метод запрашивает у пользователя выбор категории дохода или расхода.
        Пользователю предлагается выбрать категорию, введя соответствующую цифру.
        Метод проверяет введенное значение с помощью метода _validate_category и
        продолжает запрашивать выбор, пока не будет введена допустимая категория.
        """
        while True:
            category = input('''
            1 - Доход
            2 - Расход
            Выберите категорию:
            ''')
            if self._validate_category(category):
                return self._validate_category(category)

    def add_amount(self) -> float:
        """ Метод запрашивает у пользователя ввод суммы и проверяет введенное значение
        с помощью метода _validate_amount. Он продолжает запрашивать ввод, пока не будет
        введена допустимая сумма.
        """
        while True:
            amount = input('Введите сумму: ')
            if self._validate_amount(amount):
                return self._validate_amount(amount)

    def add_comment(self) -> str:
        """ Метод запрашивает у пользователя ввод описания и проверяет чтобы дилна не превышала 50 симолов."""
        while True:
            comment = input('Введите описание: (не более 50 символов) ')
            if len(comment) <= 50:
                return comment

    def new_deal(self) -> dict:
        """ Метод запрашивает у пользователя дату, категорию, сумму и комментарий для новой сделки.
        Затем метод возвращает сделку в виде словаря.
        """
        date = self.add_date()
        category = self.add_category()
        amount = self.add_amount()
        comment = self.add_comment()

        return {'Дата': date, 'Категория': category, 'Сумма': amount, 'Описание': comment}


class WalletInterface(DealInterface):
    """ Интерфейс для работы с классом Wallet. """

    def _validate_index(self, index_str: str, lst: list) -> bool:
        """ Проверяет допустимость индекса в списке."""
        try:
            index = int(index_str)
            if 0 <= index < len(lst):
                return True
            return False
        except ValueError:
            return False

    def get_index(self, lst: list) -> int:
        """ Метод запрашивает у пользователя ввод индекса и проверяет его с помощью метода
        _validate_index. Он продолжает запрашивать ввод, пока не будет введен допустимый индекс, после чего возвращает его.
        """
        while True:
            index = input('Введите индекс: ')
            if self._validate_index(index, lst):
                return int(index)

    def get_param(self) -> Tuple[str, Union[str, float]]:
        """ Метод предлагает пользователю выбрать один из параметров (Дата/Категория/Сумма),
        после чего предлагает ввести значение для выбранного параметра
        используя методы родительского класса DealInterface.
        """
        keys = {'1': 'Дата',
                '2': 'Категория',
                '3': 'Сумма'}

        while True:
            key = input('''
            1 - Дата
            2 - Категория
            3 - Сумма
            Выберите параметр: 
            ''')
            if key in keys:
                key = keys.get(key)
                break

        if key == 'Дата':
            value = self.add_date()
        elif key == 'Категория':
            value = self.add_category()
        else:
            value = self.add_amount()

        return key, value
