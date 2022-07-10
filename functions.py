# Импортируем модуль JSON для работы с этим форматом
import json

def load_candidates(file_with_candidates):
    """
    :param file_with_candidates: Файл с кандидатами формата JSON
    :return: Список кандидатов
    """
    with open(file_with_candidates, encoding="utf-8") as file:
        candidates = json.loads(file.read())
    return candidates


def get_student_by_pk(list_with_students, pk):
    """
    :param list_with_students: Список студентов
    :param pk: Номер студента
    :return: Данные студента
    """
    for i in list_with_students:
        if i["pk"] == pk:
            return i["full_name"], i["skills"]
    return False


def get_profession_by_title(list_with_professions, title):
    """
    :param list_with_professions: Список профессий с навыками
    :param title: Название профессии
    :return: Список навыков для профессии
    """
    for i in list_with_professions:
        if i["title"].lower() == title.lower():
            return i["skills"]
    return False


def check_fitness(student, profession):
    """
    :param student: Студент для оценки
    :param profession: Профессия для оценки
    :return: Оценка студента
    """
    student_fitness = dict()
    set_of_student = set(student)
    set_of_profession = set(profession)
    set_of_student.intersection_update(set_of_profession)
    student_fitness["fitness"] = list(set_of_student)
    fitness_percent = int(len(set_of_student) / len(set_of_profession) * 100)
    student_fitness["fitness_percent"] = fitness_percent
    set_of_profession.difference_update(set_of_student)
    student_fitness["unfitness"] = list(set_of_profession)
    return student_fitness
