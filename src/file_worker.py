import json
import os
from abc import ABC, abstractmethod
from config import DATA_DIR


class Worker(ABC):

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

    def __init__(self, filename='vacancies.json'):
        self.__filename = os.path.join(DATA_DIR, filename)

    @property
    def filename(self):
        return self.__filename

    def read_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding="UTF-8") as f:
                return json.load(f)
        else:
            return []

    def write_file(self, ser_vacs):
        data = self.read_file()
        vacancy_list = []
        for i in ser_vacs:
            if i in data:
                continue
            else:
                vacancy_list.append(i)
        with open(self.filename, 'w', encoding="UTF-8") as f:
            json.dump(vacancy_list, f, ensure_ascii=False, indent=4)

    @staticmethod
    def serialize(vacancies):
        vac_list = []
        for i in vacancies:
            vac_list.append(
                {
                    "name": i['name'],
                    "link": i["alternate_url"],
                    "salary": i['salary'],
                    'snippet': i['snippet'],
                    "area": i['area']
                }
            )
        return vac_list

    def add_vacancy(self, vacancy):
        pass

    def del_vacancy(self, vacancy):
        pass
