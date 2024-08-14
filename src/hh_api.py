from abc import ABC, abstractmethod

import requests


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
        self.validate_vacancies = []

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

        for vacancy in self.vacancies:
            if vacancy['name'] is None:
                vacancy['name'] = 'Название не указано'
            if vacancy['alternate_url'] is None:
                vacancy['alternate_url'] = 'Ссылка отсутствует'
            if vacancy['salary'] is None:
                vacancy['salary'] = 'Зарплата не указана'
            if vacancy['snippet'] is None:
                vacancy["snippet"]["responsibility"] = 'Описание отсутствует'
            if vacancy["area"] is None:
                vacancy["area"]["name"] = 'Город не указан'
            self.validate_vacancies.append(vacancy)

    def get_vacancies(self):
        return self.validate_vacancies


if __name__ == "__main__":
    hh = HeadHunterAPI()
    hh.load_vacancies("Python")
    hh_vacancies = hh.get_vacancies()
    print(hh_vacancies)
