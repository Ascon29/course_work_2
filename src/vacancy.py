class Vacancy:
    __slots__ = ('name', 'link', 'salary', 'description', 'area')

    def __init__(self, name, link, salary, description, area):
        self.name = name
        self.link = link
        self.salary = salary
        self.description = description
        self.area = area

    def __str__(self):
        name = f'Вакансия: {self.name}'
        link = f'Ссылка: {self.link}'
        salary = f'Зарплата: {self.salary}'
        description = f'Описание: {self.description}'
        area = f'Город: {self.area}'
        return f'{name}\n{link}\n{salary}\n{description}\n{area}'

    # @staticmethod
    # def cast_to_object_list(vacs_list):
    #     temp_vac_list = []
    #     for item in vacs_list:
    #         temp_vac_list.append(
    #             {
    #                 "name": item.name,
    #                 "link": item.link,
    #                 "salary": item.salary,
    #                 "description": item.description,
    #                 "area": item.area
    #             }
    #         )
    #     return temp_vac_list

    @classmethod
    def cast_to_object_list(cls, vacs):
        vacancies_sort = []
        for vacancy in vacs:
            name = vacancy['name'] if vacancy['name'] else 'Название не указано'
            link = vacancy['alternate_url'] if vacancy['alternate_url'] else 'Ссылка отсутствует'
            salary = vacancy['salary']['from'] if vacancy['salary'] else 'Зарплата не указана'
            description = vacancy["snippet"]["responsibility"] if vacancy['snippet'] else 'Описание отсутствует'
            area = vacancy["area"]["name"] if vacancy['area'] else 'Город не указан'
            vac = cls(name=name, link=link, salary=salary, description=description, area=area)
            vacancies_sort.append(vac)
        return vacancies_sort

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary


if __name__ == '__main__':
    vacancy1 = Vacancy("повар", "ссылка", None, "требуется повар", "Екатеринбург")
    vacancy2 = Vacancy('222', 'dasd', 0, 'asdsd', 'dsadas')
    print(vacancy1)
