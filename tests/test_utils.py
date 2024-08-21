from src.utils import FilterSortVacancies
from src.vacancy import Vacancy


def test_filter_init():
    test = FilterSortVacancies(filter_word="python", filter_area="москва", filter_salary=0, top_n=5)
    assert test.filter_word == "python"
    assert test.filter_area == "москва"
    assert test.filter_salary == 0
    assert test.top_n == 5


def test_filter_by_description(vac_list_1):
    test = FilterSortVacancies(filter_word="Создание", filter_area="Могилев", filter_salary=0, top_n=5)
    assert test.filter_by_description(vac_list_1) == [
        Vacancy(
            name="Junior Python",
            link="https://hh.ru/vacancy/105338726",
            salary=0,
            description="Создание скриптов",
            area="Могилев",
        )
    ]


def test_filter_by_area(vac_list_1):
    test = FilterSortVacancies(filter_word="Создание", filter_area="Москва", filter_salary=0, top_n=5)
    assert test.filter_by_area(vac_list_1) == [
        Vacancy(
            name="Senior Python",
            link="https://hh.ru/vacancy/105338726",
            salary=10000,
            description="Приглашаем Инженера",
            area="Москва",
        )
    ]


def test_filter_by_salary(vac_list_1):
    test = FilterSortVacancies(filter_word="Создание", filter_area="Москва", filter_salary=10, top_n=5)
    assert test.filter_by_area(vac_list_1) == [
        Vacancy(
            name="Senior Python",
            link="https://hh.ru/vacancy/105338726",
            salary=10000,
            description="Приглашаем Инженера",
            area="Москва",
        )
    ]


def test_sort_vacancies_by_salary(vac_list_1):
    test = FilterSortVacancies(filter_word="Создание", filter_area="Москва", filter_salary=10, top_n=5)
    assert test.sort_vacancies_by_salary(vac_list_1) == [
        Vacancy(
            name="Senior Python",
            link="https://hh.ru/vacancy/105338726",
            salary=10000,
            description="Приглашаем Инженера",
            area="Москва",
        ),
        Vacancy(
            name="Junior Python",
            link="https://hh.ru/vacancy/105338726",
            salary=0,
            description="Создание скриптов",
            area="Могилев",
        ),
    ]


def test_get_top_vacancies(vac_list_1):
    test = FilterSortVacancies(filter_word="Создание", filter_area="Москва", filter_salary=10, top_n=5)
    assert test.get_top_vacancies(vac_list_1) == (
        "Вакансия номер 1:\nВакансия: Junior Python\nСсылка: https://hh.ru/vacancy/105338726\nЗарплата от: 0\nОписание: Создание скриптов\nГород: Могилев\n\nВакансия номер 2:\nВакансия: Senior Python\nСсылка: https://hh.ru/vacancy/105338726\nЗарплата от: 10000\nОписание: Приглашаем Инженера\nГород: Москва\n\n"
    )
