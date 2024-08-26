class Vacancy:
    """
    Класс для описания вакансии
    """

    __slots__ = ("__name", "__link", "__salary", "__description", "__area")

    def __init__(self, vac):
        self.__name = vac["name"] if vac["name"] else "Название не указано"
        self.__link = vac["alternate_url"] if vac["alternate_url"] else "Ссылка не указана"
        self.__salary = vac["salary"]["from"] if vac["salary"] and vac["salary"]["from"] else 0
        self.__description = (
            vac["snippet"]["responsibility"]
            if vac["snippet"] and vac["snippet"]["responsibility"]
            else "Описание отсутствует"
        )
        self.__area = vac["area"]["name"] if vac["area"] and vac["area"]["name"] else "Город не указан"

    @property
    def name(self):
        return self.__name

    @property
    def link(self):
        return self.__link

    @property
    def salary(self):
        return self.__salary

    @property
    def description(self):
        return self.__description

    @property
    def area(self):
        return self.__area

    def __str__(self) -> str:
        name = f"Вакансия: {self.name}"
        link = f"Ссылка: {self.link}"
        salary = f"Зарплата от: {self.salary}"
        description = f"Описание: {self.description}"
        area = f"Город: {self.area}"
        return f"{name}\n{link}\n{salary}\n{description}\n{area}"

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary


if __name__ == "__main__":
    vacancy1 = {
        "name": "повар",
        "alternate_url": "ссылка",
        "salary": {"from": 10000},
        "snippet": {"responsibility": "требуется повар"},
        "area": {"name": "Екатеринбург"},
    }
    vacancy2 = {"name": "таксист", "alternate_url": None, "salary": None, "snippet": None, "area": None}
    x = Vacancy(vacancy1)
    print(x)
    y = Vacancy(vacancy2)
    print(y)
