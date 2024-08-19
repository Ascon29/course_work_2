class Vacancy:
    """
    Класс для описания вакансии
    """

    __slots__ = ("name", "link", "salary", "description", "area")

    def __init__(self, name, link, salary, description, area):
        self.name = name
        self.link = link
        self.salary = salary
        self.description = description
        self.area = area

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
    vacancy1 = Vacancy("повар", "ссылка", 10000, "требуется повар", "Екатеринбург")
    vacancy2 = Vacancy("222", "dasd", 100, "asdsd", "dsadas")
    print(vacancy1)
    print(vacancy2 < vacancy1)
