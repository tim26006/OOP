from bank import *

def main():

    client1 = Client("John") # Создание клиента
    acc1 = client1.open_account("rub", 200500.0)   # открытие клиентом счёта с балансом

    client1.get_name() # Получение имени клиента

    manager1 = Manager("Vasiliy")  # Создание менеджера

    request1 = client1.request_summ(210000.0) #Инициализация клиентом запроса на списание средств со счета

    manager1.make_request(request1) # Проведение запроса на списание



if __name__ == "__main__":
    main()