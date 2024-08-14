from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.file_worker import JSONSaver


# Функция для взаимодействия с пользователем
def user_interaction():
    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий с hh.ru в формате JSON
    hh_api.load_vacancies(search_query)
    hh_vacancies = hh_api.get_vacancies()
    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    serialized_vacancies = json_saver.serialize(hh_vacancies)
    json_saver.write_file(serialized_vacancies)

    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    #
    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
