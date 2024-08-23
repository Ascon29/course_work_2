from src.vacancy import Vacancy


def test_vacancy_init(vacancy_1):
    vacancy_1 = Vacancy(vacancy_1)
    assert vacancy_1.name == "Junior Python"
    assert vacancy_1.link == "https://hh.ru/vacancy/105338726"
    assert vacancy_1.salary == 0
    assert vacancy_1.description == "Создание скриптов"
    assert vacancy_1.area == "Могилев"

    assert (
        str(vacancy_1)
        == "Вакансия: Junior Python\nСсылка: https://hh.ru/vacancy/105338726\nЗарплата от: 0\nОписание: Создание скриптов\nГород: Могилев"
    )


def test_comparison(vacancy_1, vacancy_2):
    vacancy_1 = Vacancy(vacancy_1)
    vacancy_2 = Vacancy(vacancy_2)
    assert vacancy_1 < vacancy_2
