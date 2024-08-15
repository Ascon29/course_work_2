import re
from src.file_worker import JSONSaver
from src.vacancy import Vacancy

json_saver = JSONSaver()
vacs_list_from_json = json_saver.read_file()

vacs_list_for_user = []
for vacancy in vacs_list_from_json:
    name = vacancy['name']
    link = vacancy['link']
    salary = vacancy['salary']
    description = vacancy['description']
    area = vacancy['name']
    vacs_list_for_user.append(Vacancy(name, link, salary, description, area))

# for vacancy in vacs_list_from_json:
#     print(Vacancy(**vacancy))


class FilterVacancies:

    def __init__(self, vacancies_list):
        self.vacancies_list = vacancies_list

    def filter_vacancies(self, filter_words):
        pass

    def sort_vacancies(self):
        pass

    def get_top_vacancies(self):
        pass

