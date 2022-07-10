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
