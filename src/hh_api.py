from abc import ABC, abstractmethod

import requests
from src.vacancy import Vacancy
from config import DATA_DIR


class Parser(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        # self.vacancies_sort = []

    def load_vacancies(self, keyword):
        self.params["text"] = keyword
        while self.params.get("page") != 2:
            try:
                response = requests.get(self.__url, headers=self.__headers, params=self.params)
            except Exception as e:
                print(f'Произошла ошибка {e}')
            else:
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.params["page"] += 1

        # for vacancy in self.vacancies:
        #     name = vacancy['name'] if vacancy['name'] else 'Название не указано'
        #     link = vacancy['alternate_url'] if vacancy['alternate_url'] else 'Ссылка отсутствует'
        #     salary = vacancy['salary']['from'] if vacancy['salary'] else 'Зарплата не указана'
        #     description = vacancy["snippet"]["responsibility"] if vacancy['snippet'] else 'Описание отсутствует'
        #     area = vacancy["area"]["name"] if vacancy['area'] else 'Город не указан'
        #     self.vacancies_sort.append(Vacancy(name=name, link=link, salary=salary, description=description, area=area))

    def get_vacancies(self):
        return self.vacancies


if __name__ == "__main__":
    hh = HeadHunterAPI()
    hh.load_vacancies("Python")
    hh_vacancies = hh.get_vacancies()
    print(hh_vacancies)
