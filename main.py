import datetime
from abc import ABC, abstractmethod
import random

class Validator:
    @staticmethod
    def validate(value, typ, max_len, min_value=0):
        """Функция валидации значений"""
        if isinstance(value, typ):
            if typ in (int, float):
                return min_value <= value <= max_len
            elif typ == str:
                return len(str(value)) < max_len and len(str(value)) > min_value
            
        else:
            print("Невалидное значение")
            return False


class Human(ABC):

    "Абстрактный класс"

    _name = ""

    def get_name(self):
        "Геттер - отдает имя клиента"
        return self._name

    def set_name(self, name: str):
        "Сеттер - назначает (переназначает) имя клиента"
        if Validator.validate(name, str, 200):
            self._name = name
            

    @abstractmethod
    def say_hello(self):
        pass


class Client(Human):

    _account = None
    _client_name: str = " "

    def __init__(self, client_name: str):
        self._account = None
        self.set_name(client_name)
        print(f"Клиент {client_name} успешно создан!")

    def say_hello(self):
        print("hello", self.get_name())

    def open_account(self, type_account: str, balance: float):
        "Функция открытия счёта"
        self._account = Account(type_account, balance, id = random.randint(10,10000))
        return self._account


    def request_summ(self, summ: float):
        "Функция инициализации запроса на списание"
        request = Request(self._account, summ, datetime.datetime.now(), self)
        return request

class Account:
    _type: str = ""
    _balance: float = 0
    _id: int = 0

    def __init__(self, type: str, balance: float, id: int):
        self.set_account_type(type)
        self.set_accont_id(id)
        self.set_account_balance(balance)
        print(f"Счёт {self.get_account_id()} успешно создан!")

    def write_money(self, summ: float):
        "Функция списания средств со счёта"
        if summ > 0 and self.check_summ(summ):
            self._balance -= summ
            print("Списание выполнено успешно!")
            return True
        else:
            print("Недостаточно средств!")
            return False

    def add_money(self, summ: float):
        "Функция пополнения баланса"
        self._balance += summ

    def get_account_id(self):
        "Геттер - отдает id счета"
        return self._id

    def get_account_type(self):
        "Геттер - отдает тип счета"
        return self._type

    def check_summ(self,summ:float):
        "Метод проверяет возможность списания средств со счёта"
        return self._balance >= summ


    def get_account_balance(self):
        "Геттер - отдает баланс счета"
        print(f"Текущий баланс: {self._balance} рублей")
        return self._balance

    def set_account_balance(self, balance: float):
        if Validator.validate(balance, float, 50000000000):
            self._balance = balance

    def set_account_type(self, new_type: str):
        "Сеттер - назначает тип счёта"
        if Validator.validate(new_type, str, 300):
            self._type = new_type

    def set_accont_id(self, id:int):
        "Сеттер - назначает ID счёта"
        self._id = id


class Request:
    _client: Client = None 
    _summ = 0.0
    _account: Account = None #Композиция
    _date: datetime

    def __init__(self, account: Account, summ: float, date: datetime, client:Client):
        self._account = account
        self.set_request_summ(summ)
        self.set_request_date(date)
        self._client = client
        print(f"Создан запрос на списание от счёта c id {self._account.get_account_id()}")

    def proc(self):
        "Функция обработки запроса на списание"
        if self._account.write_money(self._summ): # Делегирование
            return True
        else:
            print("Недостаточно средств на счете")
            return False

    "Геттеры"


    def get_request_summ(self):
        "Геттер - отдает сумму запроса"
        return self._summ

    def get_request_date(self):
        "Геттер - отдает дату запроса"
        return self._date

    "Сеттеры"

    def set_request_summ(self, new_summ: float):
        if Validator.validate(new_summ, float, 100000):
            self._summ = new_summ

    def set_request_date(self, new_date: str):
            self._date = new_date

    def check_the_compliance(self, client):
        if isinstance(client, Client) and client._account == self._account:
            return True
        return False

    def check_the_possibility(self, account, summ):
        return account.check_summ(summ)  # Проверка возможности списания со счёта

    def check_request(self):
        if self.check_the_possibility(self._account, self._summ) and self.check_the_compliance(self._client):
            return True
        return False


class Manager(Client):
    def say_hello(self):
        print("hello, i'm manager", self.get_name()) 
    

    def make_request(self, request: Request):
            if request.check_request():
                return request.proc()
            return "Недостаточно средств на счете"


Kostya = Client("Костя")

acc = Kostya.open_account("RUB", 200000000.0)

spisanie_1 = Kostya.request_summ(19500.0)


manager = Manager("PETYA")



manager.make_request(spisanie_1)

acc.get_account_balance()



