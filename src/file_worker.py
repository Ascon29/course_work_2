import json
import os
from abc import ABC, abstractmethod
from src.vacancy import Vacancy
from config import DATA_DIR


class Worker(ABC):

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self, vacancies):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        pass


class JSONSaver(Worker):

    def __init__(self, filename='vacancies.json'):
        self.__filename = os.path.join(DATA_DIR, filename)
        self.vacancy_list = []

    @property
    def filename(self):
        return self.__filename

    def read_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding="UTF-8") as f:
                return json.load(f)
        else:
            return []

    def write_file(self, vacancies):
        data = self.read_file()
        data.extend(vacancies)
        with open(self.filename, 'w', encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        pass

    def del_vacancy(self, vacancy):
        pass
