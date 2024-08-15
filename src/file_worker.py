import json
import os
from abc import ABC, abstractmethod
from config import DATA_DIR


class Worker(ABC):
    """
    Абстрактный родительский класс для чтения и записи файла
    """

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self, ser_vacs):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        pass


class JSONSaver(Worker):
    """
    Класс для чтения из файла, записи в файл списка вакансий
    Класс Worker является родительским классом
    """

    def __init__(self, filename='vacancies.json'):
        self.__filename = os.path.join(DATA_DIR, filename)

    @property
    def filename(self):
        return self.__filename

    def read_file(self):
        """
        Функция для чтения файла. Проверяет, есть ли файл. И, если есть, возвращает его содержимое.
        Иначе создает файл с указанным именем и возвращает пустой список.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding="UTF-8") as f:
                return json.load(f)
        else:
            return []

    def write_file(self, ser_vacs):
        """
        Функция для записи списка вакансий в файл. Принимает список вакансий.
        """
        data = self.read_file()
        for i in ser_vacs:
            if i in data:
                continue
            else:
                data.append(i)
        with open(self.filename, 'w', encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def serialize(vacancies):
        """
        Статический метод для сериализации списка вакансий в нужный формат
        """
        vac_list = []
        for i in vacancies:
            vac_list.append(
                {
                    "name": i['name'],
                    "link": i["alternate_url"],
                    "salary": i['salary'],
                    'description': i['snippet']['responsibility'],
                    "area": i['area']['name']
                }
            )
        return vac_list

    def add_vacancy(self, vacancy):
        pass

    def del_vacancy(self, vacancy):
        pass
