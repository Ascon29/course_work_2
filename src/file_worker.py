import json
import os
from abc import ABC, abstractmethod
from typing import List

from config import DATA_DIR
from src.vacancy import Vacancy


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
    def del_vacancy(self):
        pass


class JSONSaver(Worker):
    """
    Класс для чтения из файла, записи в файл списка вакансий
    Класс Worker является родительским классом
    """

    filename_value = "vacancies.json"

    def __init__(self, filename=filename_value):
        self.vacs_list = []
        self.__filename = os.path.join(DATA_DIR, filename)

    @property
    def filename(self):
        return self.__filename

    def read_file(self):
        """
        Функция для чтения файла. Проверяет, есть ли файл. И, если есть, сохраняет список объектов
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="UTF-8") as f:
                vacs = json.load(f)
            self.vacs_list = [Vacancy(i) for i in vacs]
        return self.vacs_list

    def write_file(self, vacs_obj: List):
        """
        Функция для записи списка вакансий в файл. Принимает список объектов класса Vacancy.
        """
        vacs_list = []
        for i in vacs_obj:
            vacs_list.append(
                {
                    "name": Vacancy(i).name,
                    "alternate_url": Vacancy(i).link,
                    "salary": {"from": Vacancy(i).salary},
                    "snippet": {"responsibility": Vacancy(i).description},
                    "area": {"name": Vacancy(i).area},
                }
            )
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(vacs_list, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        pass

    def del_vacancy(self):
        with open(self.filename, "w") as f:
            pass
