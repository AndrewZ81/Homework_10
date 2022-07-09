from flask import Flask
app = Flask(__name__)

@app.route("/")
def page_index():
    return "ПРИВЕТ!"

@app.route("/profile/")
def page_profile():
    return "Профиль пользователя"

@app.route("/feed/")
def page_feed():
    return "Лента пользователя"

@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"

if __name__ == "__main__":
    app.run(host="127.0.0.2", port=80)
