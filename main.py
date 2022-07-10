# Импортируем модуль functions для работы с форматом JSON
import functions

# Читаем список кандидатов
candidates = functions.load_candidates("candidates.json")

# Импортируем класс Flask
from flask import Flask

# Создаём экземпляр Flask
app = Flask(__name__)

# Создаём корневой маршрут
@app.route("/")
def get_all():
    """
    :return: Преформатированную строку кандидатов
    """
    list_of_candidates_for_output = []
    for i in candidates:
        list_of_candidates_for_output.append("Имя кандидата - " + i["name"])
        list_of_candidates_for_output.append("Позиция кандидата - " + i["position"])
        list_of_candidates_for_output.append("Навыки кандидата -  " + i["skills"] + "\n\n")
    string_of_candidates_for_output = "\n".join(list_of_candidates_for_output)
    return f"<pre>{string_of_candidates_for_output}</pre>"


# Создаём маршрут для выборки кандидата
@app.route("/candidates/<int:id>")
def get_by_pk(id):
    """
    :param id: Идентификатор (номер) кандидата
    :return: Данные кандидата по его номеру
    """
    list_of_candidate_for_output = []
    for i in candidates:
        if i["pk"] == id:
            url = i["picture"]
            list_of_candidate_for_output.append("Имя кандидата - " + i["name"])
            list_of_candidate_for_output.append("Позиция кандидата - " + i["position"])
            list_of_candidate_for_output.append("Навыки кандидата -  " + i["skills"] + "\n\n")
    string_of_candidate_for_output = "\n".join(list_of_candidate_for_output)
    return f"<img src={url}><pre>{string_of_candidate_for_output}</pre>"


# Запускаем сервер
app.run()
