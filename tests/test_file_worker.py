import os

from config import DATA_DIR
from src.file_worker import JSONSaver
from src.vacancy import Vacancy


def test_init():
    assert JSONSaver().filename == os.path.join(DATA_DIR, "vacancies.json")


def test_serialize_for_json(hh_vacs_list, serialized_for_json):
    test = JSONSaver()
    assert test.serialize_for_json(hh_vacs_list) == serialized_for_json


def test_serialize_for_user(serialized):
    test = JSONSaver()
    assert test.serialize_for_user(serialized) == [
        Vacancy(
            name="Junior Python",
            link="https://hh.ru/vacancy/105338726",
            salary=10,
            description="Создание скриптов",
            area="Могилев",
        )
    ]
