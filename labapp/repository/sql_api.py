from typing import List

from config import DB_URL       # параметры подключения к БД из модуля конфигурации config.py
from .connectorfactory import SQLStoreConnectorFactory

from .connector import StoreConnector


"""
    В данном модуле реализуется API (Application Programming Interface)
    для взаимодействия с БД с помощью объектов-коннекторов.
    
    ВАЖНО! Методы должны быть названы таким образом, чтобы по названию
    можно было понять выполняемые действия.
"""


def select_all_from_climbing() -> List[tuple]:
    """ Вывод списка гор с сортировкой по сложности восхождения в порядке возрастания и по квалификации гида в порядке убывания"""
    connector = open_connection()
    query = f"SELECT * FROM climbing ORDER BY difficulty_of_climbing ASC, guide_qualification DESC "

    result = connector.execute(query).fetchall()
    connector.end_transaction()
    connector.close()
    return result


def select_one_climbing_by_id(climbing_id: int) -> tuple:
    """ Получение записи о восхождении по идентификатору записи """
    connector = open_connection()
    query = f"SELECT * FROM climbing WHERE id = {climbing_id}"
    result = connector.execute(query).fetchone()
    connector.end_transaction()
    connector.close()
    return result


def select_all_from_climbings_by_mountain_name(mountain) -> List[tuple]:
    """ Поиск автомобилей, используя полное или частичное совпадение искомой строки
        в наименовании горы """
    connector = open_connection()
    query = f"SELECT * FROM climbing where mountain LIKE '%{mountain}%'"
    result = connector.execute(query).fetchall()
    connector.end_transaction()
    connector.close()
    return result


def insert_into_climbing(mountain: str, difficulty_of_climbing: int, country: str, guide: str, guide_qualification: int):
    """ Вставка новой записи в таблицу climbing """
    connector = open_connection()
    query = f"INSERT INTO climbing (mountain, difficulty_of_climbing, country, guide, guide_qualification)" \
            f" VALUES ('{mountain}', '{difficulty_of_climbing}', '{country}', '{guide}', '{guide_qualification}')"
    result = connector.execute(query)
    connector.end_transaction()
    connector.close()
    return result


def update_climbing_by_id(climbing_id: int, mountain: str = "none", difficulty_of_climbing: int = 0, country: str = "none",
                          guide: str = "none", guide_qualification: int = 0):
    """ Обновление значений записи о восхождение по идентификатору.
        В функции установлены значения по умолчанию, в случае, если поля формы были незаполнены"""
    connector = open_connection()
    query = f"UPDATE climbing SET mountain = '{mountain}', difficulty_of_climbing = '{difficulty_of_climbing}'," \
            f" country = '{country}', guide = '{guide}', guide_qualification = {guide_qualification} WHERE id = {climbing_id}"
    result = connector.execute(query)
    connector.end_transaction()
    connector.close()
    return result


def delete_climbing_by_mountain_name(mountain: str) -> List[tuple]:
    """ Удаление записи о восхождении по названию горы """
    connector = open_connection()
    query = f"DELETE FROM climbing where mountain = '{mountain}'"
    result = connector.execute(query)
    connector.end_transaction()
    connector.close()
    return result


def delete_climbing_by_id(climbing_id: int) -> List[tuple]:
    """ Удаление записи в таблице по идентификатору """
    connector = open_connection()
    query = f"DELETE FROM climbing where id = {climbing_id}"
    result = connector.execute(query)
    connector.end_transaction()
    connector.close()
    return result


def open_connection() -> StoreConnector:
    """ Функция открывает соединение для выполнения запросов """
    connector = SQLStoreConnectorFactory().get_connector(DB_URL)  # инициализируем соединение
    connector.start_transaction()  # начинаем выполнение запросов (открываем транзакцию)
    return connector


